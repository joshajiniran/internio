#!/usr/bin/env bash

DB_PSWD=postgres
DB_USER=postgres
DB_HOST=db
DB_PORT=5432

export DB_URL=postgresql://${DB_USER}:${DB_PSWD}@${DB_HOST}:${DB_PORT}
export DB_HOST=$DB_HOST
export DB_PORT=$DB_PORT
export DB_USER=$DB_USER
export DB_PSWD=$DB_PSWD