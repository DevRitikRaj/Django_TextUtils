from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    param = {'name': 'Prakash', 'Place': 'Delhi'}
    return render(request, 'about.html', param)


def analyzer(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    lowercaps = request.POST.get('lowercaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzer.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'To capitalize', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzer.html', params)

    if (lowercaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'To LOWER', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzer.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'NEW LINEREMOVER', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzer.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

        return render(request, 'analyzer.html', params)

 




