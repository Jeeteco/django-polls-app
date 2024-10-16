from polls.models import Question
from polls.serializers import QuestionSerializer
from rest_framework import generics,viewsets



class Questionlist(generics.ListCreateAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    