FROM debian:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod -R 755 /app/*

EXPOSE 8000

USER 2000

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]