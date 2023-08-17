from django.urls import path
from .views import *
from .views import GuitarraDelete, InstrumentoCreacion, CsgoDetalle, BattlefieldLista, LolLista, CsgoLista, RocketLeagueLista, OtroLista, LolDetalle, RocketLeagueDetalle, BattlefieldDetalle, OtroDetalle, CsgoUpdate, LolUpdate, RocketLeagueUpdate, BattlefieldUpdate, OtroUpdate, LolDelete, RocketLeagueDelete, BattlefieldDelete, CsgoDelete, OtroDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaCsgo/', CsgoLista.as_view(), name='csgo'),
    path('listaLol/', LolLista.as_view(), name='lol'),
    path('listaRocketLeague/', RocketLeagueLista.as_view(), name='rocket_league'),
    path('listaBattlefield/', BattlefieldLista.as_view(), name='battlefield'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('csgoDetalle/<int:pk>/', CsgoDetalle.as_view(), name='csgo'),
    path('lolDetalle/<int:pk>/', LolDetalle.as_view(), name='lol'),
    path('rocketleagueDetalle/<int:pk>/', RocketLeagueDetalle.as_view(), name='rocket_lueague'),
    path('battlefieldDetalle/<int:pk>/', BattlefieldDetalle.as_view(), name='battlefield'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('csgoEdicion/<int:pk>/', CsgoUpdate.as_view(), name='csgo_editar'),
    path('lolEdicion/<int:pk>/', LolUpdate.as_view(), name='lol_editar'),
    path('rocketleagueEdicion/<int:pk>/', RocketLeagueUpdate.as_view(), name='rocket_league_editar'),
    path('battlefieldEdicion/<int:pk>/', BattlefieldUpdate.as_view(), name='battlefield_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),

    path('csgoBorrado/<int:pk>/', CsgoDelete.as_view(), name='csgo_eliminar'),
    path('lolBorrado/<int:pk>/', LolDelete.as_view(), name='lol_eliminar'),
    path('rocketleagueBorrado/<int:pk>/', RocketLeagueDelete.as_view(), name='rocket_league_eliminar'),
    path('battlefieldBorrado/<int:pk>/', BattlefieldDelete.as_view(), name='battlefield_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('instrumentoCreacion/', InstrumentoCreacion.as_view(), name='nuevo'),

    path('csgoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('lolDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('rocketleagueDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('battlefieldDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
]