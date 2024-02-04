from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {"text": "Hello World!", "number": 100}
    return render(request, 'basicapp/index.html', context=context_dict)


def other(request):
    return render(request, 'basicapp/other.html')


# def base(request):
#     return render(request, 'basicapp/base.html')


def relative(request):
    return render(request, 'basicapp/relative_url_templates.html')

