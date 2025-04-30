from django.shortcuts import render
from .models import Service, FAQ, Contact

# Create your views here.
def index(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project = request.POST.get('project')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, phone=phone, project=project, subject=subject, message=message)
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'service.html', context)

def service_detail(request, id):
    service = Service.objects.get(id=id)
    context = {
        'service': service,
    }
    return render(request, 'service_detail.html', context)

def faq(request):
    faq = FAQ.objects.all()
    context = {
        'faq': faq,
    }
    return render(request, 'FAQ.html', context)