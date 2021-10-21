from django.urls import path
from houses import views


urlpatterns = [
    path('',views.home, name="home"),
    path('propeties_list',views.propeties_list, name="propeties_list"),
    path('contact',views.contact, name="contact"),
    path('about',views.about, name="about"),
    path('Suburb',views.Suburb_list, name="Suburb"),
    path('propeties_list',views.propeties_list, name="propeties_list"),
    path('property_detail/<int:id>/',views.property_detail, name="property_detail"),
    
]