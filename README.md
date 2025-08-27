# 💰 Personal Finance Manager

A command-line based **Personal Finance Manager** that helps users **track income, expenses, budgets, and generate financial reports**.  
This project was built as part of my Software Engineering Bootcamp.

---

## 🚀 Features
- **🔐 Secure Login** – Password-protected access.  
- **➕ Add Transactions** – Add income or expense with amount, category, date, and description.  
- **📜 View Transactions** – See a detailed list of all transactions.  
- **📊 Generate Reports & Summaries** – Total income, expenses, balance, and category-wise breakdown.  
- **💡 Budget Management** – Set and monitor monthly budget limits.  
- **🔎 Search & Filter Transactions** – Quickly find transactions by keyword.  
- **📦 Backup & Restore** – Backup your financial data and restore when needed.  

---

## 📂 Project Structure
Personal-Finance-Manager/
│── main.py # Entry point of the program
│── finance/
│ ├── manager.py # Core FinanceManager class
│ ├── transaction.py # Transaction class
│ ├── report.py # Reports & summaries
│ ├── budget.py # Budget management
│ ├── recurring.py # Recurring transactions (future feature)
│ ├── file_handler.py # Data persistence (JSON, backup, restore)
│── data/
│ ├── transactions.json # Stores transactions
│ ├── backup.json # Backup file
│── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Personal-Finance-Manager.git
   cd Personal-Finance-Manager
Run the program:

bash
Copy code
python3 main.py
🖥️ Usage
When you run the app, you’ll be prompted to log in with a password.
Default password: 1234

Main Menu Options:
Add Transaction

View Transactions

Generate Reports & Summaries

Manage Budget

Search & Filter Transactions

Backup & Restore

Exit

🎥 Project Demo
📌 Watch the demo & walkthrough here:
👉 Video Demo Link

📈 Future Improvements
Add a GUI version for better usability.

Implement recurring transactions automation.

Add export to Excel/CSV feature.

Provide data visualization (charts & graphs).

👨‍💻 Author
Ernest Munyoki
📧 Email: ernestmunyoki@gmail.com
🔗 GitHub: ErnestMunyoki