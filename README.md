# GADI-email_filter
GADI EMAIL FILTER is a Python-based tool that cleans bulk email lists by cross-checking new emails against an existing database. It removes duplicates, filters invalid emails, and logs removed entries. With a user-friendly Tkinter GUI, backup creation, multiple file support, and a summary report, it ensures efficient and accurate email management.

## Features

- 📂 Bulk Email Cross-Check – Compares new emails with an existing database and removes duplicates.
- ✅ Invalid Email Detection – Identifies and removes improperly formatted emails (e.g., missing `@`).
- 📊 Summary Report – Provides counts of removed, invalid, and remaining emails.
- 💾 Automatic Backup – Saves a backup of the collected emails before modification.
- 🔄 Multiple File Support – Allows importing multiple files for comparison.
- 🖥 User-Friendly GUI – Built with Tkinter or PyQt for easy operation.
- 🚀 Fast Processing – Optimized for handling large datasets (~1 crore emails).

## Installation

1. Clone the repository*
   ```sh
   git clone https://github.com/20501A0407/GADI-email_filter.git
   cd GADI-email_filter
   ```
2. Install dependencies*
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application*
   ```sh
   python gadi_email_filter.py
   ```

## Usage

1. Upload Database – Load your existing email files (CSV/Excel).
2. Select Collected Emails – Choose the newly collected emails file.
3. Start Filtering – The tool will remove duplicate and invalid emails.
4. View Results – Check the updated file, removed emails log, and summary report.

## License

This project is licensed under the MIT License – you are free to modify and distribute it.

## Contributing

Feel free to submit pull requests for improvements!


