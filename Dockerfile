FROM python:3.6

RUN mkdir -p /app/
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt
COPY main.py gilipollas_bot.txt ./

CMD python main.py