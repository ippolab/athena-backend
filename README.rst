Quickstart
----------

Rename ``.env.example`` to ``.env`` and change values if need.

``Makefile`` contains all necessary commands to start application::

    bootstrap-environment  - create virtualenv and install dependencies
    activate-environment   - enter in vrtialenv
    collectstatic          - collect static files for serving by nginx in docker
    startapp               - run django development server
    startdb                - start postgres in docker
    dbip                   - get postgres ip for local development
    compose-up             - start all services from compose config
    compose-up-rebuild     - rebuild image for `athena` and start compose
    compose-logs           - show compose logs
    compose-stop           - stop all running compose services
    compose-athena-connect - connect to athena container
    docker-dev             - build dev image for athena
    docker-master          - build image for athena with default tag
