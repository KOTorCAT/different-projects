import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .gigachat_client import gigachat_client

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def item_detail(request, item_id):
    return render(request, 'myapp/item_detail.html', {'item_id': item_id})

def chat_view(request):
    """Страница чата со Шреком"""
    return render(request, 'myapp/chat.html')

@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    """API для общения со Шреком через GigaChat"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': 'Сообщение не может быть пустым'}, status=400)
        
        # Получаем историю из сессии
        conversation_history = request.session.get('chat_history', [])
        
        # Отправляем запрос к GigaChat
        shrek_reply = gigachat_client.send_message(user_message, conversation_history)
        
        # Очищаем ответ от лишнего
        shrek_reply = shrek_reply.replace('Шрек:', '').replace('шрек:', '').strip()
        shrek_reply = shrek_reply.replace('Shrek:', '').replace('shrek:', '').strip()
        
        # Сохраняем историю
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": shrek_reply})
        
        # Храним только последние 20 сообщений
        request.session['chat_history'] = conversation_history[-20:]
        
        return JsonResponse({'reply': shrek_reply})
        
    except Exception as e:
        return JsonResponse({'error': f'Ошибка: {str(e)}'}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def clear_chat(request):
    """Очистка истории чата"""
    request.session['chat_history'] = []
    return JsonResponse({'status': 'ok'})