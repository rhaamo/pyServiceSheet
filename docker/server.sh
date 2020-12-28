#!/bin/bash -eux
python /app/manage.py collectstatic --noinput
python /app/manage.py migrate
cd /app
gunicorn --log-file=- --worker-tmp-dir /dev/shm config.asgi:application -w ${WEB_WORKERS-2} --threads ${WEB_THREADS-4} -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 ${GUNICORN_ARGS-}
