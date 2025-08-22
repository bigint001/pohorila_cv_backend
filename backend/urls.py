from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.landing.views import HeaderView, SummaryViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'summary', SummaryViewSet, basename='summary')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/header/', HeaderView.as_view(), name='header-api'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

