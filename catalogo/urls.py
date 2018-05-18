from django.conf.urls import url, include
from rest_framework import routers
from .views.categoria_view import CategoriaViewSet
from .views.hotel_view import HotelViewSet


from .views.cliente_view import ClienteViewSet

from .views.tipoTrabajador_view import TipoTrabajadorViewSet
from .views.trabajador_view import TrabajadorViewSet
from .views.comprobante_view import ComprobanteViewSet
from .views.reserva_view import ReservaViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'hoteles', HotelViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'tipoTrabajadores', TipoTrabajadorViewSet)
router.register(r'trabajadores', TrabajadorViewSet)
router.register(r'comprobante', ComprobanteViewSet)
router.register(r'reserva', ReservaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
