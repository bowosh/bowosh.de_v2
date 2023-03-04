import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION']

engine = create_engine(
  db_connection_string,
  connect_args={"ssl": {
    "ssl_ca": "/home/gord/client-ssl/ca.pem"
  }})
