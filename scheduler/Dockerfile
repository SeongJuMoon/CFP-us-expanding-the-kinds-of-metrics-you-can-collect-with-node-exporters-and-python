FROM python3


COPY . /app
WORKDIR /app
RUN pip3 install -r requirments.txt

ENTRYPOINT [ "python3", "app.py" ]
