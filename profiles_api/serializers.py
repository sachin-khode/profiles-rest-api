from unittest.util import _MAX_LENGTH
from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """serializers are a name field for test our APIS"""
    name = serializers.CharField(max_length = 10)
 