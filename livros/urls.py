#livros/urls.py
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet

router = DefaultRouter()
router.register('livros', LivroViewSet)

urlpatterns = router.urls
