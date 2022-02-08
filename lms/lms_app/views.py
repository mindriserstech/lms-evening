from django.shortcuts import redirect, render
from django.http import request
from lms_app.models import UserProfile
from lms_app.form import UserProfileForm
from django.core.files.storage import FileSystemStorage

# importing form
from lms_app.form import UserTypeForm
from lms_app.form import UserRegisterForm
from lms_app.form import UserLoginForm

# importing model
from lms_app.models import UserType
from lms_app.models import User
# Create your views here.

# display all usertypes
def usertype_index(request):

    # we can use any one of the below shown method to retrieve data from db
    # method one - direct Model Object creation and data retrieval
    context = UserType.objects.all()

    # method two - 1. object creation 2. data retrieval from object;
    ut = UserType
    data = ut.objects.all() 
    # equivalent to  SELECT * FROM lms_usertype

    # retrieving single item by id
    obj2 = UserType.objects.get(id=2)
    # equivalent to SELECT * FROM lms_usertype WHERE id = 2;
    return render(request, 'usertype/index.html', {'data': context, 'single_data': obj2})

# stores data of UserType model
def usertype_create(request):
    if request.method == "POST":
        # saving form request data in variable
        usertype = request.POST.get('user_type')

        # creating Model object - here model is UserType
        ut = UserType(user_type=usertype)
        ut.save() 

        # after object is saved into database
        # we create template and return data to template
        template = 'usertype/index.html'
        
        context = UserType.objects.all()
        # preparing response data with dictionary
        data = {'usertype': context, 'msg': 'Stored successfully'}

        # redirecting the page by rendering it
        return render(request, template, data)
    else:
        template = 'usertype/create.html'
        user_type = UserTypeForm
        return render(request, template, {'form': user_type, 'msg': "Something went wrong"})

def usertype_edit(request, usertype_id):
    data = UserType.objects.get(id=usertype_id)
    return render(request, 'usertype/edit.html', {'data':data})

def usertype_show(request, usertype_id):
    data = UserType.objects.get(id=usertype_id)
    return render(request, 'usertype/show.html', {'data': data})

def usertype_delete(request, usertype_id):
    ut = UserType.objects.get(id=usertype_id)
    ut.delete()
    msg = "Deleted Successfully"
    context = UserType.objects.all()
    return render(request, 'usertype/index.html', {'data': context, 'msg':msg })

def usertype_update(request):
    if request.method == "POST":
        ut = UserType.objects.get(id=request.POST.get('id'))
        ut.user_type = request.POST.get('user_type')
        ut.save()
        msg = "Updated Successfully"
        context = UserType.objects.all()
        return render(request, 'usertype/index.html', {'data': context, 'msg': msg})
    else:
        context = UserType.objects.all()
        msg = "Error while updating"
        return render(request, 'usertype/index.html', {'data': context, 'msg': msg})

# User

# returns the registration form
def user_create(request):
    user_form = UserRegisterForm
    return render(request, 'users/register.html', {'form':user_form})

# store or create new users
def user_store(request):
    if request.method == "POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        user = User(first_name=fname, last_name=lname, \
            email=email, contact=contact, password=password)
        user.save()
        request.session['email'] = user.email
        if request.session.has_key('email'):
            uname = request.session['email']
            return render(request, 'users/index.html', {'email': uname})
    else:
        user_form = UserRegisterForm
        return render(request, 'users/register.html', {'form':user_form})
def user_index(request):
    # checking session stored or not
    if request.session.has_key('email'):
        uname = request.session['email']
        return render(request, 'users/index.html', {'email': uname})
    else:
        ul = UserLoginForm
        return render(request, 'users/login.html', {'form': ul, \
                'msg': "Please login to access"})
def user_login(request):
    ul = UserLoginForm
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if user.password == password:
            # storing session
            request.session['email'] = user.email
            return render(request, 'users/index.html', {'email': email})
        else:
            return render(request, 'users/login', {'form': ul, 'msg': "Please login to access"})
    else:
        return render(request, 'users/login.html', {'form': ul, 'msg': "Please login to access"})

# user profile document upload
def user_document(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'users/index.html')
    else:
        form = UserProfileForm
        return render(request, 'users/document.html', {'form': form})

def user_logout(request):
    if request.session.has_key('email'):
        # destroying/deleting session to logout
        del request.session['email']
        ul = UserLoginForm
        return render(request, 'users/login.html', {'form':ul})
    else:
        ul = UserLoginForm
        return render(request, 'users/login.html', {'form':ul})