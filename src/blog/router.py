from rest_framework import routers
from .viewsets import BlogViewSet

router = routers.DefaultRouter()

router.register(r'blog', BlogViewSet)