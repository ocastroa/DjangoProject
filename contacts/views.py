from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contacts(request):
    if request.method == 'POST':
        # Get form values
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if(has_contacted):
                messages.error(request, 'You already made an inquiry for this listing')
                return redirect('/listings/' + listing_id) 

        contacts = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone,
        message=message, user_id=user_id)

        contacts.save()

        # send_mail(
        #     'Property Inquiry for ' + listing,
        #     name + ' made an inquiry for ' + listing + '. Sign into the admin panel for more information.',
        #     '',
        #     [email],
        #     fail_silently=False,
        # )

        messages.success(request, 'Your request has been submitted! A realtor will get back to you shortly')
        return redirect('/listings/' + listing_id)

