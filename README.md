# Космический Инстаграм

Набор скриптов на питоне для скачивания фотографий SpaceX и Hubble и загрузки их в Instagram.

### Как запустить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для загрузки фотографий используются открытые API [SpaceX](https://github.com/r-spacex/SpaceX-API) и [Hubble](http://hubblesite.org/api/documentation).

```

Фотографии скачаются в папку `images`.

Для загрузки фотографий в Instagram зарегистрируйте аккаунт, создайте в папке проекта файл `.env` и запишите в него логин и пароль:
```
INSTAGRAM_LOGIN=ВАШ_ЛОГИН
INSTAGRAM_PSSWD=ВАШ_ПАРОЛЬ
```
Запустите

```
python publish_to_instagram.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
