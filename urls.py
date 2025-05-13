from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import UsuarioViewSet, AlunoViewSet, AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
