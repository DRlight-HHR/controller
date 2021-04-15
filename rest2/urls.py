from django.contrib import admin
from django.urls import path
from .main_app import sing_up, log_in, log_out, home_, check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sing_up),
    path('login/', log_in),
    path('long_out/', log_out),
    path('home/', home_),
    path('check/', check),
]
