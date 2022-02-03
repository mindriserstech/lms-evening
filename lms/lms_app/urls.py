from django.urls import path
from . import views

urlpatterns = [
    # usertype
    # urls for user-type
    path('usertype/', views.usertype_index, name="users.type.index"),  # index is always treated as root directory
    path('usertype/create/', views.usertype_create, name="users.type.create"),
    path('usertype/edit/<int:usertype_id>', views.usertype_edit, name="users.type.edit"),
    path('usertype/show/<int:usertype_id>', views.usertype_show, name="users.type.show"),
    path('usertype/delete/<int:usertype_id>', views.usertype_delete, name="users.type.delete"),
    path('usertype/update/', views.usertype_update, name="users.type.update"),


    # user
    path('users/', views.user_index, name="user.index"),
    path('users/create/', views.user_create, name="users.create"),
    path('users/store/', views.user_store, name="users.store"),
    path('users/login/', views.user_login, name="users.login"),
    path('users/logout/', views.user_logout, name="users.logout")
]