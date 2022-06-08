FROM python:3.7-alpine
LABEL author="Krzewski Michal"
WORKDIR /code
ENV FLASK_APP=app.py
RUN apk add --no-cache gcc musl-dev linux-headers
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./src .
CMD ["flask", "run", "--host=0.0.0.0"]