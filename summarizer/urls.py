from django.urls import path
from .views import summarize_view  # <-- вот этой строчки не хватает

urlpatterns = [
    path('', summarize_view, name='upload_video'),
    path('summarize/', summarize_view, name='summarize'),
]