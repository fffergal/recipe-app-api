# recipe-app-api

A toy backend project for learning Django.

## How to play with the API

Assuming you have Docker set up and ready, create a user you can use to
authenticate with:

```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

The command is interactive and you need to enter a username and password.

Next start the server with:

```
docker-compose up
```

Go to http://localhost:8001/api/docs/ in a browser. Scroll down to the `POST
/api/users/token/` endpoint, open it, and press “Try it out”. Enter the email
and password you chose before and press “Execute”. Copy the token from the
response body. Scroll to the top of the page and press “Authorize”. Scroll down
to “tokenAuth”, enter “Token”, a space, and paste the token, then press
“Authorize”. You can now use all the other endpoints.
