import pyodbc


def close_conn(conn: pyodbc.Connection):
    try:
        conn.close()
    except Exception as ex:
        print(f'err close cnn-> {ex}')
        pass


class ConnectionUtility:
    def __init__(self, dbtuser, dbtpass, dbtname, dbtserver, dbtclass, timeout: int = 0, secure: bool = True):
        self.dbuser = dbtuser
        self.dbpass = dbtpass
        self.dbserver = dbtserver
        self.dbclass = dbtclass
        self.dbname = dbtname
        self.timeout = timeout
        self.secure = secure

    def i_get_conn(self) -> pyodbc.Connection:
        ll_postgre = [
            'POSTGRESQL ODBC DRIVER(ANSI)',
            'POSTGRESQL ODBC DRIVER(UNICODE)',
            'POSTGRESQL ODBC DRIVER',
            'POSTGRESQL UNICODE']

        if str(self.dbclass).upper() in ll_postgre:
            port = "5432"

            split = str(self.dbserver).split(',')
            if len(split) == 2:
                port = split[1]

            ls_str_conn = 'DRIVER={' + self.dbclass + '};'
            ls_str_conn += f'SERVER={self.dbserver};'
            ls_str_conn += f'DATABASE={self.dbname};'
            ls_str_conn += f'UID={self.dbuser};'
            ls_str_conn += f'PWD={self.dbpass};'
            ls_str_conn += f'PORT={port};'

            conn = pyodbc.connect(ls_str_conn)
        else:
            ls_str_conn = 'DRIVER={' + self.dbclass + '};'
            ls_str_conn += f'SERVER={self.dbserver};'
            ls_str_conn += f'DATABASE={self.dbname};'
            ls_str_conn += f'UID={self.dbuser};'
            ls_str_conn += f'PWD={self.dbpass};'
            ls_str_conn += f'MARS_Connection=Yes;'
            ls_str_conn += f'Pooling=True;'
            ls_str_conn += f'Max Pool Size=100;'
            ls_str_conn += f'Min Pool Size=5;'

            if self.secure:
                ls_str_conn += ';Encrypt=yes;TrustServerCertificate=yes'

            conn = pyodbc.connect(ls_str_conn, timeout=self.timeout)

        return conn
