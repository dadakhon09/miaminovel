from django.shortcuts import render
from django.conf import settings


def home(request):
    return render(request, 'home.html', context={
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
    })


def designer(request):
    return render(request, 'partials/designer.html', context={
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
    })


def contacts(request):
    return render(request, 'partials/contact.html', context={
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
    })


def psixolog(request):
    return render(request, 'partials/psixolog.html', context={
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
    })
