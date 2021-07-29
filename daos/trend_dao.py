'''
與db溝通
將流行趨勢的data 存入firestore
根據傳入風格 讀取流行趨勢資料
'''

from google.cloud import firestore

class TrendDao:
    # 建立客戶端
    db = firestore.Client()
    @classmethod
    def save_trend(cls):
        # (未)
        return 'Ok'
    

    '''
    輸入風格
    回傳風格流行趨勢data 
    List 格式
    '''
    @classmethod
    def get_trend(cls, style):
        trend_data = []
        docs = cls.db.collection(u'trend').where(u'style', u'==', style).stream()
        for doc in docs:
            trend_data.append(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
        return trend_data