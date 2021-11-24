FROM python:3.9.4

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /WorldofGames

COPY . /WorldofGames

CMD ["python", "MainScores.py"]