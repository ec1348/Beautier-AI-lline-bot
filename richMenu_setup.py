'''
設定line bot的圖文選單
'''


from linebot.exceptions import LineBotApiError
from linebot import LineBotApi
import requests
import os
from dotenv import dotenv_values
config = dotenv_values(".env")
# 設定圖文選單
richmenu_1 = {
    "size": {
        "width": 1200,
        "height": 810
    },
    "selected": True,
    "name": "richmenu-1",
            "chatBarText": "功能選單",
            "areas": [
                {
                    "bounds": {
                        "x": 0,
                        "y": 0,
                        "width": 400,
                        "height": 405
                    },
                    "action": {
                        "type": "postback",
                        "label": "item_rec",
                        "data": "func=item_rec",
                        "text": "商品推薦(待開發)"
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
                        "type": "postback",
                        "label": "風格選擇",
                        "data": "action=next"
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
                        "type": "uri",
                        "label": "Camera roll",
                        "uri": "line://nv/cameraRoll/single"
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
                        "type": "uri",
                        "label": "偏好設定",
                        "uri": "https://liff.line.me/1656234315-bpJYQaV8"
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
                        "type": "postback",
                        "label": "流行趨勢",
                        "data": "fun=trend",
                        "text": "流行趨勢(待開發)"
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
                        "type": "uri",
                        "label": "camera",
                        "uri": "line://nv/camera"
                    }
                }
    ]
}

richmenu_2 = {
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
                        "type": "postback",
                        "label": "sweet",
                        "data": "style=nature",
                        "text": "甜美風格"
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
                        "type": "postback",
                        "label": "work",
                        "data": "style=work",
                        "text": "職場魅力"
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
                        "label": "真的美",
                        "data": "feedback=good&action=prev",
                        "text": "我好漂亮"
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
                        "type": "postback",
                        "label": "smoke",
                        "data": "style=smoke",
                        "text": "煙燻搖滾"
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
                        "type": "postback",
                        "label": "club",
                        "data": "style=wild",
                        "text": "夜店風"
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
                        "label": "饒了我",
                        "data": "feedback=bad&action=prev",
                        "text": "饒了我吧，心美也是一種美。"
                    }
                }
    ]
}

class RichMenuService:

    line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

    @classmethod
    def createRichMenu(cls, richmenu_json):
        '''
        創建一個圖文選單,每隻機器人最多只能有1000個圖文選單
        :param richmenu_json: 設計好的圖文選單json格式
        '''
        requests.post(
            "https://api.line.me/v2/bot/richmenu",
            headers={
                "Authorization":  "Bearer " + config.get("LINE_CHANNEL_ACCESS_TOKEN"),
                "Content-Type": "application/json"
            },
            json=richmenu_json
        )

    @classmethod
    def setRichMenuPicture(cls, richMenuId, imagePath):
        '''
        創建完圖文選單後,設定圖文選單的圖片,尺寸要與設定時相同
        :param richMenuId: 圖文選單的ID
        :param imgaePath: 圖文選單圖片位置
        '''
        requests.post(
            "https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content",
            headers={
                "Authorization":  "Bearer " + config.get("LINE_CHANNEL_ACCESS_TOKEN"),
                "Content-Type": "image/png"
            },
        )
        with open(imagePath, 'rb') as f:
            cls.line_bot_api.set_rich_menu_image(richMenuId, "image/png", f)


line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))
# 讀取所有的圖文選單
rich_menu_list = line_bot_api.get_rich_menu_list()
# print(rich_menu_list[0].rich_menu_id)
# print(rich_menu_list[1].rich_menu_id)
# x = line_bot_api.get_default_rich_menu()
# print(x)

# 刪除圖文選單
line_bot_api.delete_rich_menu(rich_menu_list[0].rich_menu_id)
line_bot_api.delete_rich_menu(rich_menu_list[1].rich_menu_id)

# 新增圖文選單
RichMenuService.createRichMenu(richmenu_1)
RichMenuService.createRichMenu(richmenu_2)

#查詢新的圖文選單 
rich_menu_list = line_bot_api.get_rich_menu_list()

# 上傳圖穩選單照片
RichMenuService.setRichMenuPicture(rich_menu_list[0].rich_menu_id, "圖文選單_p1.png")
RichMenuService.setRichMenuPicture(rich_menu_list[1].rich_menu_id, "圖文選單_p2.png")

# 設定預設圖文選單
line_bot_api.set_default_rich_menu(rich_menu_list[0].rich_menu_id)

# 預設圖文選單id
print("第一張",rich_menu_list[0].rich_menu_id)
print("第二張",rich_menu_list[1].rich_menu_id)
print("預設圖文",line_bot_api.get_default_rich_menu())

# print("共有%d個圖文選單" % (len(rich_menu_list)),rich_menu_list[0].rich_menu_id, rich_menu_list[1].rich_menu_id)
# for i in range(0, len(rich_menu_list)-1, 1):
#     print("第%d個ID是: %s"% (i+1,rich_menu_list[i].rich_menu_id))
