import os
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# ضع هنا توكن البوت الخاص بك ورقم الأيدي الخاص بك
TOKEN = "8870161341:AAGHfcULIOwa6e5qh5V3iGhjS1zIJqvQgSI"
ADMIN_CHAT_ID = "7819370240"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

# صفحة الويب التي ستظهر للعميل عند فتح الرابط
HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>بوابة المساعدة الفنية</title>
    <style>
        body { font-family: Tahoma, sans-serif; background: #f4f6f9; text-align: center; padding-top: 50px; }
        .card { background: white; max-width: 450px; margin: auto; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h2 { color: #0088cc; }
        p { color: #555; line-height: 1.6; }
        .status { color: #28a745; font-weight: bold; margin-top: 20px; font-size: 16px; }
        .note { font-size: 13px; color: #888; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>الدعم الفني والخدمات الطلابية</h2>
        <p>أنت الآن متصل بنظام المساعدة الفنية عن بُعد.</p>
        <div class="status">● متصل وجاهز لاستقبال التوجيهات</div>
        <div class="note">يرجى إبقاء هذه الصفحة مفتوحة طوال فترة جلسة الدعم.</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # إرسال إشعار لتلجرام فور دخول العميل للرابط لتعلم أن العميل فتح الجلسة
    try:
        client_ip = request.remote_addr
        message = f"🚨 تنبيه: قام عميل بالدخول إلى رابط الدعم الفني!\nعنوان الايبي: {client_ip}"
        requests.get(f"{TELEGRAM_API}/sendMessage", params={"chat_id": ADMIN_CHAT_ID, "text": message})
    except Exception as e:
        print(e)
    
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)