from django.shortcuts import render
from . models import Contact, Project
# Create your views here.
def home(request):
    return render(request, 'sparklabs/index.html')

def about(request):
    return render(request, 'sparklabs/about.html')

def services(request):
    return render(request, 'sparklabs/services.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'sparklabs/portfolio.html', context={'pr':projects})

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        sub = request.POST.get('email_sub', '')
        msg = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, email_sub=sub, message=msg)
        contact.save()
    return render(request, 'sparklabs/contact.html')
