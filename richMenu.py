import requests
from dotenv import dotenv_values
config = dotenv_values(".env")

from linebot import LineBotApi
from linebot.exceptions import LineBotApiError


line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

def createRichMenu():
    requests.post(
        "https://api.line.me/v2/bot/richmenu",
        headers={
            "Authorization" :  "Bearer " + config.get("LINE_CHANNEL_ACCESS_TOKEN"),
            "Content-Type": "application/json"
        },
        json = {
            "size": {
                "width": 1200,
                "height": 810
            },
            "selected": True,
            "name": "richmenu-1",
            "chatBarText": "風格選擇",
            "areas": [
                {
                    "bounds": {
                        "x": 0,
                        "y": 0,
                        "width": 400,
                        "height": 405
                    },
                    "action": {
                        "type": "message",
                        "label": "文字",
                        "text": "Hello, iBot!"
                    }
                },
                {
                    "bounds": {
                        "x": 400,
                        "y": 0,
                        "width": 400,
                        "height": 405
                    },
                    "action": {
                        "type": "uri",
                        "label": "網址",
                        "uri": "https://ithelp.ithome.com.tw/users/20106865/ironman/2732"
                    }
                },
                {
                    "bounds": {
                        "x": 800,
                        "y": 0,
                        "width": 400,
                        "height": 405
                    },
                    "action": {
                        "type": "postback",
                        "label": "選單2",
                        "data": "action=changeMenu2"
                    }
                },
                {
                    "bounds": {
                        "x": 0,
                        "y": 405,
                        "width": 400,
                        "height": 405
                    },
                    "action": {
                        "type": "message",
                        "label": "文字",
                        "text": "Hello, iBot!"
                    }
                },
                {
                    "bounds": {
                        "x": 400,
                        "y": 405,
                        "width": 400,
                        "height": 405
                    },
                    "action": {
                        "type": "uri",
                        "label": "網址",
                        "uri": "https://ithelp.ithome.com.tw/users/20106865/ironman/2732"
                    }
                },
                {
                    "bounds": {
                        "x": 800,
                        "y": 405,
                        "width": 400,
                        "height": 405
                    },
                    "action": {
                        "type": "postback",
                        "label": "選單2",
                        "data": "action=changeMenu2"
                    }
                }
            ]
        }
    )
    
rich_menu_list = line_bot_api.get_rich_menu_list()
print(len(rich_menu_list))

# createRichMenu()
 
