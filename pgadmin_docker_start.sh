#!/bin/bash
podman run -p 5050:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=admin@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=admin' \
    -v pgadmin:/var/lib/pgadmin \
    --name pgadmin4 \
    -d dpage/pgadmin4
