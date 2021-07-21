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

#載入controllers
from controllers.line_bot_controller import LineBotController

# 載入Follow事件
from linebot.models.events import (
    FollowEvent,UnfollowEvent,MessageEvent,TextMessage,PostbackEvent,ImageMessage,AudioMessage,VideoMessage
)

# 建立日誌設定檔 log 
import logging
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler

# 本地端用金鑰環境設置
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.get('GOOGLE_APPLICATION_CREDENTIALS')

client = google.cloud.logging.Client()

bot_event_handler = CloudLoggingHandler(client, name="beautier_bot_log")
bot_event_logger = logging.getLogger("beautier_bot_log")
bot_event_logger.setLevel(logging.INFO)
bot_event_logger.addHandler(bot_event_handler)



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

@handler.add(FollowEvent)
def handle_line_follow(event):
    return LineBotController.follow_event(event)

@handler.add(UnfollowEvent)
def handle_line_unfollow(event):
    return LineBotController.unfollow_event(event)

@handler.add(MessageEvent,TextMessage)
def handle_line_text(event):
    return LineBotController.handle_text_message(event)

@handler.add(MessageEvent,ImageMessage)
def handle_line_image(event):
    return LineBotController.handle_image_message(event)

@handler.add(PostbackEvent)
def handle_postback_event(event):
    return LineBotController.handle_postback_event(event)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))