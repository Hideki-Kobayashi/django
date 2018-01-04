from django.shortcuts import render
from django.contrib.auth.decorators import login_required
 
 
def index(request):
    return render(request, 'accounts/index.html')
 
 
@login_required
def mypage(request):
    return render(request, 'accounts/mypage.html')
 
 
@login_required
def redilect(request):
    return render(request, 'accounts/redirect.html')