from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('uslugi', views.uslugi, name='uslugi'),
    path('about', views.about, name='about'),
    path('link', views.ShowLinkView.as_view(), name='link'),
    path('link/<slug>', views.LinkDetailView.as_view(), name='link-detail'),
    path('links/add', views.CreateLinkView.as_view(), name='link-add'),
    path('link/<slug>/update/', views.UpdateLinkView.as_view(), name='link-update'),
    path('link/<slug>/delete/', views.DeleteLinkView.as_view(), name='link-delete'),
    ]
