from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .utils import extract_data 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def index(request):
    return render(request, 'index.html')

# @method_decorator(csrf_exempt, name='dispatch')
class WeatherSummaryAPIView(APIView):
    def post(self, request):
        url = request.data.get('dataset_url')
        if not url:
            return Response({'error': 'No URL provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            result = extract_data(url)  # list of dicts or model objects
            serializer = WeatherDataSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WeatherListAPIView(APIView):
    def get(self, request):
        data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(data, many=True)
        return Response(serializer.data)
