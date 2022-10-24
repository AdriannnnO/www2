from .models import Question
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def home_view(request):
   return render(request, 'jd.html', {})

def question_list(request):
   questions = Question.objects.all
   return render(request, 'question_list.html', {'questions': 
questions})

def question_detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   print(question.id)
   return render(request, 'question_detail.html', {'question': question})

def policjant(request):
   return render(request, 'zasilek.html', {})
 
def question_add(request):
   if request.method == 'POST':
      form = QuestionForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse('question_list'))
   else:
      form = QuestionForm()
      return render(request, 'questionform.html', {'form': form})


