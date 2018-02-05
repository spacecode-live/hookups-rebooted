# Hookups💋 Rebooted

A modern rewrite of the
[classic Hookups💋](https://github.com/UWCCSC/hookup-csc) app. Built for
anonymous liasons of the most intimate kind, using
[Flask](http://flask.pocoo.org/).

![Mockup of how the hookups app looks like](https://i.imgur.com/Zqv18Yt.png)
*Note: All images are product mockups, and are not representative of the
current stage of this project*

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes. See deployment for notes on
how to deploy the project on a live system.

### Prerequisites

Hookups requires `python2` and `virtualenv`.

### Installing

After all of the dependencies have been satisfied, create yourself a
`virtualenv` by running:

```bash
virtualenv venv
```

Next, you need to install the dependencies with `pip` (`pip2` if you are on
Arch):

```bash
pip install Flask flask-socketio eventlet pycodestyle
```

Finally, to run the server:
```bash
export FLASK_APP=./HookupsRebooted/Hookups.py
flask run
```

## Running the tests

Running the tests is as easy as running the prepared `run_debug.sh` script:

```bash
sh run_debug.sh
```

This script runs both unit and code style tests.

### Break down into end to end tests

To be created.

### And coding style tests

To be created.

## Deployment

To be created.

## Built With

* [Flask](http://flask.pocoo.org/) - a powerful microframework for python2 web
development.

## Contributing

Please read
[CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426)
for details on our code of conduct, and the process for submitting pull
requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* [@ShenZhouHong](https://github.com/orgs/UWCCSC/people/ShenZhouHong)
* [@pinusc](https://github.com/orgs/UWCCSC/people/pinusc)
* [@markovejnovic](https://github.com/orgs/UWCCSC/people/markovejnovic)

## License

This project is currently closed source - see the [LICENSE.md](LICENSE.md)
file for details.
