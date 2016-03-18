from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from my_app.models import Participant, Room
from django.views.decorators.csrf import csrf_exempt # fix later so thatcsrf exeemption isnt on loggedIn
from .forms import CustomUserCreationForm, ContactForm # allows the creation of individualized registration form
from django.contrib.auth import logout
import hashlib # to encode adn transform room number into a key
from my_app.forms import ContactForm # to create a user contact form



# Create your views here.
def home(request):
    # note: request is in the cycle. the request is you. whatever window you go to, you will be there.
    # request goes with everying
    # note: the context dictionary stores data that will be given to the html page, when it renders a page
    # html is always constructed by a python script
    context = dict()  # note: this dictionary stores datat that will be rendered on the html page
    return render(request, "home.html", context)
    # Q: what is render
    # note: tell it which page to render with
    # & html is always rendered after the data is retrieved from the html

def about(request):
    context = dict()
    return render(request,"about.html", context)

def compete(request):
    context = dict()
    return render(request,"compete.html", context)

def competitions(request):
    context = dict()
    return render(request,"competitions.html", context)

def guest(request):
    context = ()
    return render(request,"guest.html", context)

@csrf_exempt
def register(request):
    context = dict()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            rm_obj = Room(room = 'a', key='1')
            rm_obj.save()
            participant_obj = Participant(user = new_user,rm_1 = rm_obj)
            # Q: what if this order was reversed & foreign key object switched.
            # therfore participant could be saved without a room
            # then, rather then having dummy room & key info, room & key could immediately be set equal to participant_obj.id
            return HttpResponseRedirect("/login")
    else:
        form = CustomUserCreationForm()
    context['form'] = form
    return render(request, "registration/register.html", context)

def loggedIn(request):
    context = dict()
    the_user = request.user
    participant_obj = Participant.objects.get(user=the_user)
    rm_obj = Room(room = participant_obj.id , key= code(participant_obj.id))
    rm_obj.save()
    context['participant'] = participant_obj
    context['room'] = rm_obj
    return render(request,'loggedIn.html',context)

def code(a):
    mystring = str(a)
    hash_object = hashlib.md5(mystring.encode())
    return(hash_object.hexdigest())


def logout_view(request):
    logout(request)
    return render(request, "loggedOut.html")

# function to use for inviting friends to participate
def contact(request):
    form_class = ContactForm
    return render(request, 'contact.html')

'''def form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']
    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)
    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')'''