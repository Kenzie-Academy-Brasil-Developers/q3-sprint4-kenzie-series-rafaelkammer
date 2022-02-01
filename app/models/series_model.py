from app.models import DatabaseConnector

class Series(DatabaseConnector):
    def __init__(self, *args, **kwargs):
        self.serie = kwargs["serie"].title()
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"].title()
        self.imdb_rating = kwargs["imdb_rating"]

    def create(self):
        self.get_conn_cur()

        query = """
            INSERT INTO
                ka_series (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        query_values = list(self.__dict__.values())

        self.cur.execute(query, query_values)

        print(self.__dict__)

        inserted_serie = self.cur.fetchone()

        self.commit_and_close()

        return inserted_serie

    @classmethod
    def series(cls):
        cls.get_conn_cur()

        create_db_query = """
        CREATE TABLE IF NOT EXISTS ka_series (
                id              BIGSERIAL PRIMARY KEY,
                serie           VARCHAR(100) NOT NULL UNIQUE, 
                seasons         INTEGER NOT NULL, 
                released_date   DATE NOT NULL, 
                genre           VARCHAR(50) NOT NULL, 
                imdb_rating     FLOAT NOT NULL
            );
        """

        cls.cur.execute(create_db_query)

        query = "SELECT * FROM ka_series;"

        cls.cur.execute(query)

        series = cls.cur.fetchall()

        cls.commit_and_close()

        return series

    @classmethod
    def select_by_id(cls, series_id):
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series WHERE id = (%s)"

        cls.cur.execute(query, series_id)

        serie = cls.cur.fetchone()

        cls.commit_and_close()

        return serie