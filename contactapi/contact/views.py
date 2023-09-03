from django.shortcuts import render
from .models import Contact
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def contact_form(request):

    def __str__(self):
        return self.name
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return render(request, 'contact/success.html')
    else:
        return render(request, 'contact/form.html')
    

    