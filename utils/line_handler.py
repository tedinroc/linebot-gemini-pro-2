from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent, ImageMessageContent
from config import LINE_CHANNEL_ACCESS_TOKEN

class LineHandler:
    def __init__(self):
        configuration = Configuration(
            access_token=LINE_CHANNEL_ACCESS_TOKEN
        )
        self.client = ApiClient(configuration)
        self.messaging_api = MessagingApi(self.client)

    def reply_message(self, reply_token, messages):
        if not isinstance(messages, (list, tuple)):
            messages = [messages]
            
        response = self.messaging_api.reply_message(
            ReplyMessageRequest(
                reply_token=reply_token,
                messages=[TextMessage(text=message) for message in messages]
            )
        )
        return response
