

  
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY . /app/app
RUN pip install fastapi uvicorn
RUN pip install requests
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]