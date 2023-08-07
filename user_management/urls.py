from django.urls import path
from .views import delete_user_data, download_user_data, login_view, ProtectedAPI

urlpatterns = [
    path('login/', login_view, name='login'),
    path('protected/', ProtectedAPI.as_view(), name='protected'),
    path('downloaduserdata/', download_user_data, name='downloaduserdata'),
    path('deleteuserdata/', delete_user_data, name='deleteuserdata')
]
