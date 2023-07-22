FROM python:3.10.12-bookworm


COPY . /app
WORKDIR /app
RUN pip3 install -r requirments.txt

ENTRYPOINT [ "python3", "app.py" ]
