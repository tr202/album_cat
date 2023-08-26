# Artist and albums catalog

## Tech
    -Python
    -Django
    -DRF
    -Postgres
## Infra
    -Nginx
    -Gunicorn
    -Docker-compose
## Using
    ####- Clone repository
    ####- Change folder to album_cat
            cd /album_cat/
    ####- Run docker-compose
            sudo docker-compose -f docker-compose.yml up -d
    ####- Execute the following commands
            docker-compose -f docker-compose.yml exec catalog python manage.py migrate
            docker compose -f docker-compose.production.yml exec catalog python manage.py collectstatic
            sudo docker compose -f docker-compose.yml exec catalog cp -r /app/collected_static/. /static/static
            sudo docker compose -f docker-compose.yml exec catalog python manage.py loaddata db.json
    ####- Test the endpoints
            http://your_host/docs
            http://your_host/admin   (login: adm passwd: 123)
            http://your_host/api
            http://your_host/artist_group
            http://your_host/album
            http://your_host/song
            http://your_host/song/?artist_group_id=1
            http://your_host/song/?album_id=3


