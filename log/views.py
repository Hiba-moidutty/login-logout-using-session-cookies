
from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
# Create your views here.

username = "hiba"
password = 1234

@never_cache
def user_login(request):
  if 'username' in request.session:
    if 'username' in request.COOKIES:
      if request.session['username']==request.COOKIES['username']:
        return redirect(home)

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    if username==username and password==password :
      response=redirect('home/')
      request.session['username'] = username
      response.set_cookie('username',username)
      return response
    else:
      print('invalid credentials')
      return redirect(user_login)
  return render(request,'homelog.html')


@never_cache
def home(request):
  if 'username' in request.session and 'username' in request.COOKIES:
    return render(request,'resultlog.html')
  return redirect(user_login)
 

def user_logout(request):
  response= redirect('user_login')
  del request.session
  response.delete_cookie('username')
  return response