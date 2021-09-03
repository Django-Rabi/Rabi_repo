from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def moviesinfo(request):
    head_msg='Latest Movie Information'
    msg1='Sonali slowly getting cured'
    msg2='Salman  going to marriage soon'
    msg3='Narendra Modi  is going to act in some movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest Sports Information'
    msg1='Anushka Sharma Firing Like anything'
    msg2='Kohli updating in game anything can happend'
    msg3='India Performance not upto the mark in asian Games'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg='Latest Politcs Information'
    msg1='Achhce Din Aaa gaya'
    msg2='Rupee Value now 1$:70Rs'
    msg3='In India Single Paisa Black money No more'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
