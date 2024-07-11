FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use Gunicorn to run the Flask app and bind it to the $PORT environment variable
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "app:app"]
EXPOSE 5000
