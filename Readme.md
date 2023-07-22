
# DJANGO REST API FOR EMPLOYMENT PORTAL

Basic project with APIs developed with Django rest frameworks, using authentication,
expose endpoints API REST for employ postulations to be able to connect with Frontend
frameworks like Vue, React, Angular, etc. and using databases like Postgres and MongoDB.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_DB`
`POSTGRES_USER`
`POSTGRES_PASSWORD`
`POSTGRES_HOSTNAME`
`POSTGRES_DOCKER_PORT`
`POSTGRES_PORT`
`APP_HOSTNAME`
`APP_HOST`
`APP_PORT`
`APP_ADMIN_USER`
`APP_ADMIN_PASSWORD`
`APP_ADMIN_EMAIL`
`APP_ALGORITHM`
`APP_SECRET_KEY`
`DJANGO_SECRET_KEY`

## API Reference

#### Admin Django Rest Framework

```http
  GET /admin/
```

| Parameter  | Type     | Description                           |
| :--------- | :------- | :------------------------------------ |
| `username` | `string` | **Required**. username of you account |
| `password` | `string` | **Required**. password of you account |



#### Register(create) User

```http
  POST /api/register/
```

| Parameter          | Type     | Description                                   |
| :----------------- | :------- | :-------------------------------------------- |
| `username`         | `string` | **Required**. username of you account         |
| `password`         | `string` | **Required**. password of you account         |
| `confirm_password` | `string` | **Required**. confirm password of you account |
| `first_name`       | `string` | First name of you user                        |
| `last_name`        | `string` | Last name of you user                         |
| `email`            | `string` | Email of you user                             |



#### Login User

```http
  POST /api/login/
```

| Parameter  | Type     | Description                           |
| :--------- | :------- | :------------------------------------ |
| `username` | `string` | **Required**. username of you account |
| `password` | `string` | **Required**. password of you account |



#### Create Company - Authorization Token <token>

```http
    POST /api/create-company/
```

| Parameter | Type     | Description                          |
| :-------- | :------- | :--------------------------------    |
| `name`    | `string` | **Required**. name of item to create |
| `nit`     | `string` | **Required**. nit of item to create  |



#### Create Offer - Authorization Token <token>

```http
    POST /api/create-offer/
```

| Parameter     | Type      | Description                                   |
| :--------     | :-------  | :--------------------------------             |
| `title`       | `string`  | **Required**. title of item to create         |
| `description` | `string`  | **Required**. description of item to create   |
| `salary`      | `int`     | **Required**. salary of item to create        |
| `company`     | `string`  | **Required**. company of item to create       |
| `skills`      | `string`  | **Required**. skills of item to create        |



#### Update Offer - Authorization Token <token>

```http
  PUT /api/update-offer/${id}/
```

| Parameter | Type  | Description                        |
| :-------- | :---- | :--------------------------------- |
| `id`      | `int` | **Required**. Id of item to update |



#### Create Company - Authorization Token <token>

```http
    POST /api/create-postulation/
```

| Parameter | Type      | Description                           |
| :-------- | :-------  | :--------------------------------     |
| `user`    | `int`     | **Required**. user of item to create  |
| `offer`   | `int`     | **Required**. offer of item to create |




## Pre-requisites

Before you begin, ensure you have met the following requirements:

- You have installed the 3.10 version of `python` and `pip`, [Instructions](https://www.python.org/downloads/)
- Docker and docker-compose installed, Docker [Instructions](https://docs.docker.com/engine/install/) and Docker Compose [Instructions](https://docs.docker.com/compose/install/)

## Installation

Clone the project

```bash
  git clone (https://github.com/rvosistemas/focunti.git)
```

Go to the project directory

```bash
  cd django_rest
```

Create a .env file in the root of the project and configure the necessary environment variables. You can use the .env.example file as a template

```bash
  cp .env.example .env
```

Make sure to configure the environment variables according to your needs, such as the PostgreSQL database settings, secret keys, etc.

Run the following command to create and start the Docker containers:

```bash
  docker-compose up -d --build
```

This will create and run the Docker containers for the project, including the PostgreSQL database container.

Apply the database migrations

  ```bash
    docker-compose exec web python manage.py migrate
  ```


Create a superuser for the Django admin

  ```bash
    docker-compose exec web python manage.py createsuperuser
  ```


## Running Tests

To run tests, open terminal in docker container

```bash
  docker-compose exec web bash
```

Run the following command to run tests (custom command in Makefile):

```bash
  make test_coverage_api_rest_postgres
```

## Running the project

To run the project, open terminal in docker container

```bash
  docker-compose up -d
```
Once the installation is complete, you can access the project in your web browser using the URL http://localhost:8000.
Here you will find the API interface and can start using the project.

## Stop the project

To stop the project, open terminal in docker container

```bash
  docker-compose down
```

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Documentation - with Swagger and Redoc OpenAPi (run server api)

[Documentation](http://127.0.0.1:8000/redoc/)

## Acknowledgements

Greats resources and tools for developing APIs.

 - [Django Rest Framework](https://www.django-rest-framework.org/)
 - [Postgresql](https://www.postgresql.org/docs/current/index.html)


## Authors

- [@rvosistemas](https://github.com/rvosistemas)

