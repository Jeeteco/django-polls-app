from polls.models import Choice, Question
from polls.serializers import ChoiceSerializer, QuestionSerializer
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination  import PageNumberPagination

class QuestionPagnation( PageNumberPagination):
    page_size=5


class Questionlist(generics.ListCreateAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    pagination_class=QuestionPagnation
    
    
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset=Choice.objects.all()
    serializer_class=ChoiceSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
  
    