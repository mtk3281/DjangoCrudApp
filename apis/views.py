from rest_framework import generics, permissions
from webapp.models import record  
from .serializers import *
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model 
from rest_framework import viewsets

# #! list api view can be used to list all the records
# class RecordListAPIView(generics.ListAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = record.objects.all()
#     serializer_class = RecordSerializer                                   #** This is used to serialize the data
#     renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XMLRenderer]  #** This is used to render the response in the specified format (JSON, XML, HTML)


# #! Retrieve api view can be used to list a single records
# class RecordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) 
#     queryset = record.objects.all()
#     serializer_class = RecordSerializer                                  #** This is used to serialize the data
#     renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XMLRenderer] #** This is used to render the response in the specified format (JSON, XML, HTML)


class RecordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = record.objects.all()
    serializer_class = RecordSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XMLRenderer]

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XMLRenderer]