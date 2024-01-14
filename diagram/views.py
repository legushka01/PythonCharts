from django.shortcuts import render
from .forms import QalaDataFrom
from .models import QalaData


def index(request):
    data = QalaData.objects.all()
    if request.method == 'POST':
        form = QalaDataFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QalaDataFrom()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'diagram/index.html', context)

