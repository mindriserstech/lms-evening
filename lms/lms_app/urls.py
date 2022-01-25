from django.urls import path
from . import views

urlpatterns = [
    # usertype
    # urls for user-type
    path('usertype/', views.usertype_index, name="users.type.index"),  # index is always treated as root directory
    path('usertype/create', views.usertype_create, name="users.type.create"),
    path('usertype/edit/<int:usertype_id>', views.usertype_edit, name="users.type.edit"),
    path('usertype/show/<int:usertype_id>', views.usertype_show, name="users.type.show"),
]