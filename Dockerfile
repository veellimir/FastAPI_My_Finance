FROM python:3.10

RUN apt-get update && apt-get install -y postgresql-client

RUN mkdir /crm_finance

WORKDIR /crm_finance

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /crm_finance/wait-for-db.sh


CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
