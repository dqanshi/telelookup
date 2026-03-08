from clickhouse_driver import Client
from config import CLICKHOUSE_HOST, CLICKHOUSE_DB, MAX_RESULTS

client = Client(host=CLICKHOUSE_HOST)


def search_database(query):

    try:

        if query.isdigit():

            sql = f"""
            SELECT raw_line
            FROM {CLICKHOUSE_DB}.users
            WHERE raw_line LIKE '{query}%'
            LIMIT {MAX_RESULTS}
            """

        else:

            sql = f"""
            SELECT raw_line
            FROM {CLICKHOUSE_DB}.users
            WHERE raw_line LIKE '%{query}%'
            LIMIT {MAX_RESULTS}
            """

        rows = client.execute(sql)

        return [r[0] for r in rows]

    except Exception as e:
        print("DB ERROR:", e)
        return []
