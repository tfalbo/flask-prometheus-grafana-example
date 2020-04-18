# python:alpine is 3.{latest}
FROM python:alpine 

COPY src /src/

RUN pip install -r src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
