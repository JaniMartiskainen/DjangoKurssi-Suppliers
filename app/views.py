from django.shortcuts import render

def landingview(request):
    return render(request, 'landingpage.html')

def productlistview(request):
    return render(request, 'productlist.html')

# DATAN LÄHETYKSEN ESIMERKKI
# def supplierlistview(request):
#     muuttuja = "tämä on merkkijono"
#     context = {'x': muuttuja}
#     return render(request, 'supplierlist.html', context)

def supplierlistview(request):
    return render(request, 'supplierlist.html')