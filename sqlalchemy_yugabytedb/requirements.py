from sqlalchemy.testing.requirements import SuiteRequirements as SuiteRequirementsSQLA
from sqlalchemy.testing import exclusions

class Requirements(SuiteRequirementsSQLA):

    savepoints = exclusions.skip_if(
        lambda config: not config.db.dialect._supports_savepoints,
        "versions before 2.8 do not support savepoints.",
    )

    # The psycopg driver doesn't support these.
    percent_schema_names = exclusions.closed()
    order_by_label_with_expression = exclusions.open()
    order_by_col_from_union = exclusions.open()
    implicitly_named_constraints = exclusions.open()
    supports_distinct_on = exclusions.open()

    @property
    def deferrable_or_no_constraints(self):
        return exclusions.closed()

    @property
    def deferrable_fks(self):
        return exclusions.open()

    @property
    def update_nowait(self):
        """Target database must support SELECT...FOR UPDATE NOWAIT"""
        return exclusions.closed()

    def get_isolation_levels(self, config):
        return {"default": "SNAPSHOT", "supported": ["SNAPSHOT","SERIALIZABLE", "READ COMMITTED"]}