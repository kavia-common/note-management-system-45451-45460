from django.urls import path
from .views import (
    health,
    NoteListCreateView,
    NoteRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Health endpoint at /api/health/
    path("health/", health, name="Health"),
    # Notes CRUD
    path("notes/", NoteListCreateView.as_view(), name="note-list-create"),
    path("notes/<int:pk>/", NoteRetrieveUpdateDestroyView.as_view(), name="note-detail"),
]
