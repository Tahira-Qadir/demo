from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('show_list/', include('personal.urls')),
    path('course_list/', include('courses.urls')),
]
