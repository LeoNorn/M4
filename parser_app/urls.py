from django.urls import path
from . import views

urlpatterns = [
    path('lalafo_list_parser/', views.ParserFaberlicListView.as_view()),
    path('start_parsing/', views.ParserFormView.as_view()),
]