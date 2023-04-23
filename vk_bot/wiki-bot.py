import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia

vk_session = vk_api.VkApi(token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
longpoll = VkLongPoll(vk_session)


def send_message(peer_id, message):
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()

        send_message(event.peer_id, 'Что вы хотите узнать?')

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                query = event.text.lower()

                try:
                    page = wikipedia.page(query)
                    summary = wikipedia.summary(query)
                    send_message(event.peer_id, summary)
                except:
                    send_message(event.peer_id,
                                 'Извините, я не смог найти информацию по вашему запросу')

                send_message(event.peer_id, 'Хотите узнать что-то еще? (Да/Нет)')

                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        answer = event.text.lower()

                        if answer == 'да':
                            break
                        else:
                            send_message(event.peer_id, 'Спасибо за обращение!')
                            break
