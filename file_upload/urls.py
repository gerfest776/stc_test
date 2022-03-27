from rest_framework.routers import DefaultRouter

from file_upload import views

router = DefaultRouter(trailing_slash=False)
router.register("file", views.FileViewSet)

urlpatterns = []
urlpatterns += router.urls
