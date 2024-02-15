from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from .base import YugabyteDBDialect


class YugabyteDBDialect_psycopg2(PGDialect_psycopg2, YugabyteDBDialect):
    driver = "psycopg2"  # driver name
    supports_statement_cache = True