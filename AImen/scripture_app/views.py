import json
import os
import random
from django.conf import settings
from django.shortcuts import render, redirect

def emotion_view(request):
    name = request.session.get('name')
    gender = request.session.get('gender')
    if not name or not gender:
        return redirect('welcome_view') 

    emotion = request.GET.get('emotion', None)

    json_path = os.path.join(settings.BASE_DIR, 'scripture_app', 'data', 'bible_verses.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    emotions = data

    verses = data.get(emotion, [])  

    verse = random.choice(verses) if verses else None

    context = {
        'name': name,
        'gender': gender,  
        'emotions': list(data.keys()),
        'selected_emotion': emotion,
        'verse': verse 
    }
    return render(request, 'emotions.html', context)

def welcome_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        if name and gender:
            request.session['name'] = name
            request.session['gender'] = gender
            return redirect('emotion_view') 
    return render(request, 'welcome.html')