from django.shortcuts import render # type: ignore

# Create your views here.
def jinga_print(request):
    d={'name':'Vasu','age':22}
    return render(request, 'jinga_print.html', context=d)
