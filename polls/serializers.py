from polls.models import Choice, Question
from rest_framework import serializers


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
         model=Choice
         fields=['id','choice_text','votes']    
         
class QuestionSerializer(serializers.ModelSerializer):
    choices=ChoiceSerializer(many=True ,read_only=True ,source='choice-set')
    
    class Meta:
         model=Question
         fields=['id','question_text','pub_date','choices'] 
         
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
         model=Question
         fields=['id','question_text','pub_date']
         
         
    def validate_question_text(self,value):
        if 'spam' in value.lower():
            raise serializers.ValidationError("No spams are allowed in question text !")
        return value 