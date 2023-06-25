from django.urls import path
from sinfonia import views

app_name = 'sinfonia'

urlpatterns = [
    path('', views.SinfoniaListView.as_view(), name='read'),
    path('criar/', views.SinfoniaCreateView.as_view(), name='create'),
    path('editar/', views.SinfoniaCreateView.as_view(), name='update'),
    path('excluir/', views.SinfoniaCreateView.as_view(), name='delete'),
]