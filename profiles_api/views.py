from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """docstring for HelloApiView."""

    def get(self, request, format=None):
        """ returns a list of APIVIEWS feature"""
        an_apiview = [
        'Uses HTTP methods as function (get, post ,patch, put, delete)',
        'Is simiar to traditional DJango View',
        'Gives you trhe most control over your app logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
