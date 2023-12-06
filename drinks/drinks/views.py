from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Get all drinks
@api_view(['GET', 'POST'])
def drink_list(req, format=None):
    drinks = Drink.objects.all()
    if req.method == "GET":
        serializer = DrinkSerializer(drinks, many=True)
        # return JsonResponse(serializer.data, safe=False)
        # return JsonResponse({ 'drinks' : serializer.data})
        return Response({'drinks': serializer.data})
    
    if req.method == "POST":
        serializer = DrinkSerializer(data = req.data)     
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(req, id, format=None):
    try: 
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if req.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif req.method == "PUT":
        serializer = DrinkSerializer(drink, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif req.method == "DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    