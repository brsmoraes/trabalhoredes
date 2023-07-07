from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json
import os
import pandas as pd
import warnings
from sdv.tabular import GaussianCopula


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

@api_view(['GET', 'POST'])
def modelo(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        model = GaussianCopula.load(BASE_DIR + str('/home/2010-2023.pk'))

        quantidade = request.query_params['quantidade']

        retorno = model.sample(int(quantidade)).to_json()


        return Response(json.loads(retorno))

    """
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
