FROM python:3.8.6

WORKDIR /opt/demo/
COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

RUN python model.py

ENTRYPOINT python app.py