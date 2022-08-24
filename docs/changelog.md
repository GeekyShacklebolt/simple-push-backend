### 23rd Aug, 2022

* Refactored directory structure

### 22nd Aug, 2022

* Add API (`POST /api/notifications/:id/send`) to trigger web push notifications.

### 19th Aug, 2022

* Add API (`GET /api/notifications`) to fetch all available notifications from DB.
* Save/Create new notifications in DB using API (`POST /api/notifications`)
* Send push notification to all subscribers with the data directly received in API (`POST /api/notifications`)
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