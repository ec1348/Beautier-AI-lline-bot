import os
from flask import Flask, request, abort
from flask_cors import CORS
import linebot
from linebot.models import actions
import requests
from io import BytesIO
app = Flask(__name__)
CORS(app)

# 使用 python-dotenv 套件取得環境變數 目的是要將存在.env檔的 LINE_CHANNEL_ACCESS_TOKEN,  LINE_CHANNEL_SECRET 讀取出來
from dotenv import dotenv_values
config = dotenv_values(".env")

# 新增 LinebotAPI 套件
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(config.get('LINE_CHANNEL_SECRET'))

# 建立日誌設定檔 log 
import logging
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.get('GOOGLE_APPLICATION_CREDENTIALS')

client = google.cloud.logging.Client()

bot_event_handler = CloudLoggingHandler(client, name="beautier_bot_log")
bot_event_logger = logging.getLogger("beautier_bot_log")
bot_event_logger.setLevel(logging.INFO)
bot_event_logger.addHandler(bot_event_handler)

# from linebot.models.rich_menu import (
#     RichMenu, RichMenuSize,RichMenuArea, RichMenuBounds
#     )
# from linebot.models.actions import(
#     CameraRollAction, CameraAction
# )
# import urllib.request
# from PIL import Image
# import numpy as np
# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=False,
#     name="Nice richmenu",
#     chat_bar_text="Tap here",
#     areas=[RichMenuArea(
#         bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#         action=CameraAction(type = "Camera", label = "Camera"))]
# )
# rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# print(rich_menu_id)

# urllib.request.urlretrieve(
#   'https://storage.googleapis.com/beautier-life-rich-menu/%E5%9C%96%E6%96%87%E9%81%B8%E5%96%AE_v1.png',
#    "richimage.png")
# img = Image.open("richimage.png")
# img = np.array(img)
# line_bot_api.set_rich_menu_image(rich_menu_id, content_type="image/png",content = img.all())
# line_bot_api.set_default_rich_menu(rich_menu_id)

@app.route("/")
def helloWorld():
    bot_event_logger.info("test")
    return "Hello"


'''
轉發功能列表
'''
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    bot_event_logger.info(body)
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))