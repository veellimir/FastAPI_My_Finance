FROM python:3.11

RUN mkdir /crm_finance

WORKDIR /crm_finance

COPY requirements.txt .

RUN pip install -upgrade pip
RUN pip install requirements.txt

COPY . .

RUN alembic upgrade head

RUN chmod a+x /crm_finance/docker/*.sh

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
