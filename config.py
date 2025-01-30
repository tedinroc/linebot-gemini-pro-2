import os
from dotenv import load_dotenv

load_dotenv()

def get_env_or_raise(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"環境變數 {key} 未設定。請在 Railway 的 Variables 中設定此變數。")
    return value

LINE_CHANNEL_SECRET = get_env_or_raise('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = get_env_or_raise('LINE_CHANNEL_ACCESS_TOKEN')
GOOGLE_API_KEY = get_env_or_raise('GOOGLE_API_KEY')
