from django.urls import path
from basdutapp.main.views import index

app_name = 'basdutapp'

urlpatterns = [
    path('', index, name="index")
]

