from django.urls import path
from designer.views import home, designer, contacts

urlpatterns = [
    path('', home, name="home"),
    path('designer/', designer, name="designer"),
    path('contacts/', contacts, name="contact"),
]