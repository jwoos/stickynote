# Stick Note

## What is this?
A service that will allow you to have notes that expire after a set period of time! You can either post anonymously or by providing a password so you can edit and delete it later on. No guarantees are made about keeping notes or auth users around as they are all stored in memory. Redis will start ejecting keys by approximated LRU so when the database is running out of memory, everything is fair game.

## API
`/notes`: POST

`/notes/<note_hash>`: GET, PATCH, DELETE

## Run
The following will build the containers as well running them if you've never run it before:
```bash
docker-compose up api
```

Otherwise, to rebuild:
```bash
docker-compose build
```

## Architecture
```
Flask app (uWSGI) <---> NGINX <---> Client (API)
            /static <--->/ \<---> Client (Site)
```
I chose to run the API and the site separately and do API calls rather than bundling in rendering and what not.

### API
1. Request comes in to NGINX
2. NGINX passes the request onto uWSGI to take care of
3. Flask app does the work and returns through uWSGI
3. NGINX serves the returned data to client

### Site
1. Request comes in to NGINX
2. NGINX parses the request and looks for the appropriate file on the file system
3. NGINX serves the file to client
