from django.urls import path
from . import views # import views so we can use them in urls.


urlpatterns = [
    path('', views.listing, name='listing'),
    path('search/', views.search, name='search'),
    path('<album_id>/', views.detail, name='detail'),
]