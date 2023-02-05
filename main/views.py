# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .forms import ChoiceForm
from .tasks import send_list


def index(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            layout = form.cleaned_data['choice_layout']
            countdown = form.cleaned_data['choice_delay_seconds']
            for s in form.cleaned_data['choice_subscriber']:
                send_list.apply_async((s.name, s.last_name, str(s.birthday)[:10], [s.email], layout), countdown=countdown)
        return render(request, 'index.html', {'form': form})
    else:
        form = ChoiceForm()
        return render(request, 'index.html', {'form': form})


def tracking(request):
    print('OK')
    return HttpResponse('hello OK')
