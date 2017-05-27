from django.shortcuts import render

# Create your views here.
def contact(request):
    context = local()
    template = "contact.html"
    reqturn render(reqeust, template, context)
