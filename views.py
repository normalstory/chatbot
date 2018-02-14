from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, './chatbot_index.html',{})

def gongju(request):
    return render(request, 'pages/chatbot.html', {'choose_gov':'60ca71b4-5d7f-4679-abd4-5fb8bbbf1ec6', 'choose_user':'9b50b9cd45ad4ad89ff3c6512fe2237e'}) 

def chunan(request):
    return render(request, 'pages/chatbot.html', {'choose_gov':'976706de-24a3-419e-adf5-5030ce7d29ad', 'choose_user':'9b50b9cd45ad4ad89ff3c6512fe2237e'}) 

def sejong(request):
    return render(request, 'pages/chatbot.html', {'choose_gov':'a5891e49-90e4-4f16-957b-11527881a745', 'choose_user':'4ca0e819af2341a09da357543cce401b'})
