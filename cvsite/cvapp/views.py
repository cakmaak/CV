from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def stokman(request):
    return render(request,'stokman.html')

def qr(request):
    return render(request,'qr.html')


def TicketSale(request):
    return render(request,'TicketSale.html')

def TicketSaleApi(request):
    return render(request,'TicketSalApi.html')

def contact(request):
    return render(request,"contact.html")


