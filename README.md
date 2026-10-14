# 🥗 Django Calorie Counter & BMR Tracker

A web-based fitness and nutrition application built with **Django**. This application allows users to calculate their Basal Metabolic Rate (BMR) and daily calorie requirements based on personal attributes, track daily meal intake, and monitor nutritional consumption against their goal weight targets.

---

## 🌟 Features

- **BMR & TDEE Calculation:** Calculates Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE) using user demographics (age, gender, height, weight, and activity level).
- **Daily Calorie Target Setup:** Recommends daily intake goals based on user fitness objectives (weight loss, maintenance, or muscle gain).
- **Meal Logging & Tracking:** Log individual food items and meals throughout the day with nutritional breakdowns (calories, proteins, carbs, fats).
- **Interactive Daily Summary:** Displays total daily calorie consumption versus daily limit with dynamic progress bars.
- **User Profile & History:** Secure user authentication allowing users to save progress over time.
- **Admin Management Panel:** Comprehensive Django Admin interface for managing food databases, categories, and user entries.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript, Tailwind CSS / Bootstrap
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Deployment:** PythonAnywhere / Render / Vercel

---

## 📁 Project Structure

```text
Django--Calory-Counter-/
│
├── core/                   # Main project configuration and settings
├── tracker/                # App handling calorie logs, food models, and calculations
├── accounts/               # App managing user login, signup, and profiles
├── templates/              # HTML frontend templates (dashboard, loggers, forms)
├── static/                 # Static assets (CSS, JavaScript, images)
├── db.sqlite3              # Local SQLite database
├── manage.py               # Django command-line utility
└── requirements.txt        # Python dependencies
