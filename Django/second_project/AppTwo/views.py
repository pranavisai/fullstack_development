from django.shortcuts import render
#from django.http import HttpResponse
#from AppTwo.models import User

from AppTwo.forms import NewUser

# Create your views here.

##def index(request):
  ##  my_dict = {'help_me': "I am coming from help.html in AppTwo",}
    ##return render(request, 'AppTwo/help.html', my_dict)
    
def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', helpdict)

def index(request):
    return render(request, 'AppTwo/users.html')



#def users(request):
    user_list = User.objects.order_by('First_name')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', user_dict)

def users(request):

    form = NewUser()

    if(request.method == "POST"):
        form = NewUser(request.POST) # we pass in the information that is given in the POST request

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('ERROR form invalid')
        
    return render(request, 'AppTwo/users.html', {'form': form})
