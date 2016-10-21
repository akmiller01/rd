# start with a base image
FROM django:1.10.2-python2
MAINTAINER alex <Alex Miller, alex.k.miller@gmail.com>

RUN mkdir /src
ADD ./ /src

WORKDIR /src
# install dependencies
RUN apt-get update
RUN pip install -r requirements.txt

CMD gunicorn -w 2 -b 0.0.0.0:80 rd.wsgi
