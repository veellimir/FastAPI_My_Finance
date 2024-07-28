FROM python:3.10

RUN apt-get update && apt-get install -y postgresql-client

RUN mkdir /crm_finance

WORKDIR /crm_finance

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# Скопировать скрипт wait-for-it.sh в контейнер
COPY wait-for-it.sh /crm_finance/wait-for-it.sh

# Сделать скрипт исполняемым
RUN chmod +x /crm_finance/wait-for-it.sh

# Использовать wait-for-it.sh для ожидания готовности базы данных перед выполнением миграций Alembic
RUN #/crm_finance/wait-for-it.sh postgres:5432 -t 60 -- alembic upgrade head

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]



