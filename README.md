# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка. Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к у вас не доступа к БД, но можете свободно использовать код верстки или посмотреть как реализованы запросы БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрулников нашего банка.

## Как установить



Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```


## Как запустить проект

Для запуска сервера нужно открыть терминал и написать:

```
python manage.py runserver
```

Необходимо указать правильные значения настроек. Чтобы их указать нужно создать файл `.env`. В нем нужно будет создать переменные:

```
DB_HOST='хост бд'
DB_PORT='порт на котором распологается бд'
DB_NAME='название бд'
DB_USER='имя админа'
DB_PASSWORD='пароль админа'
DB_SECRET_KEY = ''
DB_DEBUG = 'False или True для отображения или скрытия ошибок'
DB_ALLOWED_HOSTS = ['разрешенные хосты на которых может отображаться сайт']

```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).