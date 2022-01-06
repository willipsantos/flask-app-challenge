#!/bin/bash

set -e

until PGPASSWORD=9Zrk2w76aYJGr7UEcQLc psql -h "db-oauth-system" -U "oauth-system" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec "$@"
