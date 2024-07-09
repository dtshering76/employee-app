from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.registerView,name="register"),
    path('user-login/',views.loginView,name="user-login"),
    path('user-logout/',views.logoutView,name="user-logout"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('add-record/',views.createView,name="add-record"),
    path('update-record/<int:pk>/',views.updateRecordView,name="update-record"),
    path('detail-record/<int:pk>/',views.detailsRecordView,name="detail-record"),
    path('delete-record/<int:pk>/',views.delete_record,name="delete-record"),
    
]
