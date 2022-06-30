from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from api.models import Profile, Relatives

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CreateProfileForm
from .models import Space, Message


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('admin_page'))
    else:
        form = UserCreationForm()
        return render(request, 'create.html', {'form': form})


def extend_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('admin_page'))
    else:
        form = CreateProfileForm()
    return render(request, 'extend.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        admin_username = 'baye'
        admin_password = 'baye'

        user = authenticate(username=username, password=password)

        if username == admin_username and password == admin_password:
            return redirect('admin_page/')
        elif user is not None:
            login(request, user)
            return redirect('profile_page/')

        else:
            form = AuthenticationForm(request.POST)
            messages.info(request, 'Credentials Invalid')
            return render(request, 'signin.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})


#### For admin page
class ProfileListView(ListView):
    model = Profile
    template_name = 'admin_page.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'details.html'


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['user', 'phone', 'address', 'profession', 'age', 'sex']
    template_name = 'update.html'


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'delete.html'
    success_url = reverse_lazy('admin_page')


################ Views for Relatives

def relatives(request):
    son = Relatives.objects.get(link='Son')
    daughter = Relatives.objects.get(link='Daughter')
    sister = Relatives.objects.get(link='Sister')
    brother = Relatives.objects.get(link='Brother')
    mother = Relatives.objects.get(link='Mother')

    context = {
        'son': son,
        'daughter': daughter,
        'sister': sister,
        'brother': brother,
        'mother': mother,
        }
    return render(request, 'profile_page.html', context=context)


# class GenealogicalTreeListView(ListView):
#     model = Relatives
#     template_name = 'tree.html'


class GenealogicalTreeCreateView(CreateView):
    model = Relatives
    template_name = 'create_relatives.html'
    fields = '__all__'
    success_url = reverse_lazy('profile_page')


@login_required
def spaces(request):
    spaces = Space.objects.all()

    return render(request, 'spaces.html', {'spaces': spaces})


@login_required
def space(request, slug):
    space = Space.objects.get(slug=slug)
    messages = Message.objects.filter(space=space)[0:25]

    return render(request, 'space.html', {'space': space, 'messages': messages})