from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import requests

# Create your views here.
BASEURL = 'https://jsonplaceholder.typicode.com/albums/'


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_photos_album(request, pk):
    try:
        response = requests.get(BASEURL + pk + '/photos')
        if response:
            data = response.json()
            return Response(data)
    except:
        return Response({"detail": "Something went wrong!"}, status=400)
    return Response([])
