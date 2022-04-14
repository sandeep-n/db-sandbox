from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.sql.ddl import CreateSchema
from sqlalchemy_utils import create_database, drop_database

from dbp.schema import Base


DB_NAME = 'enum_sandbox'
SCHEMA = 'playground'
USER = 'dwight'


def get_engine():
    dialect = 'postgresql'
    driver = 'psycopg2'
    password = 'notyourbeeswax'
    host = 'localhost'
    port = 5555
    conn_str = f'{dialect}+{driver}://{USER}:{password}@{host}:{port}/{DB_NAME}'
    engine = create_engine(conn_str, poolclass=NullPool, executemany_mode='values', echo=False)
    return engine


def get_session():
    engine = get_engine()
    return sessionmaker(bind=engine)()


@contextmanager
def session_scope():
    session = get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def create_db():
    engine = get_engine()
    create_database(engine.url)
    engine.execute(CreateSchema('playground'))


def destroy_db():
    engine = get_engine()
    drop_database(engine.url)


def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

    engine.execute(f'REVOKE CONNECT ON DATABASE {DB_NAME} FROM PUBLIC')

    engine.execute(f'GRANT CONNECT ON DATABASE {DB_NAME} TO {USER}')
    engine.execute(f'GRANT USAGE ON SCHEMA playground TO {USER}')
    engine.execute(
        f'ALTER DEFAULT PRIVILEGES IN SCHEMA {SCHEMA} GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {USER}'
    )
    engine.execute(f'GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA {SCHEMA} TO {USER}')
    engine.execute(f'GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA {SCHEMA} to {USER}')
    engine.execute(
        f'ALTER DEFAULT PRIVILEGES IN SCHEMA {SCHEMA} GRANT USAGE, SELECT ON SEQUENCES TO {USER};'
    )


if __name__ == '__main__':
    create_db()
    # create_tables()
