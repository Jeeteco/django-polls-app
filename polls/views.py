
from django.core.paginator import Paginator
from django.views import View
from polls.forms import ContactForm
from polls.models import Choice, Question # type: ignore
from django.shortcuts import render, get_object_or_404 ,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required #decorater ensure user is  logged in



def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.isvalid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            
            return redirect("polls:thanks")
    else:
        form=ContactForm()
    return render(request,'polls/contact.html' , {'form':form})
            

# def index(request):
#     return HttpResponse("Hello world . you're at the polls index")

#class based approach
# class IndexView(View):
#     def get(self,request):
#         return HttpResponse("Hello ,World .You are in the poools index")

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')
    paginator=Paginator(latest_question_list,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, 'polls/index.html' , {'page_obj':page_obj})
    
# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:]
#     context={'latest_question_list':latest_question_list}
#     return render(request, 'polls/index.html' ,context)

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