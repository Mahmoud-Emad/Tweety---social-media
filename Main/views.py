from django.shortcuts import render, redirect
from Main.forms import TweetForm
from django.urls.base import reverse
# Create your views here.



def MainHoMe(request):
    form = TweetForm()
    if request.method =='POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.Name = request.user
            myform.save()
            return redirect(reverse('Home'))
            
    else:
        form = TweetForm()
    context = {'form':form}
    return render (request , 'Main.html',context)