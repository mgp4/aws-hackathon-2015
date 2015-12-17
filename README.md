[![Build Status](https://travis-ci.org/mgp4/aws-hackathon-2015.svg?branch=master)](https://travis-ci.org/mgp4/aws-hackathon-2015)
[![Coverage Status](https://coveralls.io/repos/mgp4/aws-hackathon-2015/badge.svg?branch=master&service=github)](https://coveralls.io/github/mgp4/aws-hackathon-2015?branch=master)


## Installation

Needed: Python 3

1. `git clone https://github.com/mgp4/aws-hackathon-2015.git`
2. `virtualenv3 virtualenv`
3. Make sure `virtualenv/bin` is in `PATH`.
4. `cd aws-hackathon-2015`
5. `pip install -r requirements.txt`
6. Optionally create `mgp4_django/settings/local.py` if you want to override some settings.


## Run

Needed: `./manage.py migrate` for synchronizing the database schema. (Creates and uses `db.sqlite3` by default.)

Run: `DEBUG=1 ./manage.py runserver` when developing.


## AWS usage

You can use `eb init`, `eb create` and `eb deploy` (configuration included).
See [`mgp4_django/settings/aws.py`](https://github.com/mgp4/aws-hackathon-2015/blob/master/mgp4_django/settings/aws.py)
to know which system variables are expected. (RDS ones are passed down automatically if EB created properly.)
