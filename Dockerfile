FROM python:3.6-alpine3.6

ENV INSTALL_DIR /opt/byewait
ENV PYTHONPATH /opt

RUN apk add --no-cache ca-certificates musl-dev gcc make openssl-dev curl-dev
ADD requirements.txt ${INSTALL_DIR}/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -Ur ${INSTALL_DIR}/requirements.txt
ADD byewait/ ${INSTALL_DIR}

EXPOSE 8888

ENV MYSQL_ENDPOINT localhost
ENV MYSQL_DATABASE byewait
ENV MYSQL_USER dev
ENV MYSQL_PASSWORD changeme
ENV MYSQL_PORT 3306

CMD python3 ${INSTALL_DIR}/src/app.py
