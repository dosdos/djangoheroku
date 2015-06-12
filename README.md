# Django Heroku Base App

A django heroku project template based on [https://github.com/heroku/heroku-django-template](https://github.com/heroku/heroku-django-template) enriched with the most needed django features and packages.

## Prerequisites
### Heroku Toolbelt and Login
Run this from your terminal (please ensure that you have Ruby installed):

```
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

Login into Heroku from shell with your heroku credentials (you can sign up for free [here](https://signup.heroku.com/www-header))

```
heroku login
```

## Install
1. Clone this project
2. Create your venv working environment: Pycharm > Settings > Project Interpreter > (Coil icon) > Create VirtualEnv
3. Set up grunt, install bower components and use grunt watch
    - Move to etc folder 

        ```cd etc```
        
    - Install grunt modules (make sure you have `node.js` and `node package manager` installed)
        
        ```sudo npm install```
    
    - Install bower components 

        ```bower install```

    - Launch grunt default: it will automatically compile every less file and js file, preen bower components and check for js errors thanks to jshint 
    
        ```grunt```

    - Launch grunt watch: it's a watcher that keeps listening and compiles less and compresses js file a file is changed 
    
        ```grunt watch```
        
4. Add ENV='prod' variable in heroku

    ```
    heroku config:set ENV='prod'
    ```
5. Deploy app to heroku

## Environmental Variables
Please note that to store env variable in local machine is necessary to add them to the venv activate file in order to use them while venv is running. Just add to activate file

```
export SECRET_KEY="here_the_diango_secret_key"
```


## Deploy to Heroku
### Set up remotes
First check the remotes of the project

```
git remote --v
```

If `heroku` is already among your git remotes, but it is not pointing to the right application, remove the `heroku` remote

```
git remote remove heroku
```

Add your heroku app to git remotes

```
heroku git:remote -a <app_name>
```

### Deploy
Deploying your code to heroku is done through git

```
git push heroku master
```

Note: make sure your local `master` branch is always aligned with `origin master`. If not aligned, when pushing to `heroku master`, heroku blocks the push launching an error.


### Database
If this was your first deploy we need to set up the db. Heroku allows to run commands through its toolbelt `run` command.

1. Syncdb

    ```
    git remote remove heroku
    ```
    

2. (Optional) Create additional super user
    
    ```
    heroku run python manage.py createsuperuser
    ```
    

3. Migrate
    
    ```
    heroku run python manage.py migrate
    ```

Note: to review database coordinates and status use `heroku pg` command

4. Access heroku database from shell (please, make sure you have installed Postgres locally)

    ```
    heroku pg:psql
    ```


## Handy commands
### Open heroku app directly in browser

```
heroku open
```

### Heroku status
Allows to see the application status, if it's running or sleeping, if deployment was successful

```
heroku ps
```

### Assign number of app instances (dynos):
Warning! Setting up a higher than 1 number of dynos may cause the service to be not free anymore

```
heroku ps:scale web=1
```

### Using Django shell

```
heroku run python manage.py shell
```

### Heroku logs
If you are not using an external logging service (aka [Logentries](https://logentries.com/) or [Papertrail](https://addons.heroku.com/papertrail)) heroku logs come in handy

```
heroku logs --tail
```

Note: there is a free [logentries plugin](https://addons.heroku.com/logentries) for heroku that eases the process to connect logentries with your heroku app


### Add addons
The example is Papertrail addon, a logging service that allows to store logs with an higher size and time retention than the heroku 1500 log entries limit

1. Add addon

    ```
    heroku addons:create papertrail
    ```

2. Check list of active addons

    ```
    heroku addons
    ```
    
3. Open logs in shell

    ```
    heroku addons:open papertrail
    ```

## Config vars
Heroku allows to store configuration variables, such as encryption keys or external resource addresses in config vars ([source](https://devcenter.heroku.com/articles/getting-started-with-python#define-config-vars)).

1. Set a new configuration variable

    ```
    heroku config:set TIMES=2
    ```


2. Review all configuration variables

    ```
    heroku config
    ```


## Further Reading
- [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile)
- [Getting Started with Django on Heroku](https://devcenter.heroku.com/articles/getting-started-with-django)
- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)