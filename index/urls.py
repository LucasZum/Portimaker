from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('create/<str:model_id>', views.create_portifolio_page, name='create_page'),
    path('create/<str:model_id>/post', views.create_portifolio, name='create'),
    path('meus_portifolios', views.meus_portifolios, name='meus_portifolios'),
    path('publish/<str:model_id>/<int:id>', views.publish, name='publish'),
    path('unpublish/<str:model_id>/<int:id>', views.unpublish, name='unpublish'),
    path('portifolio/<str:username>', views.my_portifolio, name='my_portifolio'),
    path('inicio', views.inicio_adm, name='inicio'),
    path('subscribe', views.subscribe, name='subscribe')
]