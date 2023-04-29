import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = 'vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA'


# функция для получения следующего города
def get_next_city(city):
    last_letter = city[-1].lower()
    with open('cities.txt', 'r', encoding='utf-8') as f:
        cities = [line.strip() for line in f]
        for c in cities:
            if c[0].lower() == last_letter and c != city:
                return c
        return None


def send_message(chat_id, message):
    vk_session.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': 0})


# функция для обработки сообщений от пользователя
def handle_message(event, ):
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        chat_id = event.chat_id
        if 'привет' in message:
            send_message(chat_id, 'Привет! Давай поиграем в города!')
        elif 'город' in message:
            city = message.split(' ')[-1]
            with open('used_cities.txt', 'r') as f:
                used_cities = [line.strip() for line in f]
                if city in used_cities:
                    send_message(chat_id,
                                 f'Город "{city}" уже был использован. Попробуй другой.')
                else:
                    next_city = get_next_city(city)
                    if next_city is None:
                        send_message(chat_id,
                                     f'Я не знаю города на букву "{city[-1].lower()}". Ты выиграл!')
                        with open('used_cities.txt', 'w', encoding='utf-8') as f:
                            f.write('')
                            f.close()
                    else:
                        send_message(chat_id,
                                     f'"{next_city.capitalize()}"! Твой ход.')
                        with open('used_cities.txt', 'a', encoding='utf-8') as f:
                            f.write(city + '\n')
                            f.write(next_city + '\n')
        elif 'пока' in message:
            send_message(chat_id, 'Пока! Хорошей игры!')
            with open('used_cities.txt', 'w', encoding='utf-8') as f:
                f.write('')
                f.close()

        else:
            send_message(chat_id, 'Я не понимаю, о чем ты...')


# основной код
vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    handle_message(event)
