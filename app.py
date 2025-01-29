from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    ImageMessageContent
)
import os
import logging
from pythonjsonlogger import jsonlogger

from config import LINE_CHANNEL_SECRET
from utils.line_handler import LineHandler
from utils.gemini_handler import GeminiHandler

# 設定日誌
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

app = Flask(__name__)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
line_handler = LineHandler()
gemini_handler = GeminiHandler()

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        logger.error("Invalid signature error")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_text_message(event):
    try:
        user_message = event.message.text
        logger.info(f"Received text message: {user_message}")
        response = gemini_handler.chat(user_message)
        line_handler.reply_message(event.reply_token, response)
    except Exception as e:
        logger.error(f"Error handling text message: {str(e)}")
        line_handler.reply_message(event.reply_token, "抱歉,處理訊息時發生錯誤")

@handler.add(MessageEvent, message=ImageMessageContent)
def handle_image_message(event):
    try:
        message_content = line_handler.messaging_api.get_message_content(
            message_id=event.message.id
        )
        image_bytes = message_content.content
        
        # 預設提示詞
        prompt = "請描述這張圖片的內容"
        logger.info("Processing image analysis")
        response = gemini_handler.analyze_image(image_bytes, prompt)
        line_handler.reply_message(event.reply_token, response)
    except Exception as e:
        logger.error(f"Error handling image message: {str(e)}")
        line_handler.reply_message(event.reply_token, "抱歉,處理圖片時發生錯誤")

@app.route("/", methods=['GET'])
def health_check():
    return 'OK'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
