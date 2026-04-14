import requests
import uuid
import json
from datetime import datetime, timedelta
from django.conf import settings

class GigaChatClient:
    """Клиент для работы с GigaChat API"""
    
    def __init__(self):
        self.api_key = settings.GIGACHAT_API_KEY
        self.base_url = "https://gigachat.devices.sberbank.ru/api/v1"
        self.auth_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        self.access_token = None
        self.token_expires_at = None
    
    def _get_access_token(self):
        """Получение токена доступа"""
        if self.access_token and self.token_expires_at > datetime.now():
            return self.access_token
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'RqUID': str(uuid.uuid4()),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            'scope': settings.GIGACHAT_SCOPE
        }
        
        response = requests.post(self.auth_url, headers=headers, data=data, verify=False)
        
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data['access_token']
            # Токен живет 30 минут
            self.token_expires_at = datetime.now() + timedelta(seconds=token_data.get('expires_in', 1800))
            return self.access_token
        else:
            raise Exception(f"Ошибка получения токена: {response.text}")
    
    def send_message(self, user_message, conversation_history=None):
        """Отправка сообщения Шреку"""
        try:
            token = self._get_access_token()
            
            url = f"{self.base_url}/chat/completions"
            
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            # Системный промпт для Шрека
            system_prompt = """Ты — Шрек из вселенной DreamWorks. Ты большой зеленый огр, который живет в болоте.

Твои черты характера:
- Грубоватый, но с добрым сердцем
- Любишь одиночество и тишину в своем болоте
- Говоришь прямо, без лишних слов, по делу
- Используешь метафоры про болото, луковицу, ослов
- Мудрый и философский, но с юмором
- Немного ворчливый, но справедливый

Твои любимые фразы на русском:
- "Огры как луковицы. У нас есть слои."
- "Что ты делаешь в моем болоте?"
- "Вали из моего болота!"
- "Осел! Заткнись."
- "Я — ОГР!"

Правила общения:
- Отвечай КРАТКО (максимум 2-3 предложения)
- Используй РУССКИЙ язык
- Будь харизматичным и немного ворчливым
- Используй простой, грубоватый язык
- Никогда не ломай характер — ты всегда Шрек
- Обращайся к пользователю на "ты"
- Добавляй немного болотного юмора

Сейчас к тебе в болото пришел гость. Ответь ему как настоящий огр, по-русски, кратко и с характером."""
            
            # Формируем список сообщений
            messages = [{"role": "system", "content": system_prompt}]
            
            # Добавляем историю диалога (если есть)
            if conversation_history:
                for msg in conversation_history[-10:]:  # Последние 10 сообщений
                    messages.append(msg)
            
            # Добавляем текущее сообщение пользователя
            messages.append({"role": "user", "content": user_message})
            
            payload = {
                "model": "GigaChat-2-Pro",
                "messages": messages,
                "temperature": 0.8,
                "top_p": 0.9,
                "max_tokens": 500,
                "stream": False,
                "repetition_penalty": 1.1
            }
            
            response = requests.post(url, headers=headers, json=payload, verify=False)
            
            if response.status_code == 200:
                result = response.json()
                reply = result['choices'][0]['message']['content']
                # Очищаем ответ от лишнего
                reply = reply.replace('Шрек:', '').replace('шрек:', '').strip()
                return reply
            else:
                return f"Извини, болото сегодня не на связи. Ошибка: {response.status_code}"
                
        except Exception as e:
            return f"Что-то пошло не так... {str(e)}"

# Создаем глобальный экземпляр клиента
gigachat_client = GigaChatClient()