from django.urls import path 
from . import views

app_name = 'ToDoModule'
urlpatterns = [
    path('', views.index , name="index"),
    path('store' , views.storeData , name='storeData'),
    path('deleta_all' , views.deleteAll , name="deleteAll"),
    path('deleteSelected' , views.deleteSelected , name="deleteSelected" ),
    path('delete/<int:id>' , views.delete , name='delete'),
    path('update/<int:id>' , views.update , name='update')
]
