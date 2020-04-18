# python:alpine is 3.{latest}
FROM python:alpine
RUN apk add python3-dev build-base linux-headers pcre-dev

COPY src /src/

RUN pip install -r src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:5000", "--wsgi-file", "src/app.py", "--callable", "app_dispatch"]
