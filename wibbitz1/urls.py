from django.urls import path
from wibbitz1.views import index, subscribe, contact


app_name = "wibbitz1"
urlpatterns = [
    path('', index, name="index"),
    path('wibbitz1', index, name='wibbitz1'),
    path("subscribe/", subscribe, name="subscribe"),
    path("contact/", contact, name="contact"),
]
