from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Customer
from api.serializers import CustomerSerializer
from rest_framework.generics import CreateAPIView, ListAPIView




class GetCustomers(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




@csrf_exempt
def CustomerList(request):
    """
    List all customers, or create a new customer.
    """    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer,many=True)
        return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def CustomerDetails(request,pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=204)
