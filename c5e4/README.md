# Exercise #1: potato salad docker-compose

This exercise builds on top of your previous exercise from [episode 2](../ep2). In this exercise you will create a docker-compose with 2 services. The first service is a simple MariaDB container and the second container is a python script that read ingredients for a potato salad recipe and inserts them into the mariadb container.

1. Adapt your `main.py` that can insert our potato salad ingredients to mariadb either using Pandas or SQLAlchemy.
1. The script needs to read the list of ingredients from our `data/potato_salad.yml` file
1. Create a custom docker container for your script which takes the MariaDB connection parameters (host, user, pswd) as environment variables
1. Create a docker compose which runs both containers. You must have your script to start correctly only after MariaDB is fully functional 

> hint: either use the docker `wait-for-it.sh` script, or create a `HEALTHCHECK` for your mariadb container and use the `depends_on` tag.

### Extra points:

1. Create another container that reads your ingredients table and prints them to the screen. This container must run after your loading container is done.

