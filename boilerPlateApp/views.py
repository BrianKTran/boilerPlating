from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from . models import basic
from . serializers import basicSerializer
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from rest_framework import status
from django.shortcuts import render
import requests
import os
import json

# Create your views here.
class index(APIView):
    def get(self, request):
        return render(request, 'index.html')


# View for GET requesting all data available in database
class basicGet(APIView):
    def get(self, request):
        # get all objects from model
        basic1 = basic.objects.all()
        # pass objects to serializer to convert to json data
        serializer = basicSerializer(basic1, many=True)
        # set converted json to retData variable
        retData = serializer.data
        # pass variable to return a response
        return Response(retData)

class basicPost(APIView):
    def post(self, request):
        serializer = basicSerializer(data=request.data)
        # save to local database to be viewed on index.html
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)