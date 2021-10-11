FROM python:3.7

COPY requirements.txt ./requirements.txt
COPY price.py ./price.py
COPY main.py ./main.py

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]