import vk_api
import random
import wikipedia


class VKBot:
    def __init__(self, token):
        self.token = token
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
        self.longpoll = vk_api.bot_longpoll.VkBotLongPoll(self.vk_session, group_id)

    def run(self):
        for event in self.longpoll.listen():
            if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
                self.on_message(event)

    def on_message(self, event):
        message = event.obj.message['text']
        user_id = event.obj.message['from_id']
        peer_id = event.obj.message['peer_id']

        if message.lower() == 'привет':
            self.send_message(peer_id, f'Привет, пользователь! Что ты хочешь узнать?')
        elif message.lower() == 'пока':
            self.send_message(peer_id, f'Пока, пользователь!')
        else:
            try:
                summary = wikipedia.summary(message)
                self.send_message(peer_id, summary)
                self.send_message(peer_id, f'Что еще ты хочешь узнать?')
            except wikipedia.exceptions.DisambiguationError as e:
                options = '\n'.join(e.options)
                self.send_message(peer_id, f'Уточни, о чем именно ты хочешь узнать:\n{options}')

    def send_message(self, peer_id, message):

        self.vk.messages.send(
            peer_id=peer_id,
            message=message,
            random_id=random.randint(0, 2 ** 64)
        )


if __name__ == '__main__':
    token = 'ваш_токен'
    group_id = 'ваш_идентификатор_сообщества'
    bot = VKBot(token)
    bot.run()
