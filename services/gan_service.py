'''
用戶選擇模擬妝容時，將照片CloudStorage取出來，進行gan模型處理
回傳給用戶，存回CloudStorage
'''

from linebot import (
    LineBotApi
)
from linebot.models import (
    ImageSendMessage, TextSendMessage
)
import os
from google.cloud import storage

from dotenv import dotenv_values
config = dotenv_values(".env")

class GanService:
    line_bot_api = LineBotApi(config.get('LINE_CHANNEL_ACCESS_TOKEN'))

    @classmethod
    def line_user_choose_style(cls, event, style):
        '''
        進行gan模型 work風格模擬
        回傳給使用者
        將照片存回雲端
        '''
        file_path = f'{event.source.user_id}_cache.png'
        cls.line_bot_api.push_message(event.source.user_id, TextSendMessage(text='妝容生成中...且慢!'))
        #Gan 模型套用 
        os.system(f"python3 PSGAN-master/main.py --source_path {file_path} --reference_dir PSGAN-master/assets/model_style/{style}")
        os.rename(f"{event.source.user_id}_cache_psgan.png",f'{event.timestamp}_psgan_{style}.png')
        temp_gan_file_path = f'{event.timestamp}_psgan_{style}.png'


        # 上傳至bucket
        storage_client = storage.Client()
        bucket_name = os.environ['USER_INFO_GS_BUCKET_NAME']
        destination_blob_name_gan = f'{event.source.user_id}/image/{event.timestamp}_psgan_{style}.png'
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name_gan)
        blob.upload_from_filename(temp_gan_file_path)

        # 上傳至Imgur
        try:
            import pyimgur
            title = "Uploaded with PyImgur"
            im = pyimgur.Imgur(config.get('IMGUR_CLIENT_ID'))
            uploaded_image = im.upload_image(temp_gan_file_path, title=title)
        except:
            cls.line_bot_api.push_message(event.source.user_id, TextSendMessage(text='imgur 壞掉了，再點選一次'))
            os.remove(temp_gan_file_path)


        try:
            # 回覆變妝後的照片
            cls.line_bot_api.reply_message(
                event.reply_token,
                [
                    ImageSendMessage(
                        original_content_url= uploaded_image.link, 
                        preview_image_url= uploaded_image.link
                        ),
                    TextSendMessage(
                        "請點選:真的美 or 饒了我，給予評價。並且返回上一頁。"
                        )
                ]
            )
        except:
            os.remove(temp_gan_file_path)
        os.remove(temp_gan_file_path)
        
