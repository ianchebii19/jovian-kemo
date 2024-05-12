

from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name='home'),
     path('about/', views.about , name='about'),
     path('CustomerRegistration/', views.CustomerRegistration.as_view() , name='CustomerRegistration'),
     path('ecoapp/login', auth_views.LoginView.as_view(template_name='ecoapp/login.html', 
     authentication_form=LoginForm), name='login'),
     path('profile/', views.ProfileView.as_view(), name='profile'),
       path('adress/', views.adress, name='adress'),

    path('contact/', views.contact , name='contact'),
    path('Category/<slug:val>/', views.CategoryView.as_view(), name='CategoryView'),
    path('ProductDetail/<int:pk>/', views.ProductDetail.as_view(), name='ProductDetail'),
   path('UpdateView/<str:pk>/', views.UpdateView.as_view(), name='updateview'),
 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)