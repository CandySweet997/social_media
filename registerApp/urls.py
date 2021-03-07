
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('profileupdate/', views.ProfileUpdateView, name='profileupdate'),
   # path('profileupdate/', views.ProfileUpdateView.as_view(), name='profileupdate'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)