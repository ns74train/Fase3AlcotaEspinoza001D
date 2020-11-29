from django.urls import path 
from copa import views

urlpatterns = [
	path('',views.index,name='index'),
	path('usuario/', views.UsuarioListView.as_view(), name='usuario'),
    path('galeria/', views.galeria, name='galeria'),
    path('detalle/<int:pk>',views.UsuarioDetailView.as_view(), name='Usuario-detail'),
    path('vista/',views.UsuarioListView.as_view(), name='vista'),
    
    path('detalle1/<int:pk>',views.ComentarioDetailView.as_view(), name='Comentario-detail'),
    path('vista1/',views.ComentarioListView.as_view(), name='vistacomentario')


]

urlpatterns +=[
    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete'),

]

urlpatterns +=[
    path('comentario/create/', views.ComentarioCreate.as_view(), name='comentario_create'),
    path('comentario/<int:pk>/update/', views.ComentarioUpdate.as_view(), name='comentario_update'),
    path('comentario/<int:pk>/delete/', views.ComentarioDelete.as_view(), name='comentario_delete'),

]