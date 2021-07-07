from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    MessageActionViewSet,
    ThreadMemberViewSet,
    ThreadViewSet,
    MessageViewSet,
    ThreadActionViewSet,
    ForwardedMessageViewSet,
)

router = DefaultRouter()
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("threadaction", ThreadActionViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("thread", ThreadViewSet)
router.register("message", MessageViewSet)
router.register("threadmember", ThreadMemberViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
