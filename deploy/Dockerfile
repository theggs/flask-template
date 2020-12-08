FROM python:3.7-alpine

RUN pip install pip -U -i https://mirrors.aliyun.com/pypi/simple/ && pip config set global.index-url  https://mirrors.aliyun.com/pypi/simple/

COPY src/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY src /app

WORKDIR /app

CMD ["gunicorn", "wsgi", "-w 1","--bind=0.0.0.0:5000", "--access-logfile=-", "--error-logfile=-"]
