FROM python:3.7
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y postgresql \
                       postgresql-contrib \
                       libpq-dev \
                       python3-dev
COPY . /var/www/ak
WORKDIR /var/www/ak
RUN python -m pip install -r requirements.txt
CMD python manage.py runserver
