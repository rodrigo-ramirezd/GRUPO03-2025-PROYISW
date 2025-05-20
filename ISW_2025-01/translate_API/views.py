from django.shortcuts import render
import requests

def translate_text(text, source_lang='en', target_lang='es'):
    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }
    response = requests.post(url, data=payload)
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code == 200:
        return response.json()['translatedText']
    else:
        return "Error en la traducción."


def translate_view(request):
    translated = ""
    if request.method == "POST":
        original_text = request.POST.get("texto", "")
        translated = translate_text(original_text)

    return render(request, "translate.html", {"translated": translated})
