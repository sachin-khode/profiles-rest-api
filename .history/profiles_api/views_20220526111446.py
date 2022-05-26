from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializers
    def get(self, request, format=None):
        """returns the list of object"""

        an_api_view = ['a','b','c'
        ]
        
        return Response({'message':'hello!','an_apiview':an_api_view})


    def post(self,request):
        "creates our api with a name"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')        
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST 
            )    


class HelloViewSet(viewsets.ViewSet):
    """test api viewsets"""
    def list(self,request):
        a_viewsets = [ 
            'list 1 list 2 list 3'
        ]


        return Response({'message': 'will always be a message','a_viewset': a_viewsets})    