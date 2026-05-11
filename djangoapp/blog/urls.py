from blog.views import index
from django.urls import path, include

app_name = "blog"

urlpatterns = [
    path('', index, name="index"),
]
