from django.views import View
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from .models import Data, FileData
from rest_framework.response import Response
from .serializers import DataSerializer, FileDataSerializer
import requests


class UploadData(View):
    def get(self,request, pk):
        data_entries = Data.objects.get(pk=pk)
        file_entries = FileData.objects.filter(data=pk)
        post_json = DataSerializer(data_entries).data
        post_json['patient_documents'] = []
        files = {'files': [] }
        for entry in file_entries.values():
            post_json['patient_documents'].append(entry['patient_document'])
            file_object = FileData.objects.get(file= entry['file'])
            files['files'].append(file_object.file.name)
        
        #print(files,post_json)
        url = 'http://dev.letsmd.com/partners/mobile'
        r = requests.post(url, files=files, data=post_json)

        return HttpResponse(r)
