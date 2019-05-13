.. |backend_master_build| image:: https://circleci.com/gh/ippolab/athena-backend/tree/master.svg?style=svg
    :target: https://circleci.com/gh/ippolab/athena-backend/tree/master

.. |backend_dev_build| image:: https://circleci.com/gh/ippolab/athena-backend/tree/dev.svg?style=svg
    :target: https://circleci.com/gh/ippolab/athena-backend/tree/dev

.. _poetry: https://github.com/sdispater/poetry
.. _docker: https://www.docker.com/get-started
.. _docker-compose: https://docs.docker.com/compose/install/
.. _localhost:8000: http://localhost:8000/
.. _postman: https://www.getpostman.com/downloads/


.. image:: https://img.shields.io/github/license/Naereen/StrapDown.js.svg
   :target: https://github.com/IppoLab/Athena-backend/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black


Build status
------------

+------------+------------------------+
|   BRANCH   | BUILD STATUS           |
+============+========================+
| master     | |backend_master_build| |
+------------+------------------------+
| dev        | |backend_dev_build|    |
+------------+------------------------+

Quickstart
----------

You need docker_ and docker-compose_ on your machine to start dev server without installing dev dependencies.
As you installed this tools and checked work, run following commands to start server on localhost:8000_:

.. code-block:: bash

    mv .env.example .env
    make compose-up

Requests will be available in ``postman_tests`` folder as postman_ collection. You can import file and test requests and
see responses from them.

Developers guide
----------------

You need poetry_ installed on your machine to bootstrap environment. Rename ``.env.example`` to ``.env`` and set
``DEBUG`` to `True`, then change other values if need. If you have your own postgres instance running on your machine,
then get ip and credentials and fill necessary variables in ``.env``. Or if you have docker_ and docker-compose_
you can run following commands to run postgres container and fill ``.env`` data for work:


.. code-block:: bash

    mv .env.example .env
    make startdb
    make dbip

Once you get ip of container with postgres write it into ``.env`` file. You can start app manually with poetry if you
have not entered into virtualenv or as usual if you've activated it.

First way is creating your own virtualenv and running app using ``virtualenv`` module:

.. code-block:: bash

    python -m virtualenv venv
    activate venv/bin/activate
    pip install poetry
    poetry install

Using this way you must always activate virtualenv to work with application.

Second way requires poetry_ installed local on your machine to install dependencies but you'll get possibility to use
simple commands from ``Makefile`` for work with application:

.. code-block:: bash

    make bootstrap-environment

Now you can use commands from ``Makefile commands`` section to work with app.

Makefile commands
-----------------

``Makefile`` contains all necessary commands to start application::

    bootstrap-environment  - create virtualenv and install dependencies
    makemigrations         - create migrations using project django
    reformat               - remove unused import and format code with black
    migrate                - run db migrations using project django
    tests                  - run tests with pytest
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
