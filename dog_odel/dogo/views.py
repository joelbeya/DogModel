from django.shortcuts import render
from .mocks import Dog

# Create your views here.
def index(request):
    #dog = []
    # dog = [
    #     {'id':1, 'title':'Ya yambo', 'body':'Nzoto bwa ya yambo'},
    #     {'id':2, 'title':'Ya mibale', 'body':'Nzoto bwa ya mibale'},
    #     {'id':3, 'title':'Ya misato', 'body':'Nzoto bwa ya misato'},
    #     {'id':4, 'title':'Ya minei', 'body':'Nzoto bwa ya minei'},
    #     {'id':5, 'title':'Ya sambo', 'body':'Nzoto bwa ya sambo'},
    # ]
    dog = Dog.all()
    return render(request, 'dogo/index.html', {'dog':dog})

def show(request, id):
    # dog = [
    #     {'id':1, 'title':'Ya yambo', 'body':'Nzoto bwa ya yambo'},
    #     {'id':2, 'title':'Ya mibale', 'body':'Nzoto bwa ya mibale'},
    #     {'id':3, 'title':'Ya misato', 'body':'Nzoto bwa ya misato'},
    #     {'id':4, 'title':'Ya minei', 'body':'Nzoto bwa ya minei'},
    #     {'id':5, 'title':'Ya sambo', 'body':'Nzoto bwa ya sambo'},
    # ]
    dog = Dog.find(id)
    return render(request, 'dogo/show.html', {'doga':dog})
