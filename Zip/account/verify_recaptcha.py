import requests
from django.conf import settings


def verify_rectcha(request):
    ''' reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': settings.GOOGLE_RECAPCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    r = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data=data)
    result = r.json()

    return result