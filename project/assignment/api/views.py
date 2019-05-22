from django.shortcuts import render
from rest_framwork.view import APIView

class UploadData(APIView):
    def post(self,request, pk):

