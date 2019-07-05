from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


from blog.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('blog/', TemplateView.as_view(template_name='blog/blog.html')),
]
