from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            #add to dictionary
            word_dictionary[word] = 1


    return render(request, 'result.html', {'fulltext' : text, 'total' : len(words), 'dictionary' : word_dictionary.items()})

def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')
    
def warn(request):
    return render(request, 'warn.html')