import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

TOKEN = 'vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA'

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)


def send_message(chat_id, text):
    random_id = random.randint(0, 100000000)
    vk.method('messages.send', {'chat_id': chat_id, 'message': text, 'random_id': random_id})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                bad_words = ['сука', 'блять']
                msg = event.text
                chat_id = event.chat_id
                if msg in bad_words:
                    send_message(chat_id, 'пошол на хуй')
                else:
                    send_message(chat_id, msg)

