web: gunicorn djangodrftodo.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
release: echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(email='dayopraisegod@gmail.com', username='PraiseGod', password='manmainman', fullname='Adesanmi D. PraiseGod')"