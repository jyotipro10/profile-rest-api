from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


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

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Simple API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Simple get method like APIView"""

        a_viewset = [
            'Uses actions similar to APIViews',
            'Give more functionality',
            'Automatically maps to URL routers',
        ]

        return Response({'message':'Hello!!! viewset', 'a_viewset':a_viewset})

    def create(self, request, pk=None):
        """Create an object by its id"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Get an object by its id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Update an object by its id"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Partially update an object by its id"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an object by its id"""
        return Response({'http_method':'DELETE'})
