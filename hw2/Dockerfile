FROM python:3.10-slim

RUN apt-get update -y && apt-get install -y iputils-ping

COPY mtu_script.py .

ENTRYPOINT ["python3", "mtu_script.py"]