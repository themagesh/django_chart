# converter/urls.py
from django.urls import path
from .views import png_to_dcm

urlpatterns = [
    path('convert/', png_to_dcm, name='png_to_dcm'),
]
