FROM python:3.6-slim
LABEL maintainer "Antoine Dao <antoinedao1@gmail.com>"

WORKDIR app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "start_docker"]
