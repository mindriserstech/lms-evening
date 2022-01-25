from django.shortcuts import render
from django.http import request

# importing form
from lms_app.form import UserTypeForm

# importing model
from lms_app.models import UserType
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

        # equivalent to 
        # 1. INSERT INTO lms_usertype VALUES(null, "Normal");
        # 2. INSERT INTO lms_usertype (id, user_type)
        #  VALUES (null, "Super Admin")

        # 3. Multiple item insert at a time
        # INSET INTO lms_usertype (id, user_type)
        # VALUES (null, "Librarian"), (null, "Visitor");
        
        # after object is saved into database
        # we create template and return data to template
        template = 'usertype/index.html'
        
        # preparing response data with dictionary
        data = {'usertype': ut, 'msg': 'Stored successfully'}

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