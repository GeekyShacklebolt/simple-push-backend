### 19th Aug

* Add celery tasks to make webpush request to all subscribers in background
* Read settings env variable from .env file
* Added WebPushClient class that wraps `pywebpush` library to make webpush requests

### 13th Aug, 2022

* Added endpoint for subscription creation API
* Spawned up subscriptions app

### 12th Aug, 2022

* Added placeholder endpoint for notification creation API
* Spawned up notifications app
* Added initial docker and docker-compose setup including `Django`, `Celery`, `RabbitMQ`, `Postgres`.
* Spawned up the repository