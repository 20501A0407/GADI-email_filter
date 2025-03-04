import os
import datetime
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import re

def extract_email(text):
    """Extract email if it contains @, otherwise return None."""
    match = re.search(r'[\w\.-]+@[\w\.-]+', str(text))
    return match.group(0).lower() if match else None

def find_email_column(df):
    """Auto-detect email column based on common names and @ symbol presence."""
    common_names = ["email", "e-mail", "email address", "emails"]
    for col in df.columns:
        if col.lower() in common_names:
            return col
    for col in df.columns:
        if df[col].astype(str).str.contains(r'@').any():
            return col
    return None

def safe_read_csv(file_path):
    """Try reading CSV with multiple encodings to avoid errors."""
    encodings = ["utf-8", "ISO-8859-1", "latin1"]
    for enc in encodings:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except UnicodeDecodeError:
            continue
    return pd.read_csv(file_path, encoding="utf-8", errors="ignore")

def create_backup(file_path):
    """Create a timestamped backup of the collected file before modification."""
    backup_folder = os.path.join(os.path.dirname(file_path), "backups")
    os.makedirs(backup_folder, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    file_name, ext = os.path.splitext(os.path.basename(file_path))
    backup_file = os.path.join(backup_folder, f"{file_name}_backup_{timestamp}{ext}")

    shutil.copy2(file_path, backup_file)
    return backup_file

def process_files():
    existing_files = filedialog.askopenfilenames(
        title="Select Existing Emails Files",
        filetypes=[("CSV & Excel Files", "*.csv;*.xlsx"), ("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")]
    )
    
    collected_file = filedialog.askopenfilename(
        title="Select Collected Emails File",
        filetypes=[("CSV & Excel Files", "*.csv;*.xlsx"), ("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")]
    )

    if not existing_files or not collected_file:
        messagebox.showwarning("Warning", "Please select both existing and collected email files.")
        return

    try:
        progress_bar["value"] = 10
        root.update_idletasks()

        backup_path = create_backup(collected_file)
        print(f"Backup created: {backup_path}")

        existing_emails = set()
        for file in existing_files:
            if file.endswith(".csv"):
                df = safe_read_csv(file)
            else:
                df = pd.read_excel(file)
                
            email_col = find_email_column(df)
            if email_col:
                existing_emails.update(df[email_col].dropna().apply(extract_email))
        
        progress_bar["value"] = 40
        root.update_idletasks()

        if collected_file.endswith(".csv"):
            collected_df = safe_read_csv(collected_file)
        else:
            collected_df = pd.read_excel(collected_file)

        collected_email_col = find_email_column(collected_df)

        if not collected_email_col:
            messagebox.showerror("Error", "Could not find an email column in the collected file!")
            return

        total_collected = len(collected_df)

        collected_df["Valid Email"] = collected_df[collected_email_col].apply(extract_email)
        invalid_df = collected_df[collected_df["Valid Email"].isna()]
        collected_df = collected_df.dropna(subset=["Valid Email"])

        progress_bar["value"] = 60
        root.update_idletasks()

        removed_df = collected_df[collected_df["Valid Email"].isin(existing_emails)]
        filtered_df = collected_df[~collected_df["Valid Email"].isin(existing_emails)].drop(columns=["Valid Email"])

        progress_bar["value"] = 80
        root.update_idletasks()

        removed_count = len(removed_df)
        invalid_count = len(invalid_df)
        remaining_count = len(filtered_df)

        removed_file = "removed_emails.xlsx"
        invalid_file = "invalid_emails.xlsx"

        if collected_file.endswith(".xlsx"):
            filtered_df.to_excel(collected_file, index=False)
            removed_df.to_excel(removed_file, index=False)
            invalid_df.to_excel(invalid_file, index=False)
        else:
            filtered_df.to_csv(collected_file, index=False, encoding="utf-8")
            removed_df.to_csv("removed_emails.csv", index=False, encoding="utf-8")
            invalid_df.to_csv("invalid_emails.csv", index=False, encoding="utf-8")

        progress_bar["value"] = 100
        root.update_idletasks()

        # Show summary in UI
        summary_text.set(
            f"📊 Summary Report\n"
            f"🔹 Total Collected Emails: {total_collected}\n"
            f"✅ Valid Emails: {total_collected - invalid_count}\n"
            f"❌ Removed Emails: {removed_count}\n"
            f"🚫 Invalid Emails: {invalid_count}\n"
            f"📌 Remaining Emails: {remaining_count}"
        )

        messagebox.showinfo("Success", f"Processing completed!\n\n✅ Backup: {backup_path}\n✅ Removed Emails: {removed_count}\n✅ Invalid Emails: {invalid_count}\n✅ Remaining Emails: {remaining_count}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        progress_bar["value"] = 0

# GUI Setup
root = tk.Tk()
root.title("Email Filter Tool")
root.geometry("420x450")

tk.Label(root, text="📌 Select Files and Process", font=("Arial", 12)).pack(pady=10)
process_button = tk.Button(root, text="📂 Select Files & Start", command=process_files, font=("Arial", 10), bg="lightblue")
process_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Summary Label
summary_text = tk.StringVar()
summary_label = tk.Label(root, textvariable=summary_text, font=("Arial", 10), justify="left", anchor="w")
summary_label.pack(pady=10, padx=20)

root.mainloop()
