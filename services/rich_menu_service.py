'''
處理圖文選單的轉換
'''
from linebot import LineBotApi
import os
from dotenv import dotenv_values
config = dotenv_values(".env")

class richMenuService:
    line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

    @classmethod
    def click_next(cls, event):
        cls.line_bot_api.link_rich_menu_to_user(event.source.user_id, config.get("RICH_MENU_SEC_PAGE_ID"))
        return "ok"
    @classmethod
    def click_prev(cls, event):
        cls.line_bot_api.link_rich_menu_to_user(event.source.user_id, config.get("RICH_MENU_HOME_PAGE_ID"))
        return "ok"