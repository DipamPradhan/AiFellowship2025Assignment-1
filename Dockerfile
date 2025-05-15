
FROM python:3.10-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY ./moviefinder ./moviefinder

EXPOSE 6551

CMD ["uvicorn", "moviefinder.app:app", "--host", "0.0.0.0", "--port", "6551"]
