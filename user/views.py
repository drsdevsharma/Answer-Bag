from django.shortcuts import render , redirect
from .models import AddUser
from random import randint
from django.conf import settings # For email related variables
from django.core.mail import send_mail # for sending email
from django.contrib.auth import hashers # For storing passwords in hash format

User_dict = {}
counters = 3

# Create your views here.
def Signup(request): # For creating new user
    global User_dict # For accessing and updating dictionary
    if request.method == 'POST': # Checking wether req is for geting page or for sending data to backend
        email = request.POST.get('email') # Retrieving email
        try: # If an error raise up
            New_user = AddUser.objects.get(Email=email) # Checking if user already exists exist
        except AddUser.DoesNotExist as e: # Mean not exists
            password = request.POST.get('password') # Retrieving Password
            cpassword = request.POST.get('cpassword') # Retrieving Confirm password
            if cpassword != password: # Checking wether password is matching
                error = "Password not matching !!"
                return render (request, 'signup.html', {'error': error}) # if not then sending back to signup page
            else: # if yes then send otp and storing all info in User_dict dictionary
                otp = str(randint(100000,999999)) # Generating a random number
                from_email = settings.EMAIL_HOST_USER # From email
                to_email = email # Receiver of email
                subject = "Email Verification Required "
                message = "You receive this mail for verification of your email.\n\n Your otp is : " +otp+".\n\n Do not shere it with anyone. "
                send_mail(subject, message, from_email, (to_email,) , auth_password = settings.EMAIL_HOST_PASSWORD )
                User_dict['First_name'] = request.POST.get('firstname') # Retrieving First name And assigning
                User_dict['Last_name'] = request.POST.get('lastname') # Retrieving Last name And assigning
                User_dict['Ph_no'] = request.POST.get('phno') # Retrieving Phone number And assigning
                User_dict['Email'] = email # Assigning Email
                User_dict['Password'] = hashers.make_password(password) # Hashing Password
                request.session['otp'] = otp # saving otp in session
                return render(request, 'verify.html')
        else:
            error = " User already exists .... "
            return render(request, 'signup.html',{'error':error})
    else: # request is for getting signup page 
        return render(request, 'signup.html')

def Forget_password(request): # IF u forget password
    if request.method == 'POST':
        email = request.POST.get('email') # Retrieving email
        try: # Checking if user exists
            New_user = AddUser.objects.get(Email=email)
        except AddUser.DoesNotExist as e: # means not exists that mean email is wrong
            error = "User does not exist ... "
            return render(request,'forget.html',{'error':error})
        else: # User exists and sending mail with otp
            otp = str(randint(100000,999999)) # Generating a rand
            from_email = settings.EMAIL_HOST_USER # From email
            to_email = email # Receiver of email
            subject = "Change Password "
            message = "You are receiving this  mail for change your password.\n\n Your otp is : " +otp+".\n\n Do not shere it with anyone. "
            send_mail(subject, message, from_email, (to_email,) , auth_password = settings.EMAIL_HOST_PASSWORD )
            request.session['otp'] = otp
            request.session['email'] = email  
            return render(request, 'verify.html')
    else:
        return render(request, 'forget.html')

def Verify(request):
    global User_dict
    global counters
    if request.method =='POST':
        votp = request.POST.get('otp') # Retrieving email
        otp = request.session.get('otp') # Retrieving email
        if votp == otp:
            if  not bool(User_dict): # Return false if dict is empty and then inverted
                 # This means request is coming from froget password
                del request.session['otp']
                return render(request, 'newpass.html')
            else: 
                # This means dict have data then this request is coming form signup
                request.session['email'] = User_dict['Email']
                New_user = AddUser.objects.create(**User_dict)
                New_user.save()
                del request.session['otp']
                User_dict.clear()
                return redirect( '/')
        elif counters == 0:
            counters = 3
            error = " Otp not matching ..."
            return render (request, 'signup.html', {'error': error})
        else:
            counters = counter - 1
            error = f" Otp not matching ... {counter} attempts left"
            return render(request, 'verify.html', {'error':error})
    else:
        return render(request, 'verify.html')



def Newpass(request):
    if request.method == 'POST':
        password = request.POST.get('password') # Retrieving email
        cpassword = request.POST.get('cpassword') # Retrieving email
        if cpassword == password:
            new_user = AddUser.objects.get(Email = request.session.get('email'))
            new_user.Password = hashers.make_password(password)
            new_user.save()
            del request.session['email']
            return render(request, 'login.html')
        else:
            error = "Password not matching...."
            return render(request, 'newpass.html', {'error':error})
    else:
        return render(request, 'newpass.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email') # Retrieving email
        try:
            New_user = AddUser.objects.get(Email=email)
        except AddUser.DoesNotExist as e:
            error = "Wrong credentials ...."
            return render(request, 'login.html', {'error':error})
        else:
            password = request.POST.get('password') # Retrieving email
            Verify_Hash_Password = hashers.check_password(password,New_user.Password)
            if Verify_Hash_Password == True:
                request.session['email'] = email
                return redirect('/')
            else:
                error = "Wrong credentials ...."
                return render(request, 'login.html', {'error':error})
    else:
        return render(request, 'login.html')

def Logout(request):
    del request.session['email']
    return render(request, 'login.html')