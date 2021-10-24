### Hot to stat project:

Clone rep and go to it's folder in terminal:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd api_final_yatube
```

Create and activate Virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Install packages from requirements.txt:

```
pip install -r requirements.txt
```

Make migrations:

```
python3 manage.py migrate
```

Launch project:

```
python3 manage.py runserver
```
