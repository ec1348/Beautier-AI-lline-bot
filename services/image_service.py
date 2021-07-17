'''
用戶上傳照片時，將照片從Line取回，放入CloudStorage
瀏覽用戶目前擁有多少張照片（未）
'''

from models.user import User
from flask import Request
from linebot import (
    LineBotApi
)

import os
from daos.user_dao import UserDAO
from linebot.models import (
    TextSendMessage, ImageSendMessage
)


# 圖片下載與上傳專用
import urllib.request
from google.cloud import storage


from dotenv import dotenv_values
config = dotenv_values(".env")

class ImageService:
    line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

    '''
    用戶上傳照片
    將照片取回
    將照片存入CloudStorage內
    '''
    @classmethod
    def line_user_upload_image(cls,event):

        # 取出照片
        image_blob = cls.line_bot_api.get_message_content(event.message.id)
        temp_file_path=f"""{event.message.id}.png"""

        #
        with open(temp_file_path, 'wb') as fd:
            for chunk in image_blob.iter_content():
                fd.write(chunk)

        # 上傳至bucket
        storage_client = storage.Client()
        bucket_name = os.environ['USER_INFO_GS_BUCKET_NAME']
        destination_blob_name = f'{event.source.user_id}/image/{event.message.id}.png'
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(temp_file_path)


        # run GAN model
        # os.system("pwd")
        os.system(f"python3 PSGAN-master/main.py --source_path {event.message.id}.png")

        # 儲存套完GAN model的照片到bucket
        temp_gan_file_path = f'{event.message.id}_psgan.png'
        destination_blob_name_gan = f'{event.source.user_id}/image/{event.message.id}_psgan.png'
        blob = bucket.blob(destination_blob_name_gan)
        blob.upload_from_filename(temp_gan_file_path)

        # 上傳至Imgur
        import pyimgur
        title = "Uploaded with PyImgur"
        im = pyimgur.Imgur(config.get('IMGUR_CLIENT_ID'))
        uploaded_image = im.upload_image(temp_gan_file_path, title=title)


        # 回覆變妝後的照片
        cls.line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url= uploaded_image.link, 
                preview_image_url= uploaded_image.link)
        )        
        # 移除本地照片
        os.remove(temp_file_path)
        os.remove(temp_gan_file_path)