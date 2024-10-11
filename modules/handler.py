try:
    import os
    import requests
    from dotenv import load_dotenv
    from modules.logger.log import logger
except ImportError:
    print("Ошибка импорта библиотеки в файле handler.py")


class SendMsgToGPT():
    
    def send_msg(self, message: str) -> str:
        """Функция для отправки текста пользователя в GhatGPT

        Args:
            message (str): Сообщение полученное от пользователя

        Returns:
            str: Результат ответа ChatGPT
        """
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = 'https://api.openai.com/v1/chat/completions'
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': message}]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
        except Exception as e:
            print(f"Ошибка отправки сообщения {e}")
            logger.error(f"Ошибка отправки сообщения {e}")
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['choices'][0]['message']['content']
        else:
            logger.error(f"Ошибка обработки запроса: {response.text}")
            return f"Ошибка обработки запроса: {response.text}"
            