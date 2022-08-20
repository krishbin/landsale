from django.shortcuts import render
from django import forms
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Comments,Land
from .forms import NewCommentForm
import random

def index(request):
    land_list = Land.objects.filter(verified=True)
    page = request.GET.get('page',1)
    paginate = Paginator(land_list,8)
    try:
        lands = paginate.page(page)
    except PageNotAnInteger:
        lands = paginate.page(1)
    except EmptyPage:
        lands = paginate.page(paginate.num_pages)
    context = {
        "lands": lands
    }
    return render(request, 'feed/feed.html',context)

def search(request):
    land_list = None
    if request.method == 'GET':
        q_l = request.GET.get("q")
        q_a = request.GET.get("qa")
        q_au = request.GET.get("qu")
        q_r = request.GET.get("qr")
        q_b = request.GET.get("qb")
        q_w = request.GET.get("qw")
        q_t = request.GET.get("qt")
        ll = Land.objects.filter(verified=True)
        if(q_l == "" and q_a != ""):
            land_list = ll.filter(
                Q(area__icontains=int(q_a)) & Q(area_unit__icontains=q_au)
                )
            if(q_t == "H"):
                land_list = land_list.filter(is_house_or_apartment=True)
                if(q_r == "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r == "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r == "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r != "" and q_b == "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r))
                        )
                if(q_r == "" and q_b == "" and q_w == ""):
                    land_list = land_list
                if(q_r != "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
        elif(q_a == "" and q_l != ""):
            land_list = ll.filter(
                Q(location__icontains=q_l)
                )

            if(q_t == "H"):
                land_list = land_list.filter(is_house_or_apartment=True)
                if(q_r == "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r == "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r == "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r != "" and q_b == "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r))
                        )
                if(q_r == "" and q_b == "" and q_w == ""):
                    land_list = land_list
                if(q_r != "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
        elif(q_a == "" and q_l == ""):
            land_list = ll

            if(q_t == "H"):
                land_list = land_list.filter(is_house_or_apartment=True)
                if(q_r == "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r == "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r == "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r != "" and q_b == "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r))
                        )
                if(q_r == "" and q_b == "" and q_w == ""):
                    land_list = land_list
                if(q_r != "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
        else:
            land_list = ll.filter(
                Q(location__icontains=q_l) & Q(area__icontains=q_a) & Q(area_unit__icontains=q_au)
                )
            if(q_t == "H"):
                land_list = land_list.filter(is_house_or_apartment=True)
                if(q_r == "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r != "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r == "" and q_b == "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_w))
                        )
                if(q_r == "" and q_b != "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(no_of_bedroom__icontains=int(q_b))
                        )
                if(q_r != "" and q_b == "" and q_w == ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r))
                        )
                if(q_r == "" and q_b == "" and q_w == ""):
                    land_list = land_list
                if(q_r != "" and q_b != "" and q_w != ""):
                    land_list = land_list.filter(
                        Q(total_no_of_rooms__icontains=int(q_r)) & Q(no_of_bedroom__icontains=int(q_b)) & Q(no_of_bedroom__icontains=int(q_w))
                        )

    context = {
        "lands": land_list,
        "title": "Search Results"
    }
    return render(request, 'feed/search_results.html',context)

@login_required
def user_land_verified(request):
    land_list = Land.objects.filter(owner=request.user).filter(verified=True)
    page = request.GET.get('page',1)
    paginate = Paginator(land_list,8)
    try:
        lands = paginate.page(page)
    except PageNotAnInteger:
        lands = paginate.page(1)
    except EmptyPage:
        lands = paginate.page(paginate.num_pages)
    context = {
        "lands": lands,
        "title": request.user.username,
        "verification_status": "Verified"
    }
    return render(request, 'feed/user_posts.html',context)

@login_required
def user_land_unverified(request):
    land_list = Land.objects.filter(owner=request.user).filter(verified=False)
    page = request.GET.get('page',1)
    paginate = Paginator(land_list,8)
    try:
        lands = paginate.page(page)
    except PageNotAnInteger:
        lands = paginate.page(1)
    except EmptyPage:
        lands = paginate.page(paginate.num_pages)
    context = {
        "lands": lands,
        "title": request.user.username,
        "verification_status": "Not Verified"
    }
    return render(request, 'feed/user_posts.html',context)

class create_land(LoginRequiredMixin,CreateView):
    model = Land
    fields = ['location','info','area','area_unit','land_image','landownership_image','landownership_image_optional','longitude','latitude','price','is_house_or_apartment','total_no_of_rooms','no_of_bedroom','no_of_washroom','house_image']

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_fields(self,request,obj=None):
        if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
            fields.append('verified')
        return fields

class update_land(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Land
    fields = ['location','info','area','area_unit','land_image','price']
    verified = False

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        land = self.get_object()
        return self.request.user == land.owner

class detail_land(DetailView):
    model = Land
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments_connected = Comments.objects.filter(land=self.get_object()).order_by('-date_posted')
        context['comments'] = comments_connected
        if self.request.user:
            if self.object.wishlist.filter(id=self.request.user.id).exists():
                context['in_wishlist'] = True
                return context
        if self.request.user.is_authenticated:
            context['comment_form'] = NewCommentForm(instance=self.request.user) 
        context['in_wishlist'] = False
        return context
    
    def post(self,request, *args, **kwargs):
        new_comment = Comments(content=request.POST.get('content'),
                            user=self.request.user,
                            land=self.get_object())
        new_comment.save()
        return self.get(self,request,*args, **kwargs)


class delete_land(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Land
    success_url = "/"
    def test_func(self):
        land = self.get_object()
        return self.request.user == land.owner

def explore(request):
    last = Land.objects.count() - 1
    random_num = set()
    land_list = []
    for i in range(0,last):
        index = random.randint(0,last)
        if index not in random_num:
            random_num.add(index)
            land_list.append(Land.objects.all()[index])
    context = {
        "lands": land_list[0:8]
    }
    return render(request, 'feed/feed.html',context)

def wishlist(request):
    return render(request, 'feed/wishlist.html')

class update_land_form(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['location','info','area','area_unit','land_image','landownership_image','landownership_image_optional','longitude','latitude','price','verified']
