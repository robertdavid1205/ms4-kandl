from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


# Credits to  https://docs.djangoproject.com/en/4.0/topics/forms/
def contact(request):
    """View to render contact page"""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent!')
            # redirect to contact page
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'There was a problem sending your message. \
                    Please try again.')
    else:
        # Create a blank form
        form = ContactForm()

        template = 'contact/contact.html'
        context = {
            'form': form,
        }

    return render(request, template, context)
