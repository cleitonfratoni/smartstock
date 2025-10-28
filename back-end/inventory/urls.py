from django.urls import path
from inventory.views import *

urlpatterns = [
    path("supplier/get/", get_suppliers, name='get-all-suppliers'),
    path("supplier/get/<str:name>/", get_suppliers_name),
    path("supplier/post/", create_suppliers),
]