from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('accessories/', views.accessories, name='accessories'),
	path('catalog/', views.catalog, name='catalog'),
	path('contact/', views.contact, name='contact'),

]