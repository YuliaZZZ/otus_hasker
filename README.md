## Задание
### Hasker: Poor Man's Stackoverflow

*Задание*: Написать Q&A сайт, аналог stackoverflow.com. Это будет Django приложение, покрытое тестами и для которого (опционально) реализовано API

*Цель задания*: получить навык создания веб-приложений и использования фреймворков.

*Критерии успеха*: задание __обязательно__, критерием успеха является работающий согласно заданию код, который проходит тесты, для которого проверено соответствие pep8, написана минимальная документация с примерами запуска. Также проект должен разворачиваться одним из способов, описанных в секции Deploy. Далее успешность определяется code review.

### Основные сущности
1. Пользователь – электронная почта, никнейм, пароль, аватарка, дата регистрации.
2. Вопрос – заголовок, содержание, автор, дата создания, тэги.
3. Ответ – содержание, автор, дата написания, флаг правильного ответа.
4. Тэг — слово тэга.

### Основные страницы и формы
__Warning__: мокапы - это ориентир, если что-то противоречит здравому смыслу, то придерживайтесь здравого смысла.

#### 1. Index
Листинг вопросов с пагинацией по 20 штук на странице с сортировкой по дате добавления и рейтингу (2 вида сортировки). 

В шапке сайта находятся: 
* логотип
* поисковая строка (для быстрого поиска)
* кнопка задать вопрос (доступна только авторизованным). 

В правой части шапки — юзерблок. 
 * Для авторизованного пользователя юзерблок содержит его
     * ник, который ведет на страницу с профилем
     * аватарку
     * ссылки на “выход” 
 * Для неавторизованных
     * ссылки “войти” 
     * и “регистрация”. 

В правой колонке — информационный блок “Популярные вопросы” (описание ниже) и кнопка "Задать вопрос".
![index](https://dl.dropbox.com/s/udfcjzy9zbpnn5n/Index.png?dl=0)

#### 2. Ask Question 
Страница добавления вопроса (можно сделать оверлеем). Доступна только для авторизованных пользователей. 

В форма вводится
* заголовок
* текст вопроса
* тэги, через запятую. 

С вопросом может быть связано не более 3 тегов. Для подсказки при выборе тега можно использовать готовый jquery плагин. При обработке формы обязательно проверка валидности данных. Если вопрос успешно добавлен — пользователя перебрасывает на страницу вопроса, если возникли ошибки — их нужно отобразить в форме.
![ask](https://dl.dropbox.com/s/66cbwmeju1z2ovs/Ask%20question.png?dl=0)

#### 3. Answer question
Страница вопроса со списком ответов. На странице вопроса можно добавить ответ. 

Ответы сортируются по рейтингу и дате добавления при равном рейтинге. Ответы разбиваются по 30 штук на странице. 

Форма добавления ответа находится на странице вопроса. Отображается только для авторизованных пользователей. После добавления ответа, автор вопроса должен получить email с уведомление от новом ответе. В этом письме должна быть ссылка для перехода на страницу вопроса. Автор вопроса может пометить один из ответов как правильный. Пользователи могут голосовать за вопросы и ответы с помощью лайков «+» или «–». Один пользователь может голосовать за 1 вопрос и ответ только 1 раз, однаком может отменить свой выбор или переголосовать неограниченное число раз.
![ans](https://dl.dropbox.com/s/3u6j2jshu2l2i2k/Answer%20question.png?dl=0)

#### 4. Search question
Страница результатов поиска по вопросам. Состоит из поисковой строки и листинга вопросов. Сортировка — по рейтингу (дате если рейтинг одинаковый), чем выше рейтинг и свежее вопрос, тем он выше в результатах. Пагинация по 20 вопросов. Поиск идет одновременно по текстам вопросов и их заголовкам, но в списке только вопросы.
![search](https://dl.dropbox.com/s/hwx9alqj875hede/Search.png?dl=0)

#### 5. Search tag
Листинг вопросов по тэгу. На этой странице выводятся все вопросы содержащие некоторый тэг. Сортировка — по рейтингу (дате если рейтинг одинаковый), чем выше рейтинг и свежее вопрос, тем он выше в результатах. Пагинация по 20 вопросов. Пользователи попадают на эту страницу кликая по одному из тэгов в описании вопроса или набирая в строке поиска `tag:<имя тэга>`
![tag](https://dl.dropbox.com/s/l0irdqqk2gcbm9b/Search%20tag.png?dl=0)

#### 6. Sign Up
Страница регистрации. Любой пользователь может зарегистрироваться на сайте, заполнив форму с электронной почтой, никнеймом, аватаркой и паролем. Аватарка загружается на сервер и отображается рядом с вопросами и ответами пользователя.
![sign](https://dl.dropbox.com/s/pckn2vixenifudi/Sign%20Up.png?dl=0)

#### 7. Log In
Форма авторизации. Состоит из поля логин и пароль. Дополнительно есть ссылка на форму регистрации. При успешной авторизации пользователь
перебрасывается на исходную страницу, при неуспешной авторизации — ему показывается ошибка. Для авторизованных пользователей вместо этой формы должна показываться кнопка “Выйти”.
![log](https://dl.dropbox.com/s/f0qhvo2ba40t9g5/Log%20In.png?dl=0)

#### 8. User Settings
Страница пользователя содержит его настройки — email, nick и аватарку. Каждый пользователь может смотреть только свою страницу. У пользователя должна быть возможность изменить email и аватарку.
![set](https://dl.dropbox.com/s/e8r58gof51014mp/Settings.png?dl=0)

#### 9. Trending
В правой колонке сайте находится список из 20 наиболее популярных вопросов, т.е. вопросы с наивысшим рейтингом

### API
__Опциональное__ API создаем с помощью Django REST Framework. Что оно должно уметь:

* аутентификация: basic или jwt (лучше)
* получить index (аналогично корню сайта с пагинацией), trending
* сделать поисковый запрос
* получить вопрос
* получить ответы к вопросу

Что еще нужно:
* тесты
* swagger схема

Конкретная структура API выбирается самостоятельно на основании знаний, полученных на занятии.

### Stack
* Последняя CentOS или Ubuntu
* Nginx
* uWSGI
* Django
    * без сторонних app'ов
    * django-debug-toolbar можно
* PostgreSQL/MySQL
* Twitter Bootstrap
* Javascript, jQuery

### Deploy
На лекции мы обсуждали layout проекта на Django, в том числе там был Makefile. Проект должно уметь запускаться по команде make prod. Т.е. предполагается следующая последовательность действий:

1. создается контейнер с маппингом 80 порта контейнера на 8000 хоста: `docker run --rm -it -p 8000:80 /bin/bash`
2. клонируется ваш гит `git clone <ваш гит>`
3. заходим в директорию проекта cd hasker (именно такую директорию)
4. запускаем команду `make prod`, которая настроит все, что нужно, исходя из того, что у нас голый контейнер
	* установит нужные пакеты
	* запустит демоны

В итоге, на 8000 порту хоста должен открываться корень сайта.

В качестве альтернативы (и это был бы идеальный вариант), можно поднять своеобразный стейджинг пользуясь этой инструкцией https://simonwillison.net/2017/Oct/17/free-continuous-deployment/. Также может пригодится http://www.eidel.io/2017/07/10/dockerizing-django-uwsgi-postgres/ и http://p.agnihotry.com/post/the_free_stack_aws/.

Еще, может кому-то понадобится: https://ngrok.com/.


## Deadline
Проект должен быть сдан целиком через 3 недели. Нарушение делайна (пока) не карается, пытаться сдать ДЗ можно до конца курсы. Но код, отправленный с опозданием, когда по плану предполагается работа над более актуальным ДЗ, будет рассматриваться в более низком приоритете без гарантий по высокой скорости проверки

## Обратная связь
Cтудент коммитит все необходимое в свой github/gitlab репозитарий. Далее необходимо зайти в ЛК, найти занятие, ДЗ по которому выполнялось, нажать “Чат с преподавателем” и отправить ссылку. После этого ревью и общение на тему ДЗ будет происходить в рамках этого чата.