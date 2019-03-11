from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Branch_Office
from .serializers import *

@api_view(['GET'])
def branch_office_list(request):
    """
    List  products, or create a new product.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        products = Branch_Office.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = Branch_OfficeSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/branch_office/?page=' + str(nextPage), 'prevlink': '/api/branch_office/?page=' + str(previousPage)})
