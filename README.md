# Beautier-AI-lline-bot
This is a line bot make people more beautiful
\n
第一步: 打開GCP console terminal\n
執行 "git clone https://github.com/ec1348/Beautier-AI-lline-bot.git"\n
案授權\n
\n
第二步: 更改操作路徑\n
先執行 "cd Beautier-AI-lline-bot"\n
在執行 "gcloud config set project beautier-life-319105"\n
這個步驟需要我開放 IAM 授權，要將你的E-mail寄給我開放授權\n
\n
第三步: 解壓縮 ngrok\n
執行 "unzip ngrok-stable-linux-amd64.zip"\n
\n
第四步: 安裝套件\n
執行 "pip3 install -r requirements.txt"\n
\n
第五步: 設定環境.env檔\n
這個步驟需要跟我拿取 .env 檔案，上傳到 Beautier-AI-lline-bot 路徑裡\n
\n
第六步: 啟用ngrok\n
執行"./ngrok http 8080"\n
把https的網址貼上lineBot的webhook\n
\n
第七步: 啟動應用\n
開啟新的terminal\n
先執行 "cd Beautier-AI-lline-bot"\n
再執行 "gcloud config set project beautier-life-319105"\n
再執行 "python3 app.py"\n
\n
完成\n

