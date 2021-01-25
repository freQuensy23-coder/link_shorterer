import pymysql
from pymysql.cursors import DictCursor
import config
import logging
import time
from base64 import encodestring
import Core

log = logging.getLogger("db")


class DB:
    def __init__(self):
        self.connection = pymysql.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            db=config.db,
            charset='utf8',
            cursorclass=DictCursor
        )
        self.__cursor = self.connection.cursor()
        timeout = 2147482
        self.__cursor.execute(query=f"""SET SESSION wait_timeout := {timeout};""")
        self.connection.commit()
        log.debug("db inited")

    def add_new_short_link(self, redirect_to, user_id=0):
        """Add new shor link"""
        link = Core.generate_rand_hash()
        cur = self.__cursor()
        q = f"""INSERT into 
                redirect_map(user_id, redirect_to , link)
                VALUES
                {user_id}, {redirect_to}, {link}
                """
        cur.execute(q)
        return link

    def get_redirection_link(self, short_link: str):
        cur = self.connection.cursor()
        q = f"""SELECT * from redirect_map
                WHERE short_link = {short_link}
                """
        cur.execute(q)
        try:
            return cur.fetchone()["redirect_to"]
        except NameError:
            return None
