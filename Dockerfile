FROM pnelsen129/fashion-mnist:1

WORKDIR /app

RUN pip install requests streamlit

COPY . /app

CMD ["python3", "app.py"]
