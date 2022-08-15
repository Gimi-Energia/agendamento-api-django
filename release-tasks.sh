echo 'Executing migrations...'
python agenda_me/manage.py migrate
echo 'Migrations completed.'

echo 'Loading initial data for database...'
python manage.py loaddata fixtures
echo 'Initial data loaded.'