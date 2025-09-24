# Django Email Automation Project

![Project Banner](https://img.shields.io/badge/Django-5.2.6-blue) ![Python](https://img.shields.io/badge/Python-3.12.5-green)

A **Django web application** to collect user feedback via a form, save it dynamically to **Google Sheets**, and send confirmation emails automatically. This project demonstrates the integration of Django with Google Sheets API and Gmail SMTP for real-time automation.

---

## 🌟 Features

- User-friendly **feedback form** with email input.
- **Dynamic Google Sheets integration**:
  - Feedback automatically saved to a specified Google Sheet.
  - No manual updates needed — all submissions logged in real-time.
- **Email confirmation**:
  - Sends a thank-you email to the user automatically after submission.
- Fully functional **frontend with modern styling**.
- Responsive design, forms centered and aligned properly.
- Easy to extend for multiple forms or sheets.

---

## 🛠️ How Google Sheets Integration Works

1. **Google Service Account**:
   - Create a service account in Google Cloud Console.
   - Generate `credentials.json` for the service account.
2. **Share your Google Sheet** with the service account email.
3. **Django integration**:
   - The app uses `gspread` and `oauth2client` to connect to Google Sheets.
   - Every form submission appends a new row with email and feedback.
4. **Security**:
   - `credentials.json` is ignored in `.gitignore` to keep secrets safe.

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/VishnuLakshmi-G/django-email-automation-sending-using-api.git
cd django-email-automation-sending-using-api
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add your Google credentials:

Place credentials.json in the project root (ignored in Git for security).

Configure email settings in settings.py:

python
Copy code
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
Run migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Open the app in your browser:

cpp
Copy code
http://127.0.0.1:8000/
Submit a feedback form and watch it update Google Sheets automatically.

📁 Project Structure
Copy code
django-feedback-app/
├─ feedback_project/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ feedback_app/
│  ├─ views.py
│  ├─ urls.py
│  ├─ templates/
│  │  ├─ feedback.html
│  │  └─ thankyou.html
│  └─ forms.py
├─ manage.py
├─ requirements.txt
└─ README.md
💡 Notes
Make sure the Google Sheet title in views.py matches exactly with your Google Sheet.

For Gmail, generate an App Password instead of using your main account password.
