# Catalog
    Catalog of artists and their albums with filtering of works by group artist and album.
    Demo site [Catalog](http://185.217.199.6/docs/).
## Features
    * Automatic generation of API schema
    * Easy querying and filtering of data
    
## Tech
    -Python
    -Django
    -DRF
    -Postgres
    -Nginx
    -Gunicorn
    -Docker

## Installation and usage
    A linux PC with docker-compose and git is required to run.
    For other hosts, use docker documentation and commands from the start script.
    Test data is preloaded, update through admin zone.

    - Clone repository
            git clone https://github.com/tr202/album_cat.git
    - Browse to album_cat
            cd album_cat
    - Make scripts executable
            chmod ugo+x start
            chmod ugo+x stop
    - Start the app
            sudo ./start
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
            sudo ./stop

