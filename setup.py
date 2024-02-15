import os
import re

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "sqlalchemy_yugabytedb", "__init__.py")) as v:
    VERSION = re.compile(r'.*__version__ = "(.*?)"', re.S).match(v.read()).group(1)

with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    README = f.read()

setup(
    name="sqlalchemy-yugabytedb",
    version=VERSION,
    author="Yugabyte",
    author_email="",
    url="https://github.com/yugabyte/sqlalchemy-yugabytedb",
    description="YugabyteDB dialect for SQLAlchemy",
    long_description=README,
    long_description_content_type="text/markdown",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="SQLAlchemy YugabyteDB",
    project_urls={
        "Documentation": "",
        "Source": "https://github.com/yugabyte/sqlalchemy-yugabytedb",
        "Tracker": "https://github.com/yugabyte/sqlalchemy-yugabytedb/issues",
    },
    packages=find_packages(include=["sqlalchemy_yugabytedb"]),
    include_package_data=True,
    install_requires=["SQLAlchemy","psycopg2-yugabytedb"],
    zip_safe=False,
    entry_points={
        "sqlalchemy.dialects": [
            "yugabytedb = sqlalchemy_yugabytedb.psycopg2:YugabyteDBDialect_psycopg2",
            "yugabytedb.psycopg2 = sqlalchemy_yugabytedb.psycopg2:YugabyteDBDialect_psycopg2"
        ],
    },
)
