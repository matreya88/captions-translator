import requests
import os

# ######### variable to update ####################################
file_to_translate = "files_translations/captions.sbv"  # change this to your sbv file path
languages = ["IT", "JA", "ES", "ZH"]  # add here languages you want to translate to

# ################# CONST ##########################################
DEEPL_API_KEY = os.environ["DEEPL_API_KEY"]
URL = "https://api-free.deepl.com/v2/translate"
####################################################################


def translate():
    with open(file_to_translate, "r") as file_to_read:
        text_to_translate = file_to_read.read()

    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
        'Content-Type': 'application/json',
    }

    for language in languages:
        parameters = {
            "text": [text_to_translate],
            "target_lang": language
        }
        response = requests.post(URL, json=parameters, headers=headers)
        result = response.json()
        translated_text = result["translations"][0]["text"]
        with open(f"{file_to_translate}_{language}", "w", encoding="utf-8") as file_to_write:
            file_to_write.write(translated_text)
    print("all translations complete.")


translate()
