### Hexlet tests and linter status:
[![Actions Status](https://github.com/M1RRoN/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/M1RRoN/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/feb3c5fd658c71dc32e8/maintainability)](https://codeclimate.com/github/M1RRoN/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/feb3c5fd658c71dc32e8/test_coverage)](https://codeclimate.com/github/M1RRoN/python-project-52/test_coverage)
[![Django CI](https://github.com/M1RRoN/python-project-52/workflows/Django_CI/badge.svg)](https://github.com/M1RRoN/python-project-52/actions)

# Task Manager

_Register, create, delete and edit tasks, labels and statuses, assign executors to tasks. Filter tasks by tags, statuses, and executors, or filter only your created tasks._

## Installation

Clone the repository:

`git clone https://github.com/DzmitrySha/python-project-52.git`

Go to the project folder:

`cd python-project-52`

Install dependencies with Poetry:

(If you don't have Poetry, follow this guide to install it: [Install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer))

`make install`

## Settings

Create an ".env" file in the root project directory: 

`touch .env`

оr rename and edit existing ".env.example" file.

Write following constants to the .env file:

1. `SECRET_KEY='your_Django_secret_key'` 

You can generate one with `make secretkey` command.

2. `DATABASE_URL='your_database_url_path'` 

To use simple sqlite database use this record: 

`DATABASE_URL='sqlite:///db.sqlite3'`

## Database preparation

`make migration`

`make migrate`

`make createsuperuser`

## Start project

`make runserver`

Use this app in browser on http://localhost:8080

---
Good Luck!

