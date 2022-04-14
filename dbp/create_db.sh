#!/bin/bash
# Spins up a docker container with a postgres database server. 
# bash create_db.sh <postgres-user_s-password>
# To bring this down, run
# $ docker rm -f db-playground

DOCKER_IMAGE_NAME=db-playground
PASSWORD=$1  # password for postgres user
PORT=5555

docker run --rm --name "$DOCKER_IMAGE_NAME" -e POSTGRES_PASSWORD="$PASSWORD" -dp "$PORT":5432 postgres:9.2

until pg_isready -t 3 -h localhost -p "$PORT"
do
  sleep 1
done

PGPASSWORD=$PASSWORD psql -h localhost -p "$PORT" -U postgres -d postgres << EOF
CREATE USER dwight;
ALTER ROLE dwight WITH CREATEDB;
ALTER ROLE dwight WITH PASSWORD 'notyourbeeswax';
EOF
