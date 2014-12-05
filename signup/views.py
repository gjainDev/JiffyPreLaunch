import json
import os
from django.http import HttpResponse
from django.shortcuts import render
from db_access.db_adaptor import DBAdapter
from rest_framework.decorators import api_view
from signup.gmail_contacts import ContactsEmail
from signup.send_email import send_email


@api_view(['POST'])
def sign_up_user(request):
    params = request.GET
    data = request.DATA
    db_adapter = DBAdapter()
    user_existing = db_adapter.get_user(data.get('email'), data.get('phone'))
    if user_existing is None:
        db_adapter.create_user(data.get('name'), data.get('email'), data.get('phone'), data.get('location'),
                                 data.get('description'), data.get('type'))
        referral_id = params.get('referral_id')
        referral = db_adapter.get_referral_by_id(referral_id)
        if referral is not None:
            db_adapter.update_referral(ref_id=referral_id, status=1)
        result = dict(success=True)
        return HttpResponse(json.dumps(result))
    else:
        result = dict(success=False)
        return HttpResponse(json.dumps(result))


@api_view(['POST'])
def send_invite(request):
    data = request.DATA
    user_name = data.get('username')
    password = data.get('password')
    gmail_contacts = ContactsEmail(user_name, password)
    emails = gmail_contacts.ListAllContacts()
    print emails
    emails = ['gaurav1987star@gmail.com']
    for email in emails:
        try:
            ref_id = os.urandom(32).encode('hex')
            send_email(email, ref_id)
            db_adapter = DBAdapter()
            user = db_adapter.get_user(data.get('email'), data.get('phone'))
            db_adapter.create_referral(user, ref_id)
        except Exception as e:
            pass
