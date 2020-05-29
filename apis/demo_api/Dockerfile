FROM python:3.8.2-alpine3.11

ENV API_DIR /opt/api/
ENV PROJECT_ROOT $API_DIR/source/
ENV HOME /root

COPY requirements ./requirements/

# install requirements
RUN apk update && apk add --no-cache \
    # psycopg2
    postgresql-dev gcc python3-dev musl-dev \
# install requirements
    && pip install --upgrade pip setuptools \
    && pip install -r requirements/dev.txt \
# remove requirements
    && rm -r requirements

# copy project source
RUN mkdir -p $API_DIR/source/
COPY source $API_DIR/source/

COPY tests $API_DIR/tests/
COPY .coveragerc $API_DIR/
COPY pytest.ini $API_DIR/
RUN mkdir -p $API_DIR/reports

# copy scripts
COPY scripts $API_DIR/scripts/
COPY scripts /usr/bin

EXPOSE 5000
WORKDIR $PROJECT_ROOT
CMD ["run.sh"]