from django.shortcuts import render , redirect
from django.conf import settings
from answer.models import Create_query,Answer_query
from user.models import AddUser


# Create your views here.
def welcome(request):
    if request.session.get('email'): # Checking whether user is logged in 
        result_set = Create_query.objects.all() # Storing all Query objects
        data = [] # An empty list for final result to be sotred
        for var in result_set: # Taking each object one by one
            inner_data = [] # A list that stores all query related aspect
            dict_data = { # A Query object to displayed on home page
                'Qid' : var.id,
                'Email' : var.Email,
                'User' : var.user,
                'Title' : var.Title,
                'Query' : var.Query,
                'Date' : var.Date,
            }
            inner_data.append(dict_data) # Appending Query object to a Query list 
            answer_result_set = Answer_query.objects.all()  # Storing all Answer objects
            for ans_var in answer_result_set : # Taking each object of Answer one by one 
                # Checking wether this answer is blongs to our Query object of outer loop
                if ans_var.Qid == var.id: 
                    Ans_user = AddUser.objects.get(Email=ans_var.Email) # Retriving the user of answer
                    dict_data_ans = { # Answer object
                        'Email' : ans_var.Email,
                        'Qid' : ans_var.Qid,
                        'user' : Ans_user.First_name + " " + Ans_user.Last_name, # Creating name from first and last name
                        'Answer' : ans_var.Answer
                    }
                    inner_data.append(dict_data_ans) # Appending each answer to outer query list
            data.append(inner_data)    # Appending Query list main list
        return render(request,"home.html",{'data':data}) # sending list to our html page 
    else:
        return redirect('/user/login/') # If not logged in then login first
