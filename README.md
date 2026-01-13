# Readme.md

# Assignment – Laravel & Python Selenium Project

This repository contains **two separate parts**:

- **Laravel (PHP) Project** – Web application with login page and calendar integration
- **Python Selenium Script** – Automation script to test the login page

---

## 📁 Project Structure

```
Assingment_Hunt-Digital-Media/
│
├── main-laravel/        # Laravel PHP project
│
├── selenium_python/    # Python Selenium automation
│
└── README.md

```

---

## 🛠 Requirements

### For Laravel (PHP)

- PHP 8.x or higher
- Composer
- XAMPP (Apache & MySQL)

### For Python (Selenium)

- Python 3.10+
- Microsoft Edge or Brave browser
- Internet connection

---

## 🚀 How to Run the Project

---

## 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/b-utkarsh-01/Assingment_Hunt-Digital-Media.git
cd Assingment_Hunt-Digital-Media

```

---

## 🔹 Step 2: Run the Laravel Project

### 2.1 Go to Laravel folder

```bash
cd main-laravel

```

### 2.2 Install dependencies

```bash
composer install

```

### 2.3 Create environment file

```bash
copy .env.example .env

```

### 2.4 Generate application key

```bash
php artisan key:generate

```

### 2.5 Clear cache (recommended)

```bash
php artisan config:clear
php artisan cache:clear
php artisan route:clear

```

### 2.6 Start the application

**Option 1 – Using XAMPP**

- Start **Apache** from XAMPP
- Open in browser:

```
http://localhost/main-laravel/public

```

**Option 2 – Using Artisan**

```bash
php artisan serve

```

Open:

```
http://127.0.0.1:8000

```

---

## 🔹 Step 3: Run the Python Selenium Script

### 3.1 Go to Python folder

```bash
cd ..
cd selenium_python

```

### 3.2 (Optional) Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate

```

### 3.3 Install required packages

```bash
pip install selenium webdriver-manager

```

### 3.4 Run the automation script

```bash
python login_test.py

```

The browser will open, fill the login form with random values, and then close automatically.
