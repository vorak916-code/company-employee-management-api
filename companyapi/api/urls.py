from django.urls import path,include
from api.views import CompnyViewSet,EmployeeViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompnyViewSet)
router.register(r'employee',EmployeeViewset)

urlpatterns = [
    path('',include(router.urls))
]