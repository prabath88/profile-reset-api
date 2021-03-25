from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of APIView features"""

        an_apiview = [
            'Uses HTTP method as function (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello..!','an_apiview': an_apiview})

    def post(self, request):
        """create a helloi message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hellow {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """handle updating an objet"""
        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})