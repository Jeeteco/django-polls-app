from polls.models import Choice, Question
from rest_framework import serializers

      
class QuestionSerializer(serializers.ModelSerializer):
   owner=serializers.ReadOnlyField(source='owner.username')
   
   class Meta:
         model=Question
         fields=['id','question_text','pub_date','owner']



class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    question_choice= serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),source='question',write_only=True
    )
    
    class Meta:
         model=Choice
         fields=['id','choice_text','votes', 'question', 'question_choice']    

         
class QuestionSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    # choices=ChoiceSerializer(many=True,read_only=True,source='choice_set')
    class Meta:
         model=Question
         fields=['id','question_text','pub_date','owner']
         
         
    def validate_question_text(self,value):
        if 'spam' in value.lower():
            raise serializers.ValidationError("No spams are allowed in question text !")
        return value 

   