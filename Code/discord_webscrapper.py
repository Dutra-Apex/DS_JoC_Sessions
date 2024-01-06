import json
import requests

def retrieve_messages(channel_id, authorization, filename):
    headers = {
        'authorization' : authorization
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', headers=headers)
    json_obj = json.loads(r.text)
 
    filter(json_obj)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(json_obj, file, ensure_ascii=False, indent=4)

    # for value in json_obj:
    #     print(value, '\n')

auth = ''
channel_id = ""
filename = 'discord_messages.json'
retrieve_messages(channel_id, auth, filename)
