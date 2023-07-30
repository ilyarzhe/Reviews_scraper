import psycopg2

class DbManager:
    def __init__(self, dbname, user, password, host, port) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        connection = psycopg2.connect(dbname=self.dbname,
                                      user=self.user,
                                      password=self.password,
                                      host=self.host,
                                      port=self.port)
        return connection
    def insert_review(self,review):
        create_table_query = '''
    CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    summary VARCHAR(255),
    text TEXT,
    rating FLOAT,
    date DATE
    );
    '''
        insert_query = f'''
INSERT INTO reviews (summary,text,rating,date) VALUES ('{review.summary}','{review.text}','{review.rating}',Date'{review.date}')'''
        connection = self.connect()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(create_table_query)
                    cursor.execute(insert_query)
                connection.commit()
                print("Table created successfully")
            except psycopg2.Error as e:
                print(e)
            finally:
                connection.close()
