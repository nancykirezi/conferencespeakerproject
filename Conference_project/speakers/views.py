from django.shortcuts import render
from .models import speaker
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def create_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('speakers:list')
    else:
        form = SpeakerForm()
    return render(request, 'speakers/create_speaker.html', {'form': form})

def update_speaker(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES, instance=speaker)
        if form.is_valid():
            form.save()
            return redirect('speakers:list')
    else:
        form = SpeakerForm(instance=speaker)
    return render(request, 'speakers/update_speaker.html', {'form': form, 'speaker': speaker})

def delete_speaker(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    if request.method == 'POST':
        speaker.delete()
        return redirect('speakers:list')
    return render(request, 'speakers/delete_speaker.html', {'speaker': speaker})

def speaker_details(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    return render(request, 'speakers/speaker_details.html', {'speaker': speaker})

def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'speakers/speaker_list.html', {'speakers': speakers})
