from django.urls import path
from core.views import index, post_detail, page_topic, about, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<str:topico>/', page_topic, name='topico'),
    path('about-me/', about, name='about'),
]