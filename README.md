# geekjobs

Tech job board in django

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install python3, pip3 and a django supported database (sqlite, postgres, mysql, etc...). 
However this documentation uses postgresql, changing your settings file will allow you to use another db. 
So far postgresql and sqlite has being tested.

### Installing

1) Install the python libraries with:

```
pip install -r project_directory/geekjobs/requirements.txt
```
2) Configure your database at 

```
project_directory/geekjobs/settings/prod_settings.py
```

3) Create and configure your secrets.py file 

```
touch project_directory/geekjobs/settings/secrets.py
```

It should look like:

```
import os

os.environ['DJANGO_GEEK_JOBS_SECRET_KEY'] = "your_django_secret_key"
os.environ['STRIPE_TEST_API_KEY'] = "your_stripe_test_API_key"
os.environ['STRIPE_API_KEY'] = "your_stripe_API_key"
os.environ['STRIPE_DATA_KEY'] = "your_stripe_data_key"
os.environ['POSTGRES_USER'] = "your_db_user"
os.environ['POSTGRES_PASSWORD'] = "your_db_passwd"
```

if you need a secret_key you can run:

```
python -c 'import random; import string; print "".join([random.SystemRandom().choice(string.digits + string.letters + string.punctuation) for i in range(100)])'
```

## Running the tests

python3 manage.py test

## Deployment

On your project directory run:

```
python3 manage.py runserver
```

Visit http://localhost:8000 and have fun!

## Built With

* [Python](https://www.python.org/) - The programming language
* [Django](https://www.djangoproject.com/) - The web framework used
* [Stripes](https://stripe.com/) - Credit Card API

## Contributing

Please get in touch with me if you are interested in contributing.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/paconte/geekjobs/tags). 

## Authors

* **Francisco Revilla** - [paconte](https://github.com/paconte)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
