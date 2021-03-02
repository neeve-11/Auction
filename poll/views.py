from django.shortcuts import render,redirect
from django.forms import ModelForm
from django.http import HttpResponse,HttpResponseRedirect
from poll.models import user, bidding, comment, wishlist
from poll.forms import register_form, login_form, makebid_form, bid_form
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


global oprice
oprice = 0
#pdtname = ''

def index(request):
    return render(request, "poll/register.html", { "form" : register_form()})


def register_confirmation(request):
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
           new_form = form.save()
           messages = "Registered Successfully"
           return redirect(reverse('poll:login'))
        else:
           return render(request, "poll/register.html", {"form" : form})
    return render(request, "poll/register.html", {"form" : register_form()})


def login_page(request):
    return render(request, "poll/login.html", {"form" : login_form()} )


def login_confirmation(request):
    if request.method == "POST":
            form = login_form(request.POST)
            email = request.POST["email"]
            password = request.POST['password']
            info = user.objects.all()
            user_info = None
            for e in info:
              if e.email == email:
                user_info = user.objects.get(email=email)
                break
            if user_info is not None:
                    if user_info.password == password:
                        request.session["username"] = email
                        login(request, user_info)
                        return HttpResponseRedirect(reverse("poll:inbox"))
                    else:
                        message = "Invalid password !!"
                        return render(request, "poll/login.html", {"form" : form , "messages" : message })
            else:
                    message = "Invalid user!! Please Register"
                    return render(request, "poll/login.html", {"form" : form , "messages" : message })
    return HttpResponseRedirect(reverse("poll:login"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("poll:home"))

#@login_required
def inbox(request):
    if "username" not in request.session:
        return render(request, "poll/login.html", {"form" : login_form()})
    user_email = request.session["username"]
    user_info = user.objects.get(email=user_email)
    print(user_info)
    return render(request, "poll/inbox.html",{"user" : user_info})

#@login_required
def create_bid(request):
    return render(request, "poll/create_bid.html", {"form" : makebid_form()})

def bid_form(request):
    if request.method == "POST":
        form = makebid_form(request.POST, request.FILES)
        if form.is_valid :
            if "username" not in request.session:
                 return render(request, "poll/login.html", { "form" : login_form()})
            user_email = request.session["username"]
            user_info = user.objects.get(email=user_email)
            price = int(request.POST['price'])
            if price < 0 :
                return render(request, "poll/create_bid.html", {"form" : form, "message" : "Invalid price!!!"})
            b = bidding(user=user_info, name=request.POST['name'], price=price,
                  picture=request.FILES['picture'],description=request.POST['description'], catergory=request.POST['catergory'])
            b.save()
            return HttpResponseRedirect(reverse("poll:mybid"))
    return HttpResponseRedirect(reverse("poll:createbid"))
#@login_required
def user_bid(request):
    if "username" not in request.session:
         return render(request, "poll/login.html", {"form" : login_form()})
    user_email = request.session["username"]
    user_info = user.objects.get(email=user_email)
    bids = bidding.objects.filter(user__email=user_email)

    return render(request, "poll/yourbid.html",{"bids" : bids})

#@login_required
def comment_bid(request):
  #pp=''
  if request.method == 'GET':
    user_pdt = request.GET['user']
    pdtname = request.GET['pdt_name']
    #pp = pdtname
    user_email = request.session["username"]
    user_info = user.objects.get(email=user_email)
    print(user_info.username)
    item = bidding.objects.filter(user__username=user_pdt, name=pdtname)
    for it in item:
        g=it
    comments = comment.objects.filter(item=g)
    return render(request, "poll/comment.html", { "item" : g, "comments" : comments, "puser" : user_info.username})
  if request.method == 'POST':
      user_comment = request.POST['c_comment']
      pdt = request.POST['pdt']
      item_creator = request.POST['itemc']
      user_email = request.session["username"]
      user_info = user.objects.get(email=user_email)
      print(user_info.username)
      item = bidding.objects.filter(user__username=item_creator, name=pdt)
      for it in item:
          g=it
      b = comment(user=user_info, item=g, c_comment=user_comment)
      b.save()
      comments = comment.objects.filter(item=g)
      return render(request, "poll/comment.html", {"item" : g, "comments" : comments, "puser" : user_info.username })
#@login_required
def price_bid(request):
    if request.method == 'GET':
        user = request.GET['user']
        pdtname = request.GET['pdt_name']
        item = bidding.objects.filter(user__username=user, name=pdtname).values_list('price', flat=True)
        # oprice =item
        global oprice
        for i in item:
           oprice = i
        return HttpResponseRedirect(reverse("poll:result"))

#@login_required
def result_bid(request):
    if request.method == 'POST':
         bprice = int(request.POST['price'])
         if bprice > oprice :
           return render(request, "poll/result.html", {"messages" : "YOU WON!!!"})
         else:
           return render(request, "poll/result.html", {"messages" : "YOU LOST!!!!"})
    return render(request, "poll/bid.html")

#@login_required
def listingl(request):
    items = bidding.objects.all()
    return render(request, "poll/listingl.html" ,{"items" : items})


def listing(request):
    items = bidding.objects.all()
    return render(request, "poll/listing.html" ,{"items" : items})

def about(request):
    return render(request, "poll/about.html")
