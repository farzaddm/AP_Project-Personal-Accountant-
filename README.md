# Personal Finance Manager

## Description
This project is a **Personal Finance Manager** application built using **Python and PyQt6**. The application provides users with an intuitive interface to manage their **income, expenses, categories, reports, and settings**. The project includes user authentication, data validation, and interactive data visualization.

## Features
- **User Authentication**: Sign up, log in, and password recovery.
- **Income and Expense Tracking**: Record financial transactions.
- **Search and Filtering**: Advanced search functionality.
- **Data Visualization**: Generate financial reports with graphical representation.
- **Settings**: Customize user preferences.
- **Database Management**: SQLite integration for data storage.
- **Backup System**: Automatically creates backups of user information as GSON files.
- **Automated Testing**: Includes unit tests using pytest.

## Technologies Used
- **Programming Language**: Python
- **GUI Framework**: PyQt6
- **Database**: SQLite
- **Data Processing**: Pandas
- **Visualization**: Matplotlib
- **Email Handling**: SMTP (for password recovery)
- **Telegram API**: For contact support
- **Testing**: Pytest

## Project Structure
```
📂 PersonalFinanceManager
 ├── 📂 Backups            # Backup files stored as JSON
 │
 ├── 📂 Controlers         # Business logic controllers
 │   ├── transaction_controllet.py
 │   ├── user_controller.py
 │
 ├── 📂 Database           # Database handling
 │   ├── database.db
 │   ├── database.py
 │
 ├── 📂 Models             # Data models
 │   ├── transacation.py
 │   ├── user.py
 │
 ├── 📂 pictures           # UI images
 │
 ├── 📂 tests              # Unit tests
 │   ├── validation_test.py
 │
 ├── 📂 Utils              # Utility functions
 │   ├── .env
 │   ├── contact_us.py
 │   ├── email_sender.py
 │   ├── save.py
 │   ├── show.py
 │   ├── validation.py
 │
 ├── 📂 Views              # UI components
 │   ├── category.py
 │   ├── contactus.py
 │   ├── first_page.py
 │   ├── forget_password.py
 │   ├── login_ui.py
 │   ├── record_cost.py
 │   ├── record_income.py
 │   ├── reporting.py
 │   ├── search.py
 │   ├── setting.py
 │   ├── sign_up.py
 │   ├── start_window.py
 │
 ├── README.md             # Project documentation
 ├── main.py
```

## Installation
### Prerequisites
- Python 3.8+
- Pip package manager

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/farzaddm/AP_Project-Personal-Accountant-.git
   cd AP_Project-Personal-Accountant
   ```

2. **Install dependencies**

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage
1. **Sign Up/Login** to access the dashboard.
2. **Add Income/Expenses** to track financial records.
3. **Search Transactions** with filters for better insights.
4. **View Reports** in graphical form using Matplotlib.
5. **Adjust Settings** like themes and user details.
6. **Export Data** to JSON for backup.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.


