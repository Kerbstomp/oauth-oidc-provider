from django.urls import path, include
from .views import UserList, GroupList

urlpatterns = [
    path('users/', UserList.as_view(), name='users_list'),
    path('groups/', GroupList.as_view(), name='groups_list'),
]
