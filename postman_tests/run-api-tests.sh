#!/usr/bin/env bash
set -x

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

APIURL=${APIURL:-https://localhost:8000/api}

npx newman run $SCRIPTDIR/Athena.postman_collection.json \
  --delay-request 500 \
  --global-var "APIURL=$APIURL" \
