from django.urls import path
from aa_orm import views as aaviews

urlpatterns = [
    path('', aaviews.index, name='aa_orm_home')
]