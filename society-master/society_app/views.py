from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Member, MaintenanceRecord, Complaint
from .forms import MemberRegistrationForm, MemberUpdateForm, AdminUpdateForm, ComplaintForm
from django.shortcuts import get_object_or_404

# Superuser
# 1
# django@gmail.com 
# django123
# 101
# password = django123
# 55
# password = ironman123
# Create your views here.

@login_required
def file_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, member=request.user)
        if form.is_valid():
            form.save()
            return redirect('member_complaints', username=request.user)
    else:
        form = ComplaintForm(member=request.user)
        return render(request, 'society_app/file_complaint.html', {'form': form})

@login_required
def member_complaints(request, username):
    member = get_object_or_404(Member, username=username)
    complaints = Complaint.objects.filter(member=member)
    context = {
        'member': member,
        'complaints': complaints,
    }
    return render(request, 'society_app/member_complaints.html', context)

@login_required
def m_maintenance(request, username):
    member = get_object_or_404(Member, username=username)
    maintenance = MaintenanceRecord.objects.filter(member=member)
    context = {
        'member': member,
        'maintenances': maintenance,
    }
    return render(request, 'society_app/m_maintenance.html', context)

@login_required
def delete_complaint(request, pk):
    complaint = Complaint.objects.get(id=pk)
    if request.method == 'POST':
        complaint.delete()
        return redirect('member_complaints', username=request.user)
    return render(request, 'society_app/delete_complaint.html', {'obj':complaint})

@login_required
def admin_complaints(request):
    complaints = Complaint.objects.all()
    return render(request, 'society_app/admin_complaints.html', {'complaints':complaints})

def home(request):
    return render(request, 'society_app/home.html')

def h_login(request):
    return render(request, 'society_app/login.html')

def member_register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            login(request, member)
            return redirect('member', pk=member.username)
    else:
        form = MemberRegistrationForm()
    return render(request, 'society_app/member_register.html', {'form': form})

def member_login(request):
    if request.method == "POST":
        flat_no = request.POST.get("username")
        password = request.POST.get("pw")
        member = authenticate(username=flat_no, password=password)
        if member is None:
            return render(request, 'society_app/member_login.html', {'msg':'Invalid login'})
        else:
            login(request, member)
            return redirect('member', pk=member.username)
    else:
        return render(request, 'society_app/member_login.html')
    
def admin_login(request):
    if request.method == "POST":
        flat_no = request.POST.get("username")
        password = request.POST.get("pw")
        member = authenticate(username=flat_no, password=password)

        if flat_no == '1':
            login(request, member)
            return redirect('admin_home')
        else:
            return render(request, 'society_app/admin_login.html', {'msg':'Invalid login'})
    else:
        return render(request, 'society_app/admin_login.html')

@login_required  
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required
def member(request, pk):
    member = Member.objects.get(username=pk)
    return render(request, 'society_app/member.html', {'member':member})

# ADMIN VIEWS

@login_required
def admin_home(request):
    return render(request, 'society_app/admin_home.html')

@login_required
def members(request):
    members = Member.objects.all()
    return render(request, 'society_app/members.html', {'members':members})

@login_required
def a_member(request, pk):
    member = Member.objects.get(username=pk)
    return render(request, 'society_app/a_member.html', {'member':member})

@login_required
def member_update(request, pk):
    member = Member.objects.get(username=pk)
    form = MemberUpdateForm(instance=member)
    if request.method == 'POST':
        form = MemberUpdateForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member', pk=member.username)
        
    return render(request, 'society_app/member_update.html', {'form': form})

@login_required
def a_update(request, pk):
    member = Member.objects.get(username=pk)
    form = AdminUpdateForm(instance=member)
    if request.method == 'POST':
        form = AdminUpdateForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
        
    return render(request, 'society_app/admin_update.html', {'form': form})

@login_required
def delete_member(request, pk):
    member = Member.objects.get(username=pk)
    # if request.user != member.username:
    #     return HttpResponse('U r not allowed here!!')
    
    if request.method == 'POST':
        member.delete()
        return redirect('members')
    return render(request, 'society_app/delete.html', {'obj':member})

@login_required
def maintenance(request):
    maintenance = MaintenanceRecord.objects.all()
    return render(request, 'society_app/maintenance.html', {'maintenance':maintenance})






