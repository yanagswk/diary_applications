from django.urls import path
from . import views


app_name = 'journal'

urlpatterns = [
    path('', views.JournalListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/', views.JournalDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.JournalCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>/', views.JournalUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/', views.JournalDeleteView.as_view(), name="diary_delete"),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/', views.CategoryJournalView.as_view(), name='category_journal'),
    path('tag/<str:tag_slug>/', views.TagJournalView.as_view(), name='tag_journal'),
    path('search/', views.SearchJournalView.as_view(), name='search_journal'),

]




