import requests
from django.shortcuts import render # type: ignore

def home(request):
    result = None
    word = ''
    if request.method == 'POST':
        word = request.POST.get('word')
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            result = response.json()[0]
        else:
            result = {'error': 'Word not found'}

    return render(request, 'dictionary/home.html', {'result': result, 'word': word})
