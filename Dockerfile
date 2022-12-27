FROM mcr.microsoft.com/playwright/python:v1.29.0-focal
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
COPY . .                                 
CMD ["flask", "run"]