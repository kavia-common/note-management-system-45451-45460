from typing import Optional

from django.db.models import Q, QuerySet
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def health(request: Request):
    """Health check endpoint used by monitoring and tests."""
    return Response({"status": "ok"})


class NotesQueryMixin:
    """Common queryset behavior: search via ?q= and default ordering by -updated_at."""

    search_param = "q"

    def get_queryset(self) -> QuerySet[Note]:
        qs: QuerySet[Note] = Note.objects.all().order_by("-updated_at")
        q: Optional[str] = self.request.query_params.get(self.search_param)
        if q:
            qs = qs.filter(Q(title__icontains=q.strip()))
        return qs


# PUBLIC_INTERFACE
class NoteListCreateView(NotesQueryMixin, generics.ListCreateAPIView):
    """List notes with optional search and pagination; create a new note.

    Query params:
    - q: string to search in title (icontains)
    - page: page number (pagination)
    - page_size: items per page (pagination)
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]


# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update (PUT/PATCH), or delete a single note by ID."""
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Note.objects.all().order_by("-updated_at")
