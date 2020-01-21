from django.urls import path
from swanalpha import views
urlpatterns = [
    path('',views.init,name="Init"),
]
