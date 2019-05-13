#!/usr/bin/env bash
set -x

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

APIURL=${APIURL:-http://localhost:8000/api}
USERNAME=${ATHENA_ADMIN_USERNAME:-admin}
PASSWORD=${ATHENA_ADMIN_PASSWORD:-admin}

npx newman run ${SCRIPTDIR}/Athena.postman_collection.json \
  --delay-request 500 \
  --global-var "apiUrl=$APIURL" \
  --global-var "admin_username=$USERNAME" \
  --global-var "admin_password=$PASSWORD" \

