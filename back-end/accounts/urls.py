from django.urls import path
from accounts.views import *

urlpatterns = [
    path("user/get/", get_users, name='get-all-users'),
    # path("user/get/<str:name>/", views.get_suppliers_name),
    path("user/post/", create_user),
]