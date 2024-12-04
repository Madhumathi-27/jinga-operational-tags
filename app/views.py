from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'name':'Chandrakala','age':23,'marks':430}
    d1={'a':10,'b':20,'c':30}
    d2={'a':20,'b':30,'c':40,'d':'12'}
    return render(request,'jinga_operational_tags.html',d)
