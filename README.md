# GLBot2 - Gemini Line Bot Assistant

這是一個基於 Google Gemini 2.0 API 開發的 Line 聊天機器人，具備以下功能：

- 智慧對話：使用 Gemini-Pro 模型進行自然語言對話
- 圖片分析：使用 Gemini-Pro-Vision 模型分析圖片內容
- 多語言支援：自動使用用戶的語言進行回應

## 本地開發

### 使用前準備

1. LINE Developers 設定：
   - 前往 [LINE Developers Console](https://developers.line.biz/)
   - 建立新的 Provider 和 Channel
   - 取得 Channel Secret 和 Channel Access Token
   - 設定 Webhook URL (部署後設定)

2. Google API 設定：
   - 前往 [Google AI Studio](https://makersuite.google.com/app/apikey)
   - 建立新的 API 金鑰

### 安裝步驟

1. 克隆專案：
   ```bash
   git clone https://github.com/你的用戶名/GLBot2.git
   cd GLBot2
   ```

2. 建立虛擬環境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   .\venv\Scripts\activate  # Windows
   ```

3. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```

4. 設定環境變數：
   - 複製 `.env.example` 為 `.env`
   - 填入您的 LINE Channel Secret 和 Channel Access Token
   - 填入您的 Google API Key

5. 啟動服務：
   ```bash
   python app.py
   ```

6. 使用 ngrok 設定 HTTPS 網址（本地開發用）：
   ```bash
   ngrok http 5000
   ```

## 雲端部署

### Heroku 部署

1. 安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

2. 登入 Heroku：
   ```bash
   heroku login
   ```

3. 建立 Heroku 應用：
   ```bash
   heroku create 你的應用名稱
   ```

4. 設定環境變數：
   ```bash
   heroku config:set LINE_CHANNEL_SECRET=你的LINE_CHANNEL_SECRET
   heroku config:set LINE_CHANNEL_ACCESS_TOKEN=你的LINE_CHANNEL_ACCESS_TOKEN
   heroku config:set GOOGLE_API_KEY=你的GOOGLE_API_KEY
   ```

5. 部署程式：
   ```bash
   git push heroku main
   ```

6. 在 LINE Developers Console 設定 Webhook URL：
   - 網址格式：https://你的應用名稱.herokuapp.com/callback

### Railway 部署

1. 在 [Railway](https://railway.app/) 建立新專案

2. 連結 GitHub 倉庫

3. 設定環境變數：
   - `LINE_CHANNEL_SECRET`
   - `LINE_CHANNEL_ACCESS_TOKEN`
   - `GOOGLE_API_KEY`

4. 部署會自動開始

5. 在 LINE Developers Console 設定 Webhook URL：
   - 網址格式：https://你的應用名稱.railway.app/callback

## 專案結構

```
GLBot2/
├── README.md                # 專案說明文件
├── requirements.txt         # 專案依賴套件
├── runtime.txt             # Python 版本設定
├── Procfile               # Heroku 部署設定
├── .env                   # 環境變數設定檔
├── .env.example          # 環境變數範例
├── .gitignore            # Git 忽略檔案設定
├── config.py             # 設定檔
├── app.py                # 主程式
└── utils/
    ├── __init__.py
    ├── gemini_handler.py # Gemini API 處理模組
    └── line_handler.py   # Line 訊息處理模組
```

## 注意事項

- 請確保您有足夠的 API 額度
- 建議在正式環境使用 HTTPS
- 圖片大小建議不要超過 10MB
- 請勿將敏感資訊（如 API 金鑰）提交到 Git 倉庫
