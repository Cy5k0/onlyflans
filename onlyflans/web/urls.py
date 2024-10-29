from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

# url conf
urlpatterns = [
    path("", views.indice),
    path("detalle/<uuid:flan_uuid>/", views.detalle_flan, name="detalle_flan"),
    path("acerca/", views.acerca),
    path("bienvenido/", views.bienvenida),
    path("contacto/", views.formulario_contacto),
    path("exito/", views.success),
    path(
        "logout/",
        LogoutView.as_view(next_page="/", template_name="registration/logout.html"),
        name="logout",
    ),
    path("cuenta/", views.gestionar_cuenta, name="gestionar_cuenta"),
]
