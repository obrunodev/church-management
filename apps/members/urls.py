from django.urls import path
from apps.members import views

app_name = 'members'
urlpatterns = [
    path('create/', views.MemberCreateView.as_view(), name='create'),
    path('', views.MemberListView.as_view(), name='list'),
    path('<int:pk>/update/', views.MemberUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.MemberDeleteView.as_view(), name='delete'),
]
