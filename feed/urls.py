from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='feed-index'),
    path('land/new/', views.create_land.as_view(), name='create-land'),
    path('land/search/', views.search, name='search-land'),
    path('land/user/v/', views.user_land_verified, name='user-land-verified'),
    path('land/user/uv/', views.user_land_unverified, name='user-land-unverified'),
    path('land/<int:pk>/', views.detail_land.as_view(), name='detail-land'),
    path('land/<int:pk>/update/', views.update_land.as_view(), name='update-land'),
    path('land/<int:pk>/delete/', views.delete_land.as_view(), name='delete-land'),
    path('feed/explore/', views.explore, name='feed-explore'),
]
