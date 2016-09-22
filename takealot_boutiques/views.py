from django.shortcuts import render, redirect


def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def pricing(request):
    context = {}
    return render(request, 'home/pricing.html', context)


from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        uf = UserCreationForm(request.POST)
        if uf.is_valid():
            uf.save()
            return redirect('/user_apps')
    else:
        context = {}
        return render(request, 'register.html', context)
