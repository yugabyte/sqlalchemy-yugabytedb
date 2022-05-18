from sqlalchemy.dialects import registry
import pytest

registry.register(
    "yugabytedb",
    "sqlalchemy_yugabyteb.psycopg2",
    "YugabyteDBDialect_psycopg2",
)
registry.register(
    "yugabytedb.psycopg2",
    "sqlalchemy_yugabytedb.psycopg2",
    "YugabyteDBDialect_psycopg2",
)

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

from sqlalchemy.testing.plugin.pytestplugin import *  # noqa