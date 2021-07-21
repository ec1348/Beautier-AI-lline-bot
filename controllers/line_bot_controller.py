'''
當用戶關注時，必須取用照片，並存放至指定bucket位置，而後生成User物件，存回db
當用戶取消關注時，
    從資料庫提取用戶數據，修改用戶的封鎖狀態後，存回資料庫
'''

from linebot import (
    LineBotApi, WebhookHandler
)
import os

# 載入Follow事件
from linebot.models.events import (
    FollowEvent, UnfollowEvent
)
from services.image_service import ImageService
from services.user_service import UserService
from services.gan_service import GanService
from services.rich_menu_service import richMenuService

from urllib.parse import parse_qs


class LineBotController:

    # 將消息交給用戶服務處理
    @classmethod
    def follow_event(cls, event):
        # print(event)
        UserService.line_user_follow(event)

    @classmethod
    def unfollow_event(cls, event):
        UserService.line_user_unfollow(event)

    # 未來可能會判斷用戶快取狀態
    # 現在暫時無
    @classmethod
    def handle_text_message(cls, event):

        return None

    # 用戶收到照片時的處理辦法
    @classmethod
    def handle_image_message(cls, event):
        ImageService.line_user_upload_image(event)
        return "OK"

    # 擷取event的data欄位，並依照function_name，丟入不同的方法
    @classmethod
    def handle_postback_event(cls, event):

        # query string 拆解 event.postback.data
        query_string_dict = parse_qs(event.postback.data)
        print(query_string_dict)
        # 擷取功能
        if query_string_dict.get('action'):
            if query_string_dict.get('action')[0] == 'next':
                print("dam same")
                richMenuService.click_next(event)
            else:
                print("go back")                
                richMenuService.click_prev(event)
        elif query_string_dict.get('style'):
            style = query_string_dict.get('style')[0]
            # Postbakc function 功能對應轉發
            GanService.line_user_choose_style(event, style)

        return 'ok'