
from django.contrib import admin
from django.urls import path
from careerapp.views import home, result, prediction

urlpatterns = [
    path('', home, name='home'),
    path('prediction/', prediction, name='prediction'),
    path('result/', result, name='result'),
    path('admin/', admin.site.urls),
]
