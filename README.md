## <a name="guides"></a> Инструкции

### <a name="launch-app"></a> Запуск приложения

 * Если вы хотите запустить приложение в продакшн, то не указывайте ваши environments в docker-compose, импользуйте переменные среды, или .env файл. В моем случае тестовые environments указаны в docker-compose для простоты запуска
 
 * Docker Compose

Находясь в папке с файлом `docker-compose.yml` выполнить в терминале:

	docker-compose up

### <a name="launch-app"></a> Запуск тестов

Находясь в контейнере апишки выполнить в терминале:

	python manage.py test


#URLS 

* 0.0.0.0:8000/api/file - загрузить файл
* 0.0.0.0:8000/api/file/info - метаинформация по файлам
* 0.0.0.0:8000/api/file/<mark>id</mark>/download - скачать файл
(id - вводите сами)
