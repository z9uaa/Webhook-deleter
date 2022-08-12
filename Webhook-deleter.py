import requests
print('Program By Flxr | Instagram : 1ee_')
webhook_url = input("Enter Webhook To Delete : ")
if webhook_url.startswith("https://discord.com/api/webhooks/"):
    try:
        requests.delete(webhook_url.rstrip())
        print("Webhook deleted !")
    except:
        print('[X] Error !')
