from django.urls import path
from polls import views
from polls.myviews import main

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', main.index, name='main-index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]