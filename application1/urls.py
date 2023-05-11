from django.urls import path
from . import views


urlpatterns = [
    path('report',views.index,name="index"),
    path('physician',views.index1,name="index1"),
    path('Surgery',views.index2,name="index2"),   
   # path('Transaction',views.index3,name="index3"),
    #path('view',views.index4,name="index4"),
  
]