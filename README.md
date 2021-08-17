# djangotestpatterns

## Setup

Create a virtual environment.

```bash
$ python -m venv venv
```

Activate the virtual environment.

```bash
$ source venv/bin/activate
```

Install developer and application packages.


```bash
$ pip install -r requirements/local.txt
```

Migrate DB

```bash
$ python manage.py migrate
```

Create a superuser account.

```bash
$  python manage.pycreatesuperuser
```

Run tests

```bash
$ pytest
```
Run coverage

```bash
$ coverage run -m pytest
```
Get coverage report

```bash
$ coverage report
```

Get coverage HTML report

```bash
$ coverage html
```
