FROM python:3.9.12

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py"]
