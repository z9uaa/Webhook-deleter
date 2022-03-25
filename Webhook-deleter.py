import requests
import webbrowser
print('Program By Flxr | Instagram : z9ua | Discord.gg/FFF')
webbrowser.open_new('https://discord.gg/fff')
webhook_url = input("Enter Webhook To Delete : ")
if webhook_url.startswith("https://discord.com/api/webhooks/"):
    try:
        requests.delete(webhook_url.rstrip())
        print("Webhook deleted !")
    except:
        print('[X] Error !')