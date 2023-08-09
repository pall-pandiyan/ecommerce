FROM python:3.11
ENV PROJECT_DIR=/app
ENV DOCKER_OVERRIDE=1

WORKDIR ${PROJECT_DIR}
COPY . .

RUN pip --no-cache-dir install -U pip && \
    pip --no-cache-dir install -r requirements.txt

CMD ${PROJECT_DIR}/entrypoint.sh
 
