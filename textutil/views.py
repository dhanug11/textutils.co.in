#Djay file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get("text","default")

    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcap','off')
    capfirst = request.POST.get('capfirst','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspceremover = request.POST.get('extraspceremover','off')
    charcount = request.POST.get('charcount','off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext = analyzed

    if fullcap == "on":
        analyzed=djtext.upper()
        params = {'purpose': 'Fully Capitalised.', 'analyzed_text': analyzed}
        djtext = analyzed

    if capfirst == "on":
        analyzed=djtext.capitalize()
        params = {'purpose': 'Capitalised fist letter.', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line removed successfully.', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed.', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcount == "on":
        analyzed=0
        for char in djtext:
            analyzed=analyzed+1
        params = {'purpose': 'Counted characters', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on" and fullcap != "on" and capfirst != "on" and newlineremover != "on" and extraspceremover != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


def about_us(request):
    about = request.GET.get('about', 'on')
    if about == "on":
        analyzed1='Dhananjay Gorde\nPaithan-431107\nSambhajinagar,MH,\nIndia.'
        params1 = {'purpose1': 'About Us', 'analyzed_text1': analyzed1}
        return render(request, 'analyze2.html', params1)
    else:
        return HttpResponse("Error")