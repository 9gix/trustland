from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic.edit import ModelFormMixin
from django.views.generic.base import TemplateView
from django.contrib import messages 

from . import models
from . import forms


class PilotView(TemplateView):
    template_name = 'pilot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.AdopterForm()
        return context

    def post(self, request):
        form = forms.AdopterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you for your interest')
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, error)
        return redirect('pilot-view')

pilot_view = PilotView.as_view()
