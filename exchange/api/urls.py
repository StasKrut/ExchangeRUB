from django.urls import include, path
from rest_framework import routers

from api.views import CurrencyViewSet

router = routers.DefaultRouter()
router.register("rate", CurrencyViewSet, basename="rate")

urlpatterns = [
    path("", include(router.urls)),
]
