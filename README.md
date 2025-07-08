## 🆘 fail
💊 Проблема на  ios с БД, создалась версия postgres с не правильной кодировкой (особенности ios)
    нужно установить правильную кодировку и локаль.
у меня есть проект Django с Базой Данных postgresql, в нем не работает title__icontains в скрипте:
Category.objects.filter(title__icontains=self.request.query_params.get('search', ''))
т.к. не правильный тип или локаль БД


(Cейчас: Collate С, Ctype С.
Нужно: Collate ru_RU.UTF-8, Ctype ru_RU.UTF-8)

что мне нужно:
    🆘 Изменить локаль БД

    1. Делаем дамп
`pg_dump -U hey_art_eq -h localhost -d edu_quest > dump.sql`

    2. Заходим в psql
    (захожу под именем владельца БД и подключаюсь к другой БД, тогда система отключится от нужной мне БД и позволит удалить мне ее )
`psql -U heyartem -d postgres -h localhost`

    3. Удаляем БД
`DROP DATABASE edu_quest;`

    4. Создаём новую БД:
`CREATE DATABASE edu_quest
  WITH
    OWNER = hey_art_eq
    ENCODING = 'UTF8'
    LC_COLLATE = 'ru_RU.UTF-8'
    LC_CTYPE = 'ru_RU.UTF-8'
    TEMPLATE = template0;`

    5. Восстанавливаем дамп
 `\q`
`psql -U hey_art_eq -d edu_quest -h localhost -f dump.sql`


Что сделал я: на 5 шаге, за место команды восстановить
`psql -U hey_art_eq -d edu_quest -h localhost -f dump.sql`

написал (сделать дамп повторно, чем перезаписал действующий дамп мой БД)
`pg_dump -U hey_art_eq -h localhost -d edu_quest > dump.sql`
