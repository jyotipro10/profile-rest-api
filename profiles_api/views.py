from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView(APIView):
    """Small APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Return a list of responses. Format may be api or json."""

        an_apiview = [
            'This is a get method APIView',
            'It returns a reponse to the user',
            'It outputs json file from list or dictionary',
        ]

        return Response({'message':'Hello APIView!!!','an_apiview':an_apiview})

    def post(self, request):
        """Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello!!! I am {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Update an entire object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Update an object partially"""
        return Response({'method':'PATCH'})

    def delete(self, response, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
