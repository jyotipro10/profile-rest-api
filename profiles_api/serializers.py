from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes names for a post method"""

    name = serializers.CharField(max_length = 10)
