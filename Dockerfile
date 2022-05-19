FROM python:3.8.2

WORKDIR /var/www/

RUN git clone https://github.com/oswaldeff/tasty2b9.git

WORKDIR /var/www/

RUN python -m pip install --upgrade pip

RUN pip3 install -r tasty2b9/requirements/deploy.txt

RUN pip3 install gunicorn

WORKDIR /var/www/tasty2b9

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

RUN . ~/.nvm/nvm.sh && nvm install node

RUN npm install

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]