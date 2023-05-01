from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    # path('show/<int:id>/', views.show, name='show'),
    path('show/', views.show, name='show'),
    # path('<int:id>/edit/', views.edit, name='edit'),
    path('edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.destroy, name='delete'),
    path('comment/', views.comment, name='comment'),
]
