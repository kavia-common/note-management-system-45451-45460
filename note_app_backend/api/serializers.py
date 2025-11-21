from rest_framework import serializers
from .models import Note

# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """Serializer for Note model to handle validation and representation."""

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value: str) -> str:
        """Ensure title is non-empty and trimmed."""
        if value is None:
            raise serializers.ValidationError("Title is required.")
        trimmed = value.strip()
        if not trimmed:
            raise serializers.ValidationError("Title cannot be empty.")
        return trimmed
