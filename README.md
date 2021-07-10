# Beautier-AI-lline-bot
This is a line bot make people more beautiful

* 第一步: 打開GCP console terminal  
執行 `git clone https://github.com/ec1348/Beautier-AI-lline-bot.git`  
案授權  
  
* 第二步: 更改操作路徑  
先執行 `cd Beautier-AI-lline-bot`  
在執行 `gcloud config set project beautier-life-319105`  
這個步驟需要我開放 IAM 授權，要將你的E-mail寄給我開放授權  
  
* 第三步: 解壓縮 ngrok  
執行 `unzip ngrok-stable-linux-amd64.zip`  
  
* 第四步: 安裝套件  
執行 `pip3 install -r requirements.txt`  
  
* 第五步: 設定環境.env檔  
這個步驟需要跟我拿取 .env 檔案，上傳到 Beautier-AI-lline-bot 路徑裡  
  
* 第六步: 啟用ngrok  
執行`./ngrok http 8080`  
把https的網址貼上lineBot的webhook  
  
* 第七步: 啟動應用  
開啟新的terminal  
先執行 `cd Beautier-AI-lline-bot`  
再執行 `gcloud config set project beautier-life-319105`  
再執行 `python3 app.py`  
  
* 完成  

