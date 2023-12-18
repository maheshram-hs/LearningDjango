from django.shortcuts import render
from score.models import Score
from score.forms import ScoreForm

def index(request):
    context = {}
    form = ScoreForm()
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            form = ScoreForm(request.POST)
            form.save()
    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)
