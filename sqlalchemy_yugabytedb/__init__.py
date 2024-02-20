from sqlalchemy.dialects import registry as _registry


__version__ = "1.0.0.1"

_registry.register(
    "yugabytedb.psycopg2",
    "sqlalchemy_yugabytedb.psycopg2",
    "YugabyteDBDialect_psycopg2",
)
