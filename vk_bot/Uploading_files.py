import json

import requests
import vk_api

# авторизация в ВКонтакте
TOKEN = 'vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA'
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
album_id = 292879866
group_id = vk.groups.getById()[0]['id']

# список файлов для загрузки
photos = ['image_1.jpg', 'image_2.jpg', 'image_3.jpg']


def writ_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_upload_server():
    r = requests.get('https://api.vk.com/method/photos.getUploadServer',
                     params={'access_token': TOKEN,
                             'album_id': album_id,
                             'group_id': group_id,
                             'v': 5.131}).json()
    writ_json(r, 'upload_server.json')


def main():
    upload_url = get_upload_server()

    file = {'file': open('image_1.jpg', 'rb')}

    upload_response = requests.post(upload_url, files=file).json()

    result = requests.get('https://api.vk.com/method/photos.save', params={'access_token': TOKEN,
                                                                           'album_id': album_id,
                                                                           'group_id': group_id,
                                                                           'server':
                                                                               upload_response[
                                                                                   'server'],
                                                                           'photos_list':
                                                                               upload_response[
                                                                                   'photos_list'],
                                                                           'hash': upload_response[
                                                                               'hash']})
    print(result)


if __name__ == '__main__':
    main()
