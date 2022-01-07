FROM python:3.8-slim-buster
RUN apt update && apt install -y build-essential python3-dev ssh git apt-transport-https lsb-release ca-certificates && apt update
COPY . /tdp-collab-suites-service
WORKDIR /tdp-collab-suites-service
RUN pip install -r requirements.txt
ARG PORT=5000
ENV PORT_NUMBER=$PORT
EXPOSE $PORT_NUMBER
ARG DEBUG=False
ENV DEBUG_MODE=$DEBUG
ARG L2_CONFIG_PATH=config.ini
ENV L2_CONFIG_PATH=$L2_CONFIG_PATH
CMD python run.py -p $PORT_NUMBER -d $DEBUG_MODE
