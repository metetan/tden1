from django.shortcuts import render

# Create your views here.
def deneme2(request):
    toplam = 5
    return render(request,"index.html",{"toplam":toplam})