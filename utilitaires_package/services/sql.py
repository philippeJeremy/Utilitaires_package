from sqlalchemy import create_engine, text


class Database:
    def __init__(self, db_type, host: str = "localhost", port=None, user=None, password=None, database=None, driver=None):
        self.db_type = db_type.lower()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.driver = driver

        self.engine = create_engine(self._build_url())

    def _build_url(self):
        drivers = {
            "sqlite": "",
            "postgres": "postgresql",
            "mysql": "mysql+pymysql",
            "sqlserver": "mssql+pyodbc",
        }

        db = drivers.get(self.db_type)
        if not db:
            raise ValueError(f"Type de DB non supporté: {self.db_type}")

        if self.db_type == "sqlite":
            return f"sqlite:///{self.database}"

        if self.driver:
            db = f"{self.db_type}+{self.driver}"

        return f"{db}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    def execute(self, query, params=None):
        with self.engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            conn.commit()
            return result

    def fetch_all(self, query, params=None):
        return self.execute(query, params).fetchall()

    def fetch_one(self, query, params=None):
        return self.execute(query, params).fetchone()
