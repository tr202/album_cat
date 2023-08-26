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
    - Clone repository
    - Change folder to album_cat
            cd /album_cat/
    - Make scripts executable
            chmod ugo+x start
            chmod ugo+x stop
    - Start the app
            sudo start
    - Test the endpoints
            http://your_host/docs
            http://your_host/admin   (login: adm passwd: 123)
            http://your_host/api
            http://your_host/artist_group
            http://your_host/album
            http://your_host/song
            http://your_host/song/?artist_group_id=1
            http://your_host/song/?album_id=3
    - Stop app
            sudo stop

