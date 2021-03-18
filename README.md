# internio

This is the next BIG thing... made with Django, will be scaled with Postgresql, AWS.

Enough of the paparazzi! Internio is a Job Portal written in Django - Simple and Stupid! :+1: :rocket:

### See screenshots

## Usage

source .env-dev.sh

### Build internio project

docker-compose up -d --build internio db adminer

### Database

After building project, go to adminer on localhost:8080 and create internioDB database.
Then run command below:

docker exec internio python manage.py migrate

### Logs

To see logs of any of the container:
docker logs -f internio
docker logs db
