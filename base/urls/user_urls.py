from django.urls import path
from base.views import user_views



urlpatterns = [
    path('', user_views.getUser, name='users'),

    path('login/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', user_views.getUserProflie, name='users-profile'),
    path('profile/update/', user_views.updateUserProfile, name='user-profile-update'),
    path('register/', user_views.registerUser, name='users-register'),


    path('update/<str:pk>/', user_views.updateUser, name='user-update'),
    path('delete/<str:pk>/', user_views.deleteUser, name='user-delete'),
    path('<str:pk>/', user_views.getUserById, name='user'),

]