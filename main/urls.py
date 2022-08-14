from unicodedata import name
from django.urls import URLPattern, path,include
from main import views

urlpatterns = [
    
    path('',views.index , name = 'home'), 
    path('contact',views.contact,name='contact'),
    path('download',views.download, name = 'download'),
    
]