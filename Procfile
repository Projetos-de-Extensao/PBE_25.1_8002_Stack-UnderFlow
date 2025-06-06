web: gunicorn --chdir src projeto.wsgi
release: python src/manage.py migrate && python src/manage.py collectstatic --no-input