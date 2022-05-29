from sqlalchemy import create_engine


def save_data(dataframe):
    save_df = dataframe
    engine = create_engine('sqlite:///save_pandas.sqlite', echo=True)
    sqlite_connection = engine.connect()
    sqlite_table = 'Books'

    save_df.to_sql(sqlite_table, sqlite_connection, if_exists='append', index=False)
    return print('Listo manao')

