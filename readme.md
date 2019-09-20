## Application to collect twitter feeds against a certain keyword

This project will require [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) 
and [docker-compose](https://docs.docker.com/compose/install/) respectively to run.

Clone the project in your directory and from the project directory run the following command:
``docker-compose up --build``

After the successful build and run you can go to your local ``0.0.0.0:8001/docs/`` to view the 
project documentation which will contain all the APIs for consumption.

``http://0.0.0.0:8001/feed/ GET`` Will enable you to see the list of all tweets collected against 
the query search words provided.

``http://0.0.0.0:8001/feed/enable/ POST`` will take a query word as an input and tweets against 
that word will be collected and stored

``http://0.0.0.0:8001/feed/disable/ POST`` will take a query word as an input and tweets against 
that word will no longer be collected and stored.