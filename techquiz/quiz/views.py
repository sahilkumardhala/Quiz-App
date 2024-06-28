from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# import requests
from .models import *
import random
# from django.contrib.auth.decorators import login_required
# Create your views here.

# GEMINI_API_URL = 'https://gemini-api.example.com/questions?search=<search_term>'

def home(request):
    context = {'Categories':Category.objects.all()}
    
    if request.GET.get('category'):
        return redirect(f'/quiz/?category={request.GET.get("category")}')

    return render(request, 'home.html',context)
    # return HttpResponse("Hello Django")



def quiz(request):
   
    return render(request, 'quiz.html')

# {
#     "status":True
#     "data":[
#         {},
#     ]
# }

def get_quiz(request):
    try:
        questions_objs = Question.objects.all()
        if request.GET.get('category'):
            questions_objs = Question.objects.filter(category__category_name__icontains=request.GET.get('category'))
        
        questions_objs =list(questions_objs)
        data = []
        random.shuffle(questions_objs)
        for question_obj in questions_objs:
            data.append({
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                'mark' : question_obj.marks,
                'answer':question_obj.get_answers()
            })


        payload = {"status":True, "data": data}
        return JsonResponse(payload)



    except Exception as e:
        print(e)
    return HttpResponse("something went wrong")