from sqlalchemy.dialects.postgresql.base import PGDialect
from sqlalchemy import text
import re

IDX_USING = re.compile(r"^(?:lsm|hash|gist|gin|[\w_]+)$", re.I)

class YugabyteDBDialect(PGDialect):
    name = "yugabytedb"

    def initialize(self, connection):
        # Bypass PGDialect's initialize implementation, which looks at
        # server_version_info and performs postgres-specific queries
        # to detect certain features on the server. Set the attributes
        # by hand and hope things don't change out from under us too
        # often.
        super(PGDialect, self).initialize(connection)
        sversion = connection.scalar(text("select version()"))
        yb_version_regex = re.compile(r'YB-(.)*-')
        yb_version = yb_version_regex.search(sversion)
        yb_version = int(yb_version.group()[5:yb_version.group().find('.',5)])
        self._is_v28plus =  yb_version > 8
        self._supports_savepoints = self._is_v28plus

    _isolation_lookup = set(
        [
            "SERIALIZABLE",
            "SNAPSHOT",
            "READ COMMITTED",
        ]
    )