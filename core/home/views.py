from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return render(request,"index.html")      #static webpage

def home(request):

    peoples=[
        {'name':'Avni Goyal','age':19},
        {'name':'Paridhi Goyal','age':19},
        {'name':'Eshpreet Wasan','age':19},
        {'name':'Himani Goyal','age':19},
        {'name':'Anil Goyal','age':19},
    ]

    text="""Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptatibus, ipsa autem asperiores sequi assumenda distinctio laboriosam deleniti facilis placeat, minima accusamus deserunt. Molestias, voluptatum sunt laborum velit soluta est sapiente adipisci quo quis officia atque nisi quos quasi debitis nesciunt id error sint eaque dolore tempore. Deserunt autem adipisci omnis!"""


    vegetables={'pumpkin','tomato','potato',}

    return render(request,"home/index.html",context={'peoples':peoples,'text':text,'vegetable':vegetables})


def about(request):
    context={'page':'about'}
    return render(request,"home/about.html",context)

def contact(request):
    context={'page':'contact'}
    return render(request,"home/contact.html",context)


def success_page(request):
    return HttpResponse('<h1>Hey this is a success page</h1>')