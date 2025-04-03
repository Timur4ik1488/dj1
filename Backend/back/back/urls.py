from django.urls import path, include
from rest_framework.routers import DefaultRouter
from prikoly import views

router = DefaultRouter()
router.register('yo', views.yoyoset)

urlpatterns = [
    path('api/', include(router.urls)),
]