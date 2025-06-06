from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
from .views_auth import RegisterView
from .views import LogoutAndBlacklistRefreshTokenForUser

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),  # only one register path
    path('logout/', LogoutAndBlacklistRefreshTokenForUser.as_view(), name='logout'),  # only one logout path
]
