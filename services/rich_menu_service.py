'''
處理圖文選單的換頁
'''
from linebot import LineBotApi
import os
from dotenv import dotenv_values
config = dotenv_values(".env")

from linebot.models import (
    TextSendMessage
)

class richMenuService:
    line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

    # 換成第2頁
    @classmethod
    def click_next(cls, event):
        # 判斷使用者是否上傳照片
        file_path = f'{event.source.user_id}_cache.png'
        if  os.path.isfile(file_path):
            print("User picture exits")
            cls.line_bot_api.link_rich_menu_to_user(event.source.user_id, config.get("RICH_MENU_SEC_PAGE_ID"))
            return "ok"           
        else:
            print("User picture does not exit")
            cls.line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("請上傳照片")
                )
            return 0
    
    # 換回首頁
    @classmethod
    def click_prev(cls, event):
        cls.line_bot_api.link_rich_menu_to_user(event.source.user_id, config.get("RICH_MENU_HOME_PAGE_ID"))
        return "ok"
    
    # 換成第3頁
    @classmethod
    def click_third(cls, event):
        cls.line_bot_api.link_rich_menu_to_user(event.source.user_id, config.get("RICH_MENU_THIRD_PAGE_ID"))
        return "ok"
 
    # 換成第4頁
    @classmethod
    def click_forth(cls, event):
        cls.line_bot_api.link_rich_menu_to_user(event.source.user_id, config.get("RICH_MENU_FORTH_PAGE_ID"))
        return "ok"