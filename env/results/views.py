from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SearchResult
from .serializers import SearchResultSerializer
# from rest_framework.views import APIView
# from django.core.serializers import json

# class SearchResultView(APIView):
#     def get(self, request):
#         results = SearchResult.objects.all()
#         print(results)
#         json_serializer = json.Serializer()
#         json_serialized = json_serializer.serialize(results)
#         return Response(json_serialized)

@api_view(['GET', 'POST'])
def search_results(request):
    results = SearchResult.objects.all().order_by('-id')[:5]
    serialized_result = SearchResultSerializer(results, many=True)

    """if request.method == 'POST':
        print('recebi o POST')
        name = request.POST.get('name')
        print(name)
        gender = request.POST.get('gender')
        print(gender)
        probability = request.POST.get('probability')
        print(probability)"""
    
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

# class SearchResultViewSet(viewsets.ModelViewSet):
#     queryset = SearchResult.objects.all().order_by('-timestamp')
#     serializer_class = SearchResultSerializer

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()[:5]
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
