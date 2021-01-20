from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:

        contact_form = ContactForm()

        template = 'contact/contact_us.html'
        context = {
            'contact_form': contact_form,

        }

    return render(request, 'contact/contact_us.html', context)

def submissions(request):
    submissions = Contact.objects.all().order_by('date')
    return render(request, 'contact/submissions.html', {'submissions': submissions})

