from django.urls import path
from designer.views import *

urlpatterns = [
    path('', home, name="home"),
    path('designer/', designer, name="designer"),
    path('contacts/', contacts, name="contact"),
    path('psixolog/', psixolog, name="psixolog"),
]