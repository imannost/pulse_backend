FROM python:3.11.7-slim
WORKDIR /pulse
COPY requirements.txt .

RUN apt-get update -y && apt-get install -y python3-pip 

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt 
COPY . .

EXPOSE 8080
CMD ["python3", "main.py", "--port 8080"]