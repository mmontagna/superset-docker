
# Environment Variables

## Setting Database Environment Variables

Configuration settings are passed to superset_config.py via environment variables, which are specified below.

## Secrets

```
SUPERSET_SECRET_KEY=mysecretkey123
MAPBOX_API_KEY=mysecretkey123
```

## Sample MySQL Config
 
```
SQLALCHEMY_DATABASE_URI=mysql://superset:password@localhost:3306/superset
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

## Sample Postgres Config
 
```
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://superset:password@localhost/superset
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

## Configuring the Cache
Environment variables prefixed with `CACHE_` are pulled into superset's CACHE_CONFIG variable.

## Sample Redis Cache Config

```
CACHE_TYPE=redis
CACHE_DEFAULT_TIMEOUT=300
CACHE_KEY_PREFIX=superset_
CACHE_REDIS_URL=redis://localhost:6379/0
```


