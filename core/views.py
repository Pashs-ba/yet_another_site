from django.shortcuts import render

def main_en(request):
    return render(request, 'en/main.html')