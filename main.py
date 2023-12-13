import requests
import os

# ######### variable to update ####################################
file_to_translate = "files_translations/captions.sbv"  # change this to your sbv file path


# ################# STATIC ##########################################
api_domain = "api-free.deepl.com"
deepl_api_key = os.environ["DEEPL_API_KEY"]
url = "https://api-free.deepl.com/v2/translate"
####################################################################


def make_translations():
    with open(file_to_translate, "r") as fil:
        text_to_translate = fil.read()

    headers = {
        'Authorization': f'DeepL-Auth-Key {deepl_api_key}',
        'Content-Type': 'application/json',
    }

    # ########## italian translation request #################
    parameters = {
        "text": [text_to_translate],
        "target_lang": "IT"
    }
    response = requests.post(url, json=parameters, headers=headers)
    result = response.json()
    translated_text = result["translations"][0]["text"]
    with open(f"{file_to_translate}_ita", "w", encoding="utf-8") as fil:
        fil.write(translated_text)

    # ########## japanese translation request #################
    parameters = {
        "text": [text_to_translate],
        "target_lang": "JA"
    }
    response = requests.post(url, json=parameters, headers=headers)
    result = response.json()
    translated_text = result["translations"][0]["text"]
    with open(f"{file_to_translate}_jap", "w", encoding="utf-8") as fil:
        fil.write(translated_text)

    # ########### spanish translation request #################
    parameters = {
        "text": [text_to_translate],
        "target_lang": "ES"
    }
    response = requests.post(url, json=parameters, headers=headers)
    result = response.json()
    translated_text = result["translations"][0]["text"]
    with open(f"{file_to_translate}_spanish", "w", encoding="utf-8") as fil:
        fil.write(translated_text)

    # ########## chinese translation request #################
    parameters = {
        "text": [text_to_translate],
        "target_lang": "ZH"
    }
    response = requests.post(url, json=parameters, headers=headers)
    result = response.json()
    translated_text = result["translations"][0]["text"]
    with open(f"{file_to_translate}_chinese", "w", encoding="utf-8") as fil:
        fil.write(translated_text)
    # ####### end of translations section ###########################

    print("all translations complete.")


make_translations()
