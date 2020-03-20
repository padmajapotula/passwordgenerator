from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,"password/home.html")
def password(request):
    thepassword=''
    character=list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("upper"):
        character.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get("special"):
        character.extend("!@#$%^&*()")
    if request.GET.get("numeric"):
        character.extend("1234567890")
    length=int(request.GET.get("length"))
    for i in range(length):
        thepassword+=random.choice(character)
    return render(request,"password/password.html",{"password":thepassword})
