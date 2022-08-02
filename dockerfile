FROM python:3.10-slim
WORKDIR /code
ENV FLASK_APP=run.py
RUN python3 -m pip install --upgrade pip setuptools
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD flask run -h 0.0.0.0 -p 80


