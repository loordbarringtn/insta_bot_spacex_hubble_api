# Космический Инстаграм

Проект создан  на языке __Питон__ для публикации фото, взятых из открытых данных __SpaceX__ и __Hubble__ в __Instagram__.

* __fetch_spacex.py__ - скачивает фотографии с последнего запуска __SpaceX__.
* __fetch_hubble.py__ - скачивает фотографии, сделанные телескопом __Hubble__.
* __upload_images.py__ - загружает скаченные фотографии в аккаунт __Instagram__.

Для загрузки фотографий используются открытые API [SpaceX](https://github.com/r-spacex/SpaceX-API) и [Hubble](http://hubblesite.org/api/documentation).

## Как запустить

__Python3__ должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для загрузки фотографий в Instagram зарегистрируйте аккаунт, создайте в папке проекта файл `.env` и 
запишите в него логин и пароль:
```
username=Ваш логин
password=Ваш пароль

```
### Запуск

Запуск скрипта происходит следующим образом:

```
python publish_to_instagram.py
```
Фотографии сначала скачиваются в папку `images`. Далее происходит ресайз картинок и обработанные файлы сохраняются
в папку `processed_images`. 

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/) .
