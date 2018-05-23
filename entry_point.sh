#!/bin/bash


if fabmanager list-users  --app superset | grep "role:\[Admin\]" | grep $ADMIN_USERNAME; then
    echo "Skipping admin user creation as $ADMIN_USERNAME already exists."
else
    echo "Setting up admin user $ADMIN_USERNAME."
    fabmanager create-admin --app superset \
    --username $ADMIN_USERNAME \
    --firstname $ADMIN_FIRST_NAME \
    --lastname $ADMIN_LAST_NAME \
    --email $ADMIN_EMAIL \
    --password $ADMIN_PASSWORD
fi

superset db upgrade
superset init

bash -c "$@"
