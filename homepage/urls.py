from django.urls import path

from .views import HomeListView

app_name = 'homepage'

urlpatterns = [
	path('home', HomeListView.as_view(), name = 'list'),
]