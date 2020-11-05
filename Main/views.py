from django.shortcuts import render


def Home(request):
    context = {}
    return render(request,"home.html",context)

    
def test(request):
    context = {}
    return render(request,"test.html",context)