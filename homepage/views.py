from django.shortcuts import render
from django.views.generic import TemplateView



class HomeListView(TemplateView):
	template_name = 'homepage/list_view.html'
