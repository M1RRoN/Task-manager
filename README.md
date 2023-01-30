### Hexlet tests and linter status:
[![Actions Status](https://github.com/M1RRoN/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/M1RRoN/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/feb3c5fd658c71dc32e8/maintainability)](https://codeclimate.com/github/M1RRoN/python-project-52/maintainability)

# Task Manager

_Register, create, delete and edit tasks, labels and statuses, assign executors to tasks. Filter tasks by tags, statuses, and executors, or filter only your created tasks._

##  DEMO

Just click and try to use **[DEMO on Railway](https://python-project-52-production-af44.up.railway.app/)** or 
**[DEMO on REG.RU](http://project52.site/)**

_P.S.: You will need to register to try all the features in demo._

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

