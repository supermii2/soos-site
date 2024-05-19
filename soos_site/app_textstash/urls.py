from django.urls import path
from .views import (
    home_stash,
    create_stash, read_stash, update_stash, delete_stash,
    view_stash
)

urlpatterns = [
    path('', home_stash, name='home_stash'),

    path('create/', create_stash, name='create_stash'),
    path('read/', read_stash, name='read_stash'),
    path('update/', update_stash, name='update_stash'),
    path('delete/', delete_stash, name='delete_stash'),

    path('view/<str:string_id>', view_stash, name='view_stash'),
]
