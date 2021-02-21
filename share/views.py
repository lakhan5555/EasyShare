from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

from django.contrib.auth import authenticate
from .forms import CreateUserForm



def Home(request):
    all_posts = Post.objects.all().order_by('-id')
    context = {'posts': all_posts}
    return render(request, 'main/home.html', context)


# Create Upload File System

def Upload(request,user_name):
    if request.method == 'POST':
        filename = request.FILES['filename']
        title = request.POST['title']
        desc = request.POST['desc']

        user_obj = Person.objects.get(username=user_name)
        upload_post = Post(user=user_obj, title=title, file_field=filename, desc=desc)
        upload_post.save()
        messages.success(request, 'Your Post has been uploaded successfully.')
        return redirect(f'/profile/{user_name}')

    return render(request, 'main/upload_file.html')    




# View User Profile

def Profile(request, user_name):
    user_obj = Person.objects.get(username=user_name)
    user_posts = user_obj.post_set.all().order_by('-id')
    context = {'user_data':user_obj, 'user_posts': user_posts}
    return render(request, 'main/profile.html', context)



# Post Delete View

def DeletePost(request, post_id):
    model = Post
    user = request.session['user']
    delete_post = model.objects.get(id=post_id)
    delete_post.delete()
    messages.success(request, 'Your post has been deleted successfully.')
    return redirect(f'/profile/{user}')



# Search View

def Search(request):
    query = request.GET['query']
    search_users = Person.objects.filter(username__icontains=query)
    search_title = Post.objects.filter(title__icontains = query)
    search_desc = Post.objects.filter(desc__icontains = query)
    search_result = search_title.union(search_desc)
    context = {'query':query, 'search_result':search_result, 'search_users':search_users}
    return render(request, 'main/search.html', context)

     
# Sign Up

def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            Person.objects.create(
                user = user,
                username = user.username,
                email = user.email
            )

            messages.success(request, "Account was created for " + username)
            form = CreateUserForm()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)        



# Login System

def LoginUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            request.session['user'] = username
            # login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is Invalid")   
    context = {}
    return render(request, 'main/login.html', context)



# Logout

def LogoutUser(request):
    try:
        del request.session['user']
    except:
        return redirect('home')    
    return redirect('home')

