from django.urls import path
from personal.views import(
    show_list,
    create,
    update,
    delete,
)

urlpatterns = [
    path('', show_list, name='show_list'),
    path('create/', create, name='create'), 
    path('update/<int:user_id>/', update, name='update'),
    path('delete/<int:user_id>/', delete, name='delete'),
]