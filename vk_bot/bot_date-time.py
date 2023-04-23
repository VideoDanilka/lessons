import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import datetime

vk_session = vk_api.VkApi(
    token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
longpoll = VkLongPoll(vk_session)


def send_message(chat_id, message):
    vk_session.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        chat_id = event.chat_id
        if 'время' in message or 'число' in message or 'дата' in message or 'день' in message:
            now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))

            response = f"Сегодня {now.strftime('%d.%m.%Y')}\nТекущее время: {now.strftime('%H:%M:%S')}\nДень недели: {now.strftime('%A')}"

            send_message(chat_id, response)
        else:
            send_message(chat_id,
                         "Я могу сообщить текущую дату, время и день недели. Просто напиши 'время', 'число', 'дата' или 'день'")
