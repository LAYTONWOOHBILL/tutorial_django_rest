from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


# Create your views here.


# you are basically telling the view that it doesn't need the token. 
# This is a security exemption that you should take seriously.
# @csrf_exempt
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer