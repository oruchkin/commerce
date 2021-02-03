from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from .forms import CommentForm


from .models import User, Listing, Comment


def index(request):
    listings = Listing.objects.all()

    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing(request, listing_title):
    try:
        L = Listing.objects.get(title=listing_title)
    except:
        raise Http404("no such listing")
    return render(request, "auctions/listing.html",{
        "title": L,
        
    })


def make_comment1(request, listing_title):
    try:
        L = Listing.objects.get(title=listing_title)
    except:
        raise Http404("no such listing")
    
    L.comment_set.create(comment_text=request.POST['text'])
    

def make_comment(request, listing_title):

  if request.method == 'POST':
    cf = CommentForm(request.POST or None)
    if cf.is_valid():
      comment_text = request.POST.get('comment_text')
      comment = Comment.objects.create(listing_id=listing_id, author_name=author_name.user, comment_text=comment_text)
      comment.save()
      return redirect(Comment.get_absolute_url())
    else:
      cf = CommentForm()

    context = {
        'comment_form': cf,
    }
    return render(request, 'socio / post_detail.html', context)
