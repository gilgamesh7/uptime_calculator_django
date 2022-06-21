# uptime_calculator_django

# Link to app
On Azure : [Uptime & SLA Calculator]()
<br/>
In Dev : [Uptime & SLA Calculator]()

# Learning Links
[Django REST API](https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html) <br>

# API Details
[Uptime.is](https://uptime.is)

# packages to be installed in venv
- django

# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject calculate_sla_uptime .  
3. Generate application : python3 manage.py startapp uptime

# To migrate after changing models
1. python manage.py makemigrations
2. python manage.py migrate

# Run server
python3 manage.py runserver  

# To make ready for Azure
1. Add requirements.txt
2. Add '?????????????.azurewebsites.net' to ALLOWED_HOSTS
3. Static_root to settings.py (not necessary for this project)
4. Add to urlsettings in url.py + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) (not necessary for this project)

