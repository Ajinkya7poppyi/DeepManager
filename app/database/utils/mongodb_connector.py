import logging
from mongoengine import connect
from . import (
    DATABASE_NAME,
    DATABASE_PORT,
    DATABASE_URL,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
)

logger = logging.getLogger(__name__)


class Connection:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        """Initiaize connection to mongodb

        Raises:
            Exception: Connection to mongodb failed
        """
        try:
            self.conn = connect(
                db=DATABASE_NAME,
                host=DATABASE_URL,
                port=DATABASE_PORT,
                # username=DATABASE_USERNAME,
                # password=DATABASE_PASSWORD,
            )
            return self.conn
        except Exception as e:
            logger.exception(
                "Exception Occured while creating connection to database {}".format(e)
            )
            raise Exception("Database Connection Failure")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection to mongodb

        Raises:
            Exception: Closing to mongodb failed
        """
        try:
            self.conn.close()
        except Exception as e:
            logger.exception(
                "Exception Occured while closing connection to database {}".format(e)
            )
            raise Exception("Database closing Failure")
