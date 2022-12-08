import requests
import json
from account.signals import custom_receiver

 # page_activity="advanced search"
    # custom_receiver(user,request,page_activity)

def updatepaymentadvice(foo, rate, currency_type, purpose, doclanguage,user,request):
    url = "http://192.236.154.69:280/api/Values"

    if purpose and rate and currency_type and doclanguage:
        payload = json.dumps({
            "receiptnumber": f"{foo}",
            "currency": f"{currency_type}",
            "conversionRate": f"{rate}",
            "purpose": f"{purpose}",
            "language": f"{doclanguage}"
        }) 
        headers = {
        'Content-Type': 'application/json'
        }

        # log activity
        page_activity=f"updated purpose, rate, currency & doclanguage on payment advice #{foo}"
        custom_receiver(user,request,page_activity)
        
        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

    elif purpose and rate and currency_type and not doclanguage:
        payload = json.dumps({
            "receiptnumber": f"{foo}",
            "purpose": f"{purpose}",
            "conversionRate": f"{rate}",
            "currency": f"{currency_type}",
        })  
        headers = {
        'Content-Type': 'application/json'
        }

        # log activity
        page_activity=f"updated purpose, rate & currency on payment advice #{foo}"
        custom_receiver(user,request,page_activity)

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text
    elif purpose and not rate and not currency_type and not doclanguage:
        payload = json.dumps({
            "receiptnumber": f"{foo}",
            "purpose": f"{purpose}",
        }) 
        headers = {
        'Content-Type': 'application/json'
        }

        # log activity
        page_activity=f"updated purpose on payment advice #{foo}"
        custom_receiver(user,request,page_activity)

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text
    elif not purpose and rate and currency_type and not doclanguage:
        payload = json.dumps({
            "receiptnumber": f"{foo}",
            "conversionRate": f"{rate}",
            "currency": f"{currency_type}",
        }) 
        headers = {
        'Content-Type': 'application/json'
        }

        # log activity
        page_activity=f"updated currency on payment advice #{foo}"
        custom_receiver(user,request,page_activity)

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text
        
    elif not purpose and not rate and not currency_type and doclanguage:
        payload = json.dumps({
            "receiptnumber": f"{foo}",
            "language": f"{doclanguage}"
        }) 
        headers = {
        'Content-Type': 'application/json'
        }


        # log activity
        page_activity=f"updated doclanguage on payment advice #{foo}"
        custom_receiver(user,request,page_activity)

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text
    
    elif purpose and not rate and not currency_type and doclanguage:
        payload = json.dumps({
            "receiptnumber": f"{foo}",
            "purpose": f"{purpose}",
            "language": f"{doclanguage}"
        }) 
        headers = {
        'Content-Type': 'application/json'
        }
        
        # log activity
        page_activity=f"updated purpose & doclanguage on payment advice #{foo}"
        custom_receiver(user,request,page_activity)

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text


   

def updateremittanceallocation(foo, doclanguage,user,request):
    url = "http://192.236.154.69:280/api/PairedReceipt"

    payload = json.dumps({
        "receiptnumber": f"{foo}",
        "language": f"{doclanguage}"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    # log activity
    page_activity=f"updated doclanguage on remittance allocation #{foo}"
    custom_receiver(user,request,page_activity)
    
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def updatenonpairedreceipt(foo, doclanguage,narration,user,request):
    url = "http://192.236.154.69:280/api/Nonpaired"

    if doclanguage and not narration:
        payload = json.dumps({
        "receiptnumber": f"{foo}",
        "language": f"{doclanguage}"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        # log activity
        page_activity=f"updated doclanguage on non-paired receipt #{foo}"
        custom_receiver(user,request,page_activity)

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text
    elif not doclanguage and narration:
        payload = json.dumps({
        "receiptnumber": f"{foo}",
        "narration": f"{narration}"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        # log activity
        page_activity=f"updated narration on non-paired receipt #{foo}"
        custom_receiver(user,request,page_activity)

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text


    

  