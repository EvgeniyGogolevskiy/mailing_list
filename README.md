# mailing_list
Для начала установите зависимости pip install -r requirements

В настройках проекта (файле settings.py) установите следующие переменные:
  SECRET_KEY - секретный ключ
  REDIS_HOST - хост редис (127.0.0.1 если он установлен на машине, либо 0.0.0.1 если поднят в докере)
  REDIS_PORT - порт редис (по умолчанию 6379)
  EMAIL_HOST_USER - емэйл отправителя
  EMAIL_HOST_PASSWORD - пароль отправителя
  
Создайте и проведите миграции, наполните базу данных подписчиками

В одном терминале запустите сервер python manage.py runserver

В другом терминале запустите celery celery -A mailing_list_project worker -l info
