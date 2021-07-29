'''
與db溝通
將商品推薦的data 存入firestore
根據傳入風格 讀取流行趨勢資料
'''

from google.cloud import firestore

class ItemDao:
    # 建立客戶端
    db = firestore.Client()
    @classmethod
    def save_trend(cls):
        # (未)
        return 'Ok'
    

    '''
    輸入風格
    回傳風格商品推薦data 
    List 格式
    '''
    @classmethod
    def get_item(cls, style):
        items_data = []
        docs = cls.db.collection(u'items').where(u'style', u'==', style).stream()
        for doc in docs:
            items_data.append(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
        return items_data