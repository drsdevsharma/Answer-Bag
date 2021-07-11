from django.shortcuts import render , redirect
from .models import Create_query,Answer_query # Models for query
from user.models import AddUser # Models for User 

# Create your views here.

qid = 0

def Answer_Query(request): # Answer will be stored here 
    Email = AddUser.objects.get(Email=request.session.get('email')) # Getting logged user's Object
    Qid = request.POST.get('Qid') # Query id 
    Date = request.POST.get('Date')
    Answer = request.POST.get('Answer') # Answer for query
    if Qid and Answer and Date: # Chceking wether these are filled or empty
        Ans_query = { # Answer Object fields
            'Email' : Email,
            'Qid' : Qid,
            'Date' : Date,
            'Answer' : Answer
        }
        answer = Answer_query.objects.create(**Ans_query) # Creating answer object 
        answer.save() # Saving answer object
        return redirect('/') # Redirecting to Home page 
    else: # If empty then redirecting back home page
        error = "Please fill the details ..."
        return redirect('/',{error:error})

def Ask_query(request): # Ask query request will come here 
    if request.method == 'POST': # If request is POST then handle data
        Title = request.POST.get('Title') 
        Date = request.POST.get('Date')
        Query = request.POST.get('Query')
        if Title and Date and Query : # Chceking wether these are filled or empty
            global qid # Declaring Global so that we can access and modify the Qid
            qid = qid + 1
            # Creating User object for Logged user
            Present_user =  AddUser.objects.get(Email=request.session.get('email'))  
            Query_dict = { # Query Object fields
                'Email' : Present_user,
                'user' : Present_user.First_name + ' ' + Present_user.Last_name, # Creating user name 
                'Qid' : qid,
                'Title' : Title,
                'Date' : Date,
                'Query' : Query
            }
            Query_object = Create_query.objects.create(**Query_dict) # Creating Query object
            Query_object.save() # Saving Query object
            return redirect('/') # Redirect to the Home page
        else: # If empty then redirecting back Askquery page
            error = "Please fill the details..."
            return redirect('/answer/askquery/', {error:error})
    else: # If request is GET then sending him Askquery page
        return render(request, 'askquery.html')
