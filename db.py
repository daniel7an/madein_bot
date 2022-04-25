from configure import host, port, user, password, dbname
import psycopg2
from datetime import datetime
import pytz

def ensure_connection(func):

    def inner(*args, **kwargs):
        with psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password) as conn:
            kwargs['conn'] = conn
            res = func(*args, **kwargs)
        return res

    return inner


@ensure_connection
def add_user(conn, user_id: int, username: str, lang: str, reg_date: str, reg_time: str, last_seen_date: str, last_seen_time: str):
    c = conn.cursor()
    c.execute("""INSERT INTO users (user_id, username, lang, reg_date, reg_time, last_seen_date, last_seen_time) VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (user_id) DO UPDATE SET 
            lang=EXCLUDED.lang,
            username = EXCLUDED.username""", (user_id, username, lang, reg_date, reg_time, last_seen_date, last_seen_time))
    conn.commit()


def getLang(user_id: int):
    print("language checked")
    conn = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)

    c = conn.cursor()
    sql_select_query = "SELECT lang FROM users WHERE user_id = %s"
    c.execute(sql_select_query, (user_id,))
    result = c.fetchone()
    lang = result[0]
    conn.close()
    return lang


def change_language(lang: str, user_id: int):
    conn = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)
    c = conn.cursor()
    sql_select_query = "UPDATE users SET lang = %s WHERE user_id = %s"
    c.execute(sql_select_query, (lang, user_id))
    conn.commit()
    conn.close()

def last_seen(user_id: int):
    time = datetime.now()
    timezone = pytz.timezone("Asia/Yerevan")
    time = timezone.localize(time)
    
    last_seen_date = time.strftime("%d/%m/%Y")
    last_seen_time = time.strftime("%H:%M:%S")
    
    conn = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)
    c = conn.cursor()
    sql_select_query = "UPDATE users SET last_seen_date = %s, last_seen_time = %s WHERE user_id = %s"
    c.execute(sql_select_query, (last_seen_date, last_seen_time, user_id))
    conn.commit()
    conn.close()
