import google.generativeai as genai
from config import GOOGLE_API_KEY
from PIL import Image
import io

class GeminiHandler:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.text_model = genai.GenerativeModel('gemini-pro')
        self.vision_model = genai.GenerativeModel('gemini-pro-vision')
        
    def chat(self, message, language="zh-TW"):
        try:
            response = self.text_model.generate_content(
                f"請用{language}回答: {message}"
            )
            return response.text
        except Exception as e:
            return f"抱歉,發生錯誤: {str(e)}"
            
    def analyze_image(self, image_bytes, prompt, language="zh-TW"):
        try:
            image = Image.open(io.BytesIO(image_bytes))
            response = self.vision_model.generate_content(
                [
                    f"請用{language}回答關於這張圖片的問題: {prompt}",
                    image
                ]
            )
            return response.text
        except Exception as e:
            return f"抱歉,圖片分析發生錯誤: {str(e)}"
