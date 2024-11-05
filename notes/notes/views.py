from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (Player, Game)
from .serializer import *

@api_view(['GET'])
def get_player(request, playerUsername):
    player = Player.objects.filter(username = playerUsername)
    serializer = PlayerSerializer(player, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_players(request):
    player = Player.objects.all()
    serializer = PlayerSerializer(player, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_player(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




