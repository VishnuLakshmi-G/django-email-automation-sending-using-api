# feedback_app/views.py
from django.shortcuts import render
from django.core.mail import send_mail
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def feedback_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')

        # Google Sheets setup
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        # Open your sheet - make sure name matches exactly
        try:
            sheet = client.open("project").sheet1  # <-- check sheet name
        except gspread.SpreadsheetNotFound:
            return render(request, 'feedback.html', {'error': 'Spreadsheet not found. Check name & sharing.'})

        # Append the feedback
        sheet.append_row([email, feedback_text])

        # Send confirmation email
        send_mail(
            'Feedback Received',
            'Thank you for your feedback! We will address it shortly.',
            'your_email@example.com',  # Replace with your email
            [email],
            fail_silently=False,
        )

        return render(request, 'thankyou.html')

    return render(request, 'feedback.html')
