FROM python:3.9.12

WORKDIR /app

RUN pip install requests streamlit

COPY . .

CMD ["streamlit", "run", "app.py"]
