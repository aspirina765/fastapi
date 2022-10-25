# # syntax = docker/dockerfile:1.4

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

# WORKDIR /app

# COPY requirements.txt ./
# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip install -r requirements.txt

# COPY ./app ./app

# FROM builder as dev-envs

# RUN <<EOF
# apt-get update
# apt-get install -y --no-install-recommends git
# EOF

# RUN <<EOF
# useradd -s /bin/bash -m vscode
# groupadd docker
# usermod -aG docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /

FROM datamechanics/spark:3.1-latest

# TODO retirar configurações de blob fuse ?

USER root

WORKDIR /opt/app

ENV PYSPARK_MAJOR_PYTHON_VERSION=3

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY app/ app/
RUN mkdir /tmp/blobfusecfg
COPY fuse_connection.cfg /tmp/blobfusecfg

RUN apt-get -y update \
    && apt-get install -y wget curl libcurl3-gnutls

RUN wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get -y update \
    && apt-get install -y blobfuse

RUN mkdir -p /mnt/blobfusetmp
RUN chown root /mnt/blobfusetmp

RUN mkdir /mnt/adls

#ENTRYPOINT ["python3"]
#CMD ["src/main.py"]



