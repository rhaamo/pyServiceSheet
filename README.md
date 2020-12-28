# pyServiceSheet

Kiss and dirty app to manage a public-facing collection of equipment, with a work-log.

# Requirements
- Python 3.8 (minimum !)
- Nginx
- PostgreSQL

# Install - manual

We assume in here you are installing under the `pyservicesheet` user with default home directory `/home/pyservicesheet`, like by doing:
```
useradd -m -s /bin/bash pyservicesheet
```

## API Backend

```shell
sudo su - pyservicesheet
git clone https://github.com/rhaamo/pyservicesheet/ pyservicesheet
cd pyservicesheet
python3.8 -m virtualenv -p python3.8 venv
source venv/bin/activate
pip install --requirement requirements.txt
# For production environment
cp deploy/env.prod.sample .env
$EDITOR .env
# For local development see the other section
python manage.py collectstatic
# don't forget to run migrations
python manage.py migrate
# create a superuser
python manage.py createsuperuser
```

You can uses `deploy/pyservicesheet-server.service` for your systemd service. 

## Nginx
See the file `deploy/pyservicesheet-nginx.conf` for a sample, don't forget you need all the `location /xxx` as the example to make it works.

### Docker All-In-One image build
```
docker build -t pyservicesheet-allinone -f Dockerfile-allinone
```

## Updating
Look at release changes first if anything is needed.

```
sudo su - pyservicesheet
cd pyservicesheet
source venv/bin/activate
git pull
pip install -r requirements.txt
python manage.py migrate
```

Then restart your `pyservicesheet-server` service.

# Install - docker All In One
You can use the `Dockerfile-allinone` to run pyservicesheet.

See the file ./deploy/env.prod.sample for the list of ENV variables you can use for the container.

You can copy that env file, edit it, and use `--env-file your-env-file.prod` for `docker run/exec` too.

The volume for uploads is `/uploads`.

To migrate the database:
```
docker exec -it pyservicesheet python manage.py migrate
```

To create your superuser:
```
docker exec -it pyservicesheet python manage.py createsuperuser
```

Example build & run:
```
docker build -t pyservicesheet-allinone -f Dockerfile-allinone .
docker run --net=host --name pyservicesheet -it --rm --env-file .env -v /local/path/to/uploads:/uploads pyservicesheet-allinone:latest
```

# Contact
- Fedivers: dashie at pleroma.otter.sh
- Email: pyservicesheet at squeaky dot tech

# License
AGPL v3
