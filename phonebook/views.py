from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getContacts(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getContact(request, pk):
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateContact(request, pk):
    data = request.data
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(instance=contact, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return Response('Contact Deleted Successfully')

@api_view(['POST'])
def createContact(request):
    data = request.data
    contact = Contact.objects.create(name=data['name'], mobile=data['mobile'])
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)