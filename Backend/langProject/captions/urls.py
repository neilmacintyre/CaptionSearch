from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/word/<str:word>/', views.word_query, name='word query'),
    path('/word/<str:word>/<int:page>', views.word_query, name='word query')
]