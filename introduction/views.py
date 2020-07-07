from django.shortcuts import render


# Create your views here.


def introductionView(request):
    return render(request, 'introduction.html', locals())
