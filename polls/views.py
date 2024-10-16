

from django.http import HttpResponse ,HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse


from polls.models import Choice, Question # type: ignore

# def index(request):
#     return HttpResponse("Hello world . you're at the polls index")

#class based approach
# class IndexView(View):
#     def get(self,request):
#         return HttpResponse("Hello ,World .You are in the poools index")
    
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html' ,context)

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})


def result(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/result.html',{'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Increment the vote count and save
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to the results page after successful vote
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))