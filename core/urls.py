from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('apps.dashboard.urls')),
    path('members/', include('apps.members.urls')),
]
