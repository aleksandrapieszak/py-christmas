from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
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
        request.session.get('family_member')
        new_family_member = request.POST['new_family_member']
        if family_member == "new" and len(new_family_member) > 2 and new_family_member != family_member:
            new_dude = FamilyMember.objects.create(name=new_family_member)
            new_dude_id = FamilyMember.objects.get(id=new_dude.id)
            request.session['new_dude_id'] = new_dude_id
            return redirect("/")
        else:
            raise Http404




