import joblib
from .models import Email, URL, Report

# Загваруудыг ачаалж байна
email_model = joblib.load('path/to/email_model.pkl')
url_model = joblib.load('path/to/url_model.pkl')

class PhishingDetector:

    @staticmethod
    def analyze_email(email):
        prediction = email_model.predict([email.content])
        return prediction[0]

    @staticmethod
    def analyze_url(url):
        prediction = url_model.predict([url.link])
        return prediction[0]

class SpamAssassin:

    @staticmethod
    def check_spam(content):
        # Спам шалгах код энд байна
        pass
