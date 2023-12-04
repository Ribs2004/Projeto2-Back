from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SearchResult, Anuncio
from .serializers import SearchResultSerializer, AnunciosSerializer
# from rest_framework.views import APIView
# from django.core.serializers import json

# class SearchResultView(APIView):
#     def get(self, request):
#         results = SearchResult.objects.all()
#         print(results)
#         json_serializer = json.Serializer()
#         json_serialized = json_serializer.serialize(results)
#         return Response(json_serialized)

class anuncios_view(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer

@api_view(['GET', 'POST'])
def search_results(request):
    results = SearchResult.objects.all().order_by('-id')[:5]
    serialized_result = SearchResultSerializer(results, many=True)
    
    if request.method == 'POST':
        print('Received POST')
        data = request.data
        name = data.get('name')
        print(name)
        gender = data.get('gender')
        print(gender)
        probability = data.get('probability')
        print(probability)

        result = SearchResult(name=name, gender=gender, probability=probability)
        result.save()
        return Response(status=201)

    elif request.method == 'GET':
        print(serialized_result.data)
        return Response(serialized_result.data)
        
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
def anuncios(request):
    results = Anuncio.objects.all()  #.order_by('-id')[:3]
    serialized_result = AnunciosSerializer(results, many=True)
    
    if request.method == 'POST':
        data = request.data
        headline = data.get('headline')
        img = data.get('img')
        link = data.get('link')

        result = Anuncio(headline=headline, img=img, link=link)
        result.save()
        return Response(status=201)

    elif request.method == 'GET':
        return Response(serialized_result.data)
        
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

