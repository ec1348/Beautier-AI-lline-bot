'''
用戶選擇不同的風格趨勢
讀取firestore流行趨勢的資料
回傳給用戶輪播範本
'''
from linebot import LineBotApi
import os
from daos.trend_dao import TrendDao

from dotenv import dotenv_values
config = dotenv_values(".env")

from linebot.models import (
    TextSendMessage, CarouselTemplate, TemplateSendMessage
)
from linebot.models.actions import (
    MessageAction, URIAction
)
from linebot.models.template import (
    CarouselColumn
)

class TrendService:
    line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

    @classmethod
    def line_user_choose_style(cls, event, style):
        
        trend_data = TrendDao.get_trend(style)
        print(f'{style}風格: ',len(trend_data))

        '''
        根據firestore抓取的資料創建出相對數量的輪播範本
        '''
        
        # 準備空list 設定輪播範本內容
        columns = []
        for i in range(0, 6 , 1):
            pic_url = trend_data[i]["pic_url"]
            title = trend_data[i]["title"]
            content = trend_data[i]["content"]
            summary = trend_data[i]["summary"]
            summary_url = trend_data[i]["summary_url"]

            ''' 
            line bot限定title不能超過40個字
            message不能超過300字元
            設定title 超過時，取 0~30 字元後面補上"......" 
            設定message 超過時，取 0~290 字元後面補上"......"
            ''' 
            if len(title) >= 40 :
                title = title[0:30]+"......"
            if len(summary) >= 300:
                summary = summary[0:290] + "......"
            carousel_column=CarouselColumn(
                            thumbnail_image_url=pic_url,
                            title=title,
                            text=content,
                            actions=[
                                MessageAction(
                                    label="點我看摘要",
                                    text=summary
                                ),
                                URIAction(
                                    label="摘要原文",
                                    uri=summary_url
                                )
                            ]
                        )
            columns.append(carousel_column)
        
        # print(columns)

        '''
        設定輪播範本
        回傳給用戶
        '''
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=columns
            )
        )
        cls.line_bot_api.reply_message(event.reply_token,carousel_template_message)
