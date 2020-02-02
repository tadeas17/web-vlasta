from django.urls import path
from . import views


urlpatterns = [
     path('', views.HomePageView.as_view(), name='home_page_view'),
     path('kontakt/', views.ContactView.as_view(), name='contact_view'),
     path('vyber-galerie/', views.GaleriMainView.as_view(), name='home_galeri_view'),
     path('galerie/', views.GaleriView.as_view(), name='galeri_view'),
     path('galerie/<int:type>', views.GaleriView.as_view(), name='type_geleri_view')

]