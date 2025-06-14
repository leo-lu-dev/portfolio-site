from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("notes", views.NoteListCreate)

urlpatterns = router.urls