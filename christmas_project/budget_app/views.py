from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from budget_app.models import FamilyMember


def start(request):
    return render(request, 'index.html')


def all_family(request):
    if request.method == 'GET':
        family = FamilyMember.objects.all()
        return render(request, 'login.html', {
            'family': family}
                    )
    else:
        family_member = request.POST['family_member']
        new_family_member = request.POST['new_family_member']
        if family_member == "New" and new_family_member.length > 2:
            family_member_id = request.POST['new_family_member_id']
            request.session['new_family_member_id'] = family_member_id
            return render(request, 'login.html', {
                'new_family_member': new_family_member,
                'new_family_member_id': family_member_id
            })



