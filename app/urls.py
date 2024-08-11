from django.urls import include, path

# import routers
from rest_framework import routers 
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
router.register('movie', MovieViewSet)
router.register('student', StudentViewSet)
  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
]