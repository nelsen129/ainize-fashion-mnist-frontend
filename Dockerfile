FROM python:3.9.12

WORKDIR /app

RUN pip install requests streamlit tensorflow Pillow

COPY . .

CMD ["streamlit", "run", "app.py"]
