FROM ubuntu
MAINTAINER sg
RUN apt update -y 
RUN apt install -y python3-pip python3-dev 
RUN mkdir /app
WORKDIR /app
ADD . ./
RUN pip3 install -r requirements.txt
expose 5000
RUN apt install curl -y
CMD ["python3", "./newapp.py"]
