# YugabyteDB dialect for SQLAlchemy

## Prerequisites

For psycopg2 support you must install either:

* [psycopg2-yugabytedb](https://pypi.org/project/psycopg2-yugabytedb/), which has some
  [prerequisites](https://www.psycopg.org/docs/install.html#prerequisites) of
  its own. Or,

* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

(The binary package is a practical choice for development and testing but in
production it is advised to use the package built from sources.)

 
## Install and usage

Use `pip` to install the latest version. Clone the repository and run the following command:

`pip install .`

Use a `Yugabytedb` connection string when creating the `Engine`. For example,
to connect to a local YugabyteDB cluster using psycopg2:

```
from sqlalchemy import create_engine
engine = create_engine('yugabytedb://yugabyte@localhost:5433/yugabyte')
```

or

```
from sqlalchemy import create_engine
engine = create_engine('yugabytedb+psycopg2://yugabyte@localhost:5433/yugabyte')
```

