#!pyhon3
import sys
import requests
import localsecrets

api_key = localsecrets.bloom_api_key

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer "+api_key}

def get_response(input):
    payload =  {"inputs": input}
    response = requests.post(API_URL, headers=headers, json=payload)
    generated_text = response.json()[0]['generated_text'].strip()
    print(generated_text)
    return generated_text

def main(firstinput):
    res=""
    if firstinput != "":
        res = get_response(firstinput)
    while True:
        user_input = input("> ").strip()
        if user_input in ["quit", "exit", "bye"]:
            break
        if user_input in ["reset"]:
            res=""
            user_input = input("> ").strip()
        res = get_response(res + " " + user_input)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) > 0:
        main(args[0])
    else:
        main("")
