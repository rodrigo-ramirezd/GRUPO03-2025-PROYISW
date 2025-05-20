from django.shortcuts import render
import requests
import os

def translate_text(request):
    translated_text = None

    if request.method == 'POST':
        text_to_translate = request.POST.get('text')
        to_lang = request.POST.get('to_lang', 'es')

        subscription_key = os.getenv("AZURE_TRANSLATOR_KEY")
        endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
        location = os.getenv("AZURE_TRANSLATOR_LOCATION")

        path = '/translate?api-version=3.0'
        params = f"&to={to_lang}"
        constructed_url = endpoint + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json'
        }

        body = [{'text': text_to_translate}]
        response = requests.post(constructed_url, headers=headers, json=body)

        if response.status_code == 200:
            translated_text = response.json()[0]['translations'][0]['text']
        else:
            translated_text = f"Error: {response.status_code}"

    return render(request, 'translate.html', {'translated_text': translated_text})
