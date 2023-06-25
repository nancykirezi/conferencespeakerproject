from django.shortcuts import render
from .models import Conference

class ConferenceListView(ListView):
    model = Conference
    template_name = 'conferences/conference_list.html'
    context_object_name = 'conferences'


class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'conferences/conference_detail.html'
    context_object_name = 'conference'


class ConferenceCreateView(CreateView):
    model = Conference
    template_name = 'conferences/conference_form.html'
    fields = '__all__'


class ConferenceUpdateView(UpdateView):
    model = Conference
    template_name = 'conferences/conference_form.html'
    fields = '__all__'


class ConferenceDeleteView(DeleteView):
    model = Conference
    template_name = 'conferences/conference_confirm'