from django.urls import path
from . import views


app_name = 'journal'

urlpatterns = [
    path('', views.JournalListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/', views.JournalDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.JournalCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>/', views.JournalUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/', views.JournalDeleteView.as_view(), name="diary_delete"),
]


