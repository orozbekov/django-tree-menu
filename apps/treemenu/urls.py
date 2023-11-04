from django.urls import path
from apps.treemenu.views import MenuView

urlpatterns = [
    path('', MenuView.as_view(), name='menu-view'),
    path('<slug:slug>', MenuView.as_view(), name='Menu'),
]