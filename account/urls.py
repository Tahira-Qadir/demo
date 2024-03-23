from django.urls import path
from account.views import(
    home,
    register_view,
    login_view,
    logout_view,
    user_list,
    create_user,
    update_user,
    delete_user,
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_list/', user_list, name='user_list'),
    path('create_user/', create_user, name='create_user'), 
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]