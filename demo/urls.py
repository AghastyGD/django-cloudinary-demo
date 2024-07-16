from django.urls import path
from demo import views

urlpatterns = [
    path('', views.post_list, name="post_list")
]
