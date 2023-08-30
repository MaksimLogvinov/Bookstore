from django.urls import path, include

from apps.main.views import HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="home_page"),
    path('user/', include("apps.users.urls"))
]
