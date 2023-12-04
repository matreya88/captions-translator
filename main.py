import requests
import os

##### changeble vars ####################################

file_to_translate = "hakodate caps.sbv"

##### STATIC ##########################################
api_domain = "api-free.deepl.com"
deepl_api_key = os.environ["DEEPL_API_KEY"]
url = "https://api-free.deepl.com/v2/translate"
#####################################################


def make_translations():
    with open(file_to_translate, "r") as fil:
        text_to_translate = fil.read()

    headers = {
        'Authorization': f'DeepL-Auth-Key {deepl_api_key}',
        'Content-Type': 'application/json',
    }

    #### italian translation request #################
    parameters = {
        "text": [text_to_translate],
        "target_lang": "IT"
    }
    response = requests.post(url, json=parameters, headers=headers)
    result = response.json()
    translated_text = result["translations"][0]["text"]
    with open(f"{file_to_translate}_ita", "w") as fil:
        fil.write(translated_text)

    ######### japanese translation request #################
    parameters = {
        "text": [text_to_translate],
        "target_lang": "JA"
    }
    response = requests.post(url, json=parameters, headers=headers)
    result = response.json()
    translated_text = result["translations"][0]["text"]
    with open(f"{file_to_translate}_jap", "w", encoding="utf-8") as fil:
        fil.write(translated_text)
    ######## end translations section ###########################

    print("all translations complete.")


make_translations()