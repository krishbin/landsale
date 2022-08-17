from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .base_form import RegistrationForm,CustomUserChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from feed.models import Land

def registerUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Successfully created your account! You can now login.')
            return redirect('users-login')
    else:
        form = RegistrationForm()
    context = {
        "form": form,
        "title": "Register"
            }
    return render(request, 'register.html',context)

@login_required
def userProfile(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST,request.FILES,instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    context = {
        "user_change_form": user_change_form
        }
    return render(request, 'profile.html',context);

@login_required
def wishlist(request):
    land_list = Land.objects.filter(wishlist=request.user)
    context = {
        "lands": land_list
    }
    return render(request, 'wishlist.html',context)

@login_required
def addToWishlist(request,id):
    land = get_object_or_404(Land,id=id)
    if land.wishlist.filter(id=request.user.id).exists():
        land.wishlist.remove(request.user)
    else:
        land.wishlist.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

