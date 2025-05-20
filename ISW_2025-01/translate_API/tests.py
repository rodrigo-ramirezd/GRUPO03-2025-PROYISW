from django.test import TestCase
import unittest
import requests
import os

class AzureTranslateAPITestCase(TestCase):
    def setUp(self):
        self.endpoint = "https://api.cognitive.microsofttranslator.com/translate"
        self.subscription_key = os.getenv("AZURE_TRANSLATE_KEY")  # Usa variables de entorno
        self.location = os.getenv("AZURE_TRANSLATE_REGION")       # Ej: "eastus"
        self.headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Ocp-Apim-Subscription-Region": self.location,
            "Content-type": "application/json"
        }
        self.params = {
            "api-version": "3.0",
            "from": "en",
            "to": ["es"]
        }

    def test_translation(self):
        body = [{"text": "Hello, world!"}]
        response = requests.post(self.endpoint, params=self.params, headers=self.headers, json=body)

        self.assertEqual(response.status_code, 200)
        translation = response.json()[0]['translations'][0]['text'].lower()
        self.assertIn("hola", translation)

