from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProfileSerializers
from .models import Profile
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class ListProfileApiView(APIView):
    def get(self,request):
        prof=Profile.objects.all()
        serilaizers=ProfileSerializers(prof,many=True)
        messages={
                "response_code":"1",
                "response":"listes successfully",
                "data":serilaizers.data
            }
        return Response(messages,status=status.HTTP_200_OK)
    def post(self,request):
        serializers=ProfileSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            messages= {
                "response_code":"1",
                "response":"data created succesfully",
                "data":serializers.data
            }
            return Response(messages,status=status.HTTP_201_CREATED)
        messages = {
            "response_Code":"0",
            "response":"sorry not found",
            "error":serializers.errors
        }
        return Response(messages,status=status.HTTP_404_NOT_FOUND)
    