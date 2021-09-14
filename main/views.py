from django.shortcuts import render
from .models import Contact, RequestBrand, Foundation, Resource
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def about(request):
    return render(request,'about.html')

def verificationmsg(request):
    return render(request,'verificationmsg.html')

def uploadmsg(request):
    return render(request,'uploadmsg.html')

def contactus(request):
    messages = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages = "Thanks for contacting us, we'll reach out you soon."
        msg = EmailMessage(
        "Somebody Contacted us!",
        "Name: "+name+ ", Email: "+email+ ", Message: "+message,
        settings.EMAIL_HOST_USER,
        ["sidharthv1017@gmail.com","mittalayush740@gmail.com"],
        )
        msg.send(fail_silently=False)
    return render(request,'contactus.html',{'message' : messages})

def faq(request):
    return render(request,'faq.html')

def privacy(request):
    return render(request,'privacy.html')

def error_404_view(request, exception):
     return render(request, '404.html')

def Favroiute(request):
    messages = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        brandname = request.POST.get('BrandName')
        brandsite = request.POST.get('BrandSite')
        want = request.POST.get('want')
        requestbrand = RequestBrand(name=name, email=email, brandname=brandname, brandsite=brandsite, want=want)
        requestbrand.save()
        messages = "Thanks for coming this far. We'll let you know when we speak to them."
        msg = EmailMessage(
        "Somebody requested a brand!",
        "Name: "+name+ ", Email: "+email+ ", Brand Name: "+brandname+ ", Brand site: "+brandsite+ ", Why they want: "+want,
        settings.EMAIL_HOST_USER,
        ["sidharthv1017@gmail.com","mittalayush740@gmail.com"],
        )
        msg.send(fail_silently=False)
    return render(request,'request.html',{'message' : messages})

def Course(request):
    messages = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        coursename = request.POST.get('coursename')
        courselink = request.POST.get('courselink')
        desc = request.POST.get('desc')
        foundation = Foundation(name=name, email=email, coursename=coursename, courselink=courselink, desc=desc)
        foundation.save()
        messages = "Thanks for filling this form."
        msg = EmailMessage(
        "Somebody requested a course!",
        "Name: "+name+ ", Email: "+email+ ", Course Name: "+coursename+ ", Course link: "+courselink+ ", Why they want: "+desc,
        settings.EMAIL_HOST_USER,
        ["sidharthv1017@gmail.com","mittalayush740@gmail.com"],
        )
        msg.send(fail_silently=False)
    return render(request,'foundation.html',{'message' : messages})

def Tools(request):
    messages = None
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        resource = Resource(email=email, phone=phone, college=college)
        resource.save()
        messages = "Thanks for filling this form."
    return render(request,'resource.html',{'message' : messages})


def wtf(request):
    return render(request,'wtf.html')
@login_required(login_url='/account/login')
def codewtf(request):
    return render(request,'codeWtf.html')

def avni(request):
    return render(request,'avni.html')
@login_required(login_url='/account/login')
def codeavni(request):
    return render(request,'codeAvni.html')

def peesafe(request):
    return render(request,'PEESAFE.html')
@login_required(login_url='/account/login')
def codepeesafe(request):
    return render(request,'codePEESAFE.html')

def naagin(request):
    return render(request,'Naagin.html')
@login_required(login_url='/account/login')
def codenaagin(request):
    return render(request,'codeNaagin.html')

def tbh(request):
    return render(request,'TBH.html')
@login_required(login_url='/account/login')
def codetbh(request):
    return render(request,'codeTBH.html')

def propshop(request):
    return render(request,'propshop.html')
@login_required(login_url='/account/login')
def codepropshop(request):
    return render(request,'codePropshop.html')

def yesdone(request):
    return render(request,'YesDone.html')
@login_required(login_url='/account/login')
def codeyesdone(request):
    return render(request,'codeYesDone.html')

def unlu(request):
    return render(request,'unlu.html')
@login_required(login_url='/account/login')
def codeunlu(request):
    return render(request,'codeUnlu.html')

def unlu2(request):
    return render(request,'unlu2.html')
@login_required(login_url='/account/login')
def codeunlu2(request):
    return render(request,'codeUnlu2.html')

def trib(request):
    return render(request,'Trib.html')
@login_required(login_url='/account/login')
def codetrib(request):
    return render(request,'codeTrib.html')

def skoosh(request):
    return render(request,'skoosh.html')
@login_required(login_url='/account/login')
def codeskoosh(request):
    return render(request,'codeskoosh.html')

def bitclass(request):
    return render(request,'bitclass.html')
@login_required(login_url='/account/login')
def codebitclass(request):
    return render(request,'codebitclass.html')

def chaaryaar(request):
    return render(request,'chaaryaar.html')
@login_required(login_url='/account/login')
def codechaaryaar(request):
    return render(request,'codechaaryaar.html')

def mypaperclip(request):
    return render(request,'mypaperclip.html')
@login_required(login_url='/account/login')
def codemypaperclip(request):
    return render(request,'codemypaperclip.html')

def mittihub(request):
    return render(request,'mittihub.html')
@login_required(login_url='/account/login')
def codemittihub(request):
    return render(request,'codemittihub.html')

def sattviko(request):
    return render(request,'sattviko.html')
@login_required(login_url='/account/login')
def codesattviko(request):
    return render(request,'codesattviko.html')

def rapido(request):
    return render(request,'rapido.html')
@login_required(login_url='/account/login')
def coderapido(request):
    return render(request,'coderapido.html')

def TWC(request):
    return render(request,'TWC.html')
@login_required(login_url='/account/login')
def codeTWC(request):
    return render(request,'codeTWC.html')

def ptal(request):
    return render(request,'ptal.html')
@login_required(login_url='/account/login')
def codeptal(request):
    return render(request,'codeptal.html')

def bookchor(request):
    return render(request,'bookchor.html')
@login_required(login_url='/account/login')
def codebookchor(request):
    return render(request,'codebookchor.html')













