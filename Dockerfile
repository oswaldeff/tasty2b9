FROM node:17.4.0

FROM python:3.8.2

WORKDIR /var/www/

RUN git clone https://github.com/oswaldeff/tasty2b9.git

WORKDIR /var/www/

RUN python -m pip install --upgrade pip

RUN pip3 install -r tasty2b9/requirements/deploy.txt

RUN pip3 install gunicorn

RUN pip3 install npm

RUN apt-get -qq update
RUN apt-get -qq upgrade --yes 
RUN apt-get -qq install curl --yes
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get -qq install nodejs --yes

WORKDIR /var/www/tasty2b9

RUN rm package-lock.json

RUN npm install

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]