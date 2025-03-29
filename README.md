# GADI-email_filter
GADI EMAIL FILTER is a Python-based tool that cleans bulk email lists by cross-checking new emails against an existing database. It removes duplicates, filters invalid emails, and logs removed entries. With a user-friendly Tkinter GUI, backup creation, multiple file support, and a summary report, it ensures efficient and accurate email management.

## Features

- 📂 Bulk Email Cross-Check – Compares new emails with an existing database and removes duplicates.
- ✅ Invalid Email Detection – Identifies and removes improperly formatted emails (e.g., missing `@`).
- 📊 Summary Report – Provides counts of removed, invalid, and remaining emails.
- 💾 Automatic Backup – Saves a backup of the collected emails before modification.
- 🔄 Multiple File Support – Allows importing multiple files for comparison.
- 🖥 User-Friendly GUI – Built with Tkinter or PyQt for easy operation.
- Fast Processing – Optimized for handling large datasets (~1 crore emails).
🛠️ Requirements & Installation
Before running the project, ensure your system has the necessary dependencies installed.

### 📌 Requirements
- Python 3.7+
- Required libraries: `pandas`, `openpyxl`, `tkinter`

## Installation of Tool

1. Clone the repository*
   ```sh
   git clone https://github.com/20501A0407/GADI-email_filter.git
   cd GADI-email_filter
   ```
2. Install dependencies*
   ```sh
   pip install -r requirements.txt
   ```

After installation follow the below steps to run the application

##🔧 Running the Tool
Navigate to the project directory and execute the script:

```sh
cd path/to/GADI-email_filter  # Change to the project directory
python email_filter_tool.py  # Run the tool
```

If using a GUI version:

```sh
python gui_tool.py
```

## 📂 How to Use
1. **Upload Database**: Load your existing email dataset (CSV/Excel).
2. **Select Collected Emails File**: Choose the new email data file for filtering.
3. **Run the Process**: Click the button to start filtering.
4. **View Results**: Check the logs and reports for filtered data.

## License

This project is licensed under the MIT License – you are free to modify and distribute it.

## Contributing

Feel free to submit pull requests for improvements!


