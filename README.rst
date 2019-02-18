Quickstart
----------

You need poetry_ installed on your machine to bootstrap environment.

.. _poetry: https://github.com/sdispater/poetry

Rename ``.env.example`` to ``.env`` and change values if need.

``Makefile`` contains all necessary commands to start application::

    bootstrap-environment  - create virtualenv and install dependencies
    makemigrations         - create migrations using project django
    reformat               - remove unused import and format code with black
    migrate                - run db migrations using project django
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
