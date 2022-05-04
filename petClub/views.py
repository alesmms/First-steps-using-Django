from django.shortcuts import render

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView

class Crud(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Soy el GET", status=200) # respuesta del servicio
    def post(self, request):
        return Response(data="Soy el POST", status=200)
    def patch(self, request):
        return Response(data="Soy el PATCH", status=200)
    def delete(self, request):
        return Response(data="Soy el DELETE", status=200)