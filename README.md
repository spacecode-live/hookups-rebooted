# Hookups💋 Rebooted

A modern rewrite of the [classic Hookups💋](https://github.com/UWCCSC/hookup-csc) app. Built for anonymous liasons of the most intimate kind, using [Flask](http://flask.pocoo.org/), [Websockets](www.websocket.org), and the latest modern web technologies.

![Mockup of how the hookups app looks like](https://i.imgur.com/Zqv18Yt.png)
*Note: All images are product mockups, and are not representative of the current stage of this project*

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Hookups💋 Rebooted uses [Vagrant](https://www.vagrantup.com/), a powerful tool that provides declarative, version-controlled development environments. This allows all developers to begin on the same Operating System with the same toolchain. Installing vagrant is simple:

* [Vagrant binary downloads](https://www.vagrantup.com/)
* [Compile Vagrant from source](https://www.vagrantup.com/docs/installation/source.html)
* [Official Vagrant documentation](https://www.vagrantup.com/docs/)

### Installing

Once vagrant is installed, it is all a matter of `cd`'ing into the project repository, and running:


```
vagrant up
```

This boots and initializes the virtual machine. The `Vagrantfile` in this project automatically takes care of dependency management, and sets up an `virtualenv` environment for Flask. Once this is complete, simply run:

```
vagrant ssh
```

This creates an shell into the virtual machine. Now you are all set to begin developing! For more information regarding how to use Vagrant, feel free to check out their [quickstart documentation]https://www.vagrantup.com/intro/getting-started/index.html.

## Running the tests

To be created.

### Break down into end to end tests

To be created.

### And coding style tests

To be created.

## Deployment

To be created.

## Built With

* [Flask](http://flask.pocoo.org/) - a powerful microframework for python2 web development.
* [Vue.js](https://vuejs.org/) - a progressive javascript frontend framework.
* [Bootstrap](https://getbootstrap.com/) - A responsive, mobile-first CSS grid system.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* [@ShenZhouHong](https://github.com/orgs/UWCCSC/people/ShenZhouHong) - *UI and UX*
* [@pinusc](https://github.com/orgs/UWCCSC/people/pinusc) - *Backend and matchmaking*
* [@markovejnovic](https://github.com/orgs/UWCCSC/people/markovejnovic) - *Backend, python, and unit testing*.

## License

This project is currently closed source - see the [LICENSE.md](LICENSE.md) file for details.
