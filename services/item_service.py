'''
用戶選擇不同的風格
讀取firestore商品的資料
回傳給用戶自訂flex message 輪播範本
'''
from linebot import LineBotApi
import os
import json
from daos.item_dao import ItemDao

from dotenv import dotenv_values
config = dotenv_values(".env")

from linebot.models import (
    TextSendMessage, CarouselTemplate, FlexSendMessage
)
from linebot.models.actions import (
    MessageAction, URIAction
)
from linebot.models.template import (
    CarouselColumn
)

class ItemService:
    line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

    @classmethod
    def line_user_choose_style(cls, event, style):
        
        item_data = ItemDao.get_item(style)
        print(f'{style}風格: ',len(item_data))
        with open(f'/home/ec1348_666/Beautier-AI-lline-bot-cloud-run/others/FLEX_MESSAGE/{style}.json', "r") as a_file:
            data=json.load(a_file)
        '''
        根據firestore抓取的資料創建出相對數量的輪播範本
        '''
        
        # 準備空list 設定自定義flex message輪播範本內容
        # contens_list = []
        # for i in range(0, 10 , 1):
            # classification = item_data[i]["Classification"]
            # comment = item_data[i]["comment"]
            # pic_url = item_data[i]["pic_url"]
            # product_name_score = item_data[i]["product_name_score"]
            # product_url = item_data[i]["product_url"]

            # ''' 
            # line bot限定title不能超過40個字
            # message不能超過300字元
            # 設定title 超過時，取 0~30 字元後面補上"......" 
            # 設定message 超過時，取 0~290 字元後面補上"......"
            # ''' 
            # # if len(title) >= 40 :
            # #     title = title[0:30]+"......"
            # # if len(summary) >= 300:
            # #     summary = summary[0:290] + "......"
            # contents={
            #     "type": "bubble",
            #     "size": "micro",
            #     "hero": {
            #         "type": "image",
            #         "url": pic_url,
            #         "size": "full",
            #         "aspectMode": "cover",
            #         "aspectRatio": "320:213"
            #     },
            #     "body": {
            #         "type": "box",
            #         "layout": "vertical",
            #         "contents": [
            #             {
            #                 "type": "text",
            #                 "text": product_name_score,
            #                 "weight": "bold",
            #                 "size": "sm",
            #                 "wrap": True
            #             },
            #             {
            #                 "type": "box",
            #                 "layout": "baseline",
            #                 "contents": [
            #                     {
            #                         "type": "icon",
            #                         "size": "xs",
            #                         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            #                     },
            #                     {
            #                         "type": "icon",
            #                         "size": "xs",
            #                         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            #                     },
            #                     {
            #                         "type": "icon",
            #                         "size": "xs",
            #                         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            #                     },
            #                     {
            #                         "type": "icon",
            #                         "size": "xs",
            #                         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            #                     },
            #                     {
            #                         "type": "icon",
            #                         "size": "xs",
            #                         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
            #                     },
            #                     {
            #                         "type": "icon",
            #                         "size": "xs",
            #                         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
            #                     },
            #                     {
            #                         "type": "icon",
            #                         "size": "xs",
            #                         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
            #                     },
            #                     {
            #                         "type": "text",
            #                         "text": "4.0",
            #                         "size": "xs",
            #                         "color": "#8c8c8c",
            #                         "margin": "md",
            #                         "flex": 0
            #                     }
            #                 ]
            #             },
            #             {
            #                 "type": "box",
            #                 "layout": "vertical",
            #                 "contents": [
            #                     {
            #                         "type": "box",
            #                         "layout": "baseline",
            #                         "spacing": "sm",
            #                         "contents": [
            #                             {
            #                                 "type": "text",
            #                                 "text": comment,
            #                                 "wrap": True,
            #                                 "color": "#8c8c8c",
            #                                 "size": "xs",
            #                                 "flex": 5
            #                             }
            #                         ]
            #                     }
            #                 ]
            #             }
            #         ],
            #         "spacing": "sm",
            #         "paddingAll": "13px"
            #     },
            #     "footer": {
            #         "type": "box",
            #         "layout": "vertical",
            #         "contents": [
            #             {
            #                 "type": "button",
            #                 "action": {
            #                     "type": "uri",
            #                     "label": "\u5546\u54c1\u9023\u7d50",
            #                     "uri": product_url
            #                 },
            #                 "height": "sm",
            #                 "style": "link"
            #             }
            #         ]
            #     }
            # }
            # contens_list.append(contents)
        
        # print(columns)

        '''
        設定輪播範本
        回傳給用戶
        '''
        # flex_message = {
        #     "type": "carousel",
        #     "contents": contens_list
        # }
        cls.line_bot_api.reply_message(event.reply_token,FlexSendMessage( alt_text="item_rec",contents=data))
