"""
Generate a random quote of the day.
"""
import sqlite3
import datetime

from . import util

class QuoteOfTheDay:
    def __init__(self, db_filename, manager=None):
        if manager is None:
            from .manager import RandomQuoteManager
            self.manager  = RandomQuoteManager(db_filename)
        else:
            self.manager = manager

        self.conn = util.connection(db_filename)

    def _date_parts(self, date=None):
        """
        Helper method to convert a date to the day/month/year that is
        stored in the database.
        """
        if date is None:
            date = datetime.datetime.now()

        return (date.day, date.month, date.year)

    def get(self, date=None):
        """
        Return the quote of the day for a given date, or the current date
        if one isn't specified.

        If no quote exists for that date, one is generated and saved.
        """
        day, month, year = self._date_parts(date)

        c = self.conn.cursor()

        c.execute("""
                  SELECT quotes.quote,
                         quotes.created,
                         qotd.quote_id,
                         qotd.day,
                         qotd.month,
                         qotd.year
                    FROM quotes, quote_of_the_day as qotd
                   WHERE quotes.id = qotd.quote_id
                     AND day=?
                     AND month=?
                     AND year=?
                  """,
                  (day, month, year))

        result = c.fetchone()

        if result is None:
            return self.add(date)
        else:
            return dict(result)

    def add(self, date=None):
        """
        Add a quote of the day for a given date, or the current date
        if one isn't specified.
        """
        day, month, year = self._date_parts(date)

        quote = self.manager.random()

        c = self.conn.cursor()

        c.execute("""
            INSERT INTO quote_of_the_day
                        (quote_id, day, month, year)
                 VALUES (?, ?, ?, ?)
           """,
           (quote["id"], day, month, year))

        self.conn.commit()

        return {
            'quote_id': quote['id'],
            'quote': quote['quote'],
            'created': quote['created'],
            'day': day,
            'month': month,
            'year': year
        }

    def all(self):
        """
        Retrieve all existing quotes of the day.
        """
        c = self.conn.cursor()

        c.execute("""
                  SELECT quotes.quote,
                         quotes.created,
                         qotd.quote_id,
                         qotd.day,
                         qotd.month,
                         qotd.year
                    FROM quotes, quote_of_the_day as qotd
                   WHERE quotes.id = qotd.quote_id
                ORDER BY qotd.year, qotd.month, qotd.day
                  """)

        result = []

        for row in c.fetchall():
            result.append(dict(row))

        return result