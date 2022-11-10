import requests
import json

def sendemail(foo):
    url = "http://10.0.33.38:655/api/values"

    payload = json.dumps({
        "receiptNumber": f"{foo}"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
