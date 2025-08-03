from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *
from .forms import ConsoleListingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import ChatRoom, Message
from django.db.models import Q, Max
# Create your views here.

def home(request):
    return render(request,'Homeapp/home.html') 
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home')
        else:
            messages.error(request,'wrong user details or user does not exists')
            return redirect('loginpage')
    return render(request,'login/loginpage.html')


def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if len(password)<4:
            messages.error(request,'password too short')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already taken")
            return redirect('register')
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request, 'User created successfully. login now')
        return redirect('loginpage')
    return render(request,'register/register.html')

def logout_view(request):
    logout(request)
    return redirect ('home')

@login_required
def create_listing(request):
    if request.method=='POST':
        form=ConsoleListingForm(request.POST,request.FILES)
        if form.is_valid():
            listing=form.save(commit=False)
            listing.user=request.user
            listing.save()
            return redirect('browse_consoles')
    else:
        form=ConsoleListingForm()
    return render(request,'listing/create_listing.html',{'form':form})
    

def browse_consoles(request):
    consoles = ConsoleListing.objects.all()

    # Search by name
    query = request.GET.get('q')
    if query:
        consoles = consoles.filter(console_name__icontains=query)

    # Filter by games
    game = request.GET.get('game')
    if game:
        consoles = consoles.filter(description__icontains=game)
    return render(request, 'browse/browse_console.html', {'consoles': consoles})

@login_required
def dashboard(request):
    # listings=ConsoleListing.objects.filter(user=request.user)
    listings = ConsoleListing.objects.filter(user=request.user)
    return render(request,'dashboard/dashboard.html',{'listings':listings})

@login_required
def edit_listing(request,pk):
    listing=get_object_or_404(ConsoleListing,pk=pk,user=request.user)
    if request.method=="POST":
        form=ConsoleListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form=ConsoleListingForm(instance=listing)
    return render(request,'edit/edit_listing.html',{'form':form})

@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(ConsoleListing, pk=pk, user=request.user)
    if request.method == 'POST':
        listing.delete()
        return redirect('dashboard')
    return render(request, 'delete/delete_confirm.html', {'listing': listing})


def console_detail(request, pk):
    listing = get_object_or_404(ConsoleListing, pk=pk)
    return render(request, 'listing/console_detail.html', {'listing': listing})


@login_required
def chat_with_user(request, username):
    other_user = get_object_or_404(User, username=username)

    if other_user == request.user:
        return redirect('home')  # Prevent chatting with yourself

    # Get or create chat room between users
    room = ChatRoom.objects.filter(user1=request.user, user2=other_user).first()
    if not room:
        room = ChatRoom.objects.filter(user1=other_user, user2=request.user).first()
    if not room:
        room = ChatRoom.objects.create(user1=request.user, user2=other_user)

    messages = room.messages.all()

    return render(request, 'chat/chat.html', {
        'room': room,
        'messages': messages,
        'other_user': other_user
    })

@login_required
def chat_list(request):
    user = request.user

    # Get all chat rooms involving the user
    rooms = ChatRoom.objects.filter(Q(user1=user) | Q(user2=user))

    chat_rooms = []

    for room in rooms:
        last_message = room.messages.order_by('-timestamp').first()
        if not last_message:
            continue  # skip rooms with no messages

        other_user = room.user2 if room.user1 == user else room.user1

        chat_rooms.append({
            'id': room.id,
            'other_user': other_user,
            'last_message': last_message.content,
        })

    return render(request, 'chat/chat_list.html', {'chat_rooms': chat_rooms})