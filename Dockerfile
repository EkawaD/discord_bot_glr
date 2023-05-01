FROM python:3.9

WORKDIR /bot

COPY ./bot/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./bot .

CMD ["python", "main.py"]