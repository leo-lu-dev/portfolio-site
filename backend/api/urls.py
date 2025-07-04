from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserCreateView,
    GroupListCreateView,
    GroupDetailView,
    ScheduleListCreateView,
    ScheduleDetailView,
    EventListCreateView,
    EventDetailView,
    MembershipListCreateView,
    MembershipUpdateView,
    MembershipDeleteView,
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),

    path('groups/<int:group_id>/members/', MembershipListCreateView.as_view(), name='member-list-create'),
    path('members/<int:pk>/', MembershipUpdateView.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', MembershipDeleteView.as_view(), name='member-delete'),

    path('schedules/', ScheduleListCreateView.as_view(), name='schedule-list-create'),
    path('schedules/<int:pk>/', ScheduleDetailView.as_view(), name='schedule-detail'),

    path('schedules/<int:schedule_id>/events/', EventListCreateView.as_view(), name='event-list-create'),
    path('schedules/<int:schedule_id>/events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
