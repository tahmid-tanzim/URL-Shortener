from django.urls import path
from .views import TinyURLViewSet

urlpatterns = [
    path("data/shorten", TinyURLViewSet.as_view({
        "post": "create",
    })),
    path("short-url/<str:code>", TinyURLViewSet.as_view({
        "get": "retrieve"
    })),
]
