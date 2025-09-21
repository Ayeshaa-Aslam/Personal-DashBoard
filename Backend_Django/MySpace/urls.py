from django.urls import path
from .views import profile_view
from .views import note_view
from .views import weather_view
from .views import quote_view


urlpatterns = [
     path("profile/", profile_view),
     path("note/", note_view),
     path("weather/", weather_view),
     path("quote/", quote_view),
]
