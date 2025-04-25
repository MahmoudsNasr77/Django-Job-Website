# Django Job Website

A simple Django-based web application for posting and browsing job listings.

## 📌 Features

- User registration and authentication
- Post new job listings
- Apply for jobs
- Admin dashboard for managing jobs
- Responsive design using Bootstrap

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default)
- **Deployment:** Not yet deployed

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MahmoudsNasr77/Django-Job-Website.git
cd Django-Job-Website
```
2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run Migrations
```
bash
python manage.py makemigrations
python manage.py migrate
```
6. Create Superuser (for admin access)
```bash
python manage.py createsuperuser
```
7. Run the Development Server
```bash
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browse
```
