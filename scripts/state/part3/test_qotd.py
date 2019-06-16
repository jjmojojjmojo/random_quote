"""
Test the "Quote of the day" functionality.
"""

import pytest
import sqlite3
import datetime

def get_quote_id(conn, day, month, year):
    """
    Helper function to get a quote id for the given day/month/year
    """
    c = conn.cursor()

    c.execute("SELECT quote_id FROM quote_of_the_day WHERE day = ? AND month = ? AND year = ?", (day, month, year))

    result = c.fetchone()

    return result[0]

def test_add_qotd(preconfigured_manager):
    """
    Add a new quote of the day, for the current day.
    """
    today = datetime.datetime.now()

    quote = preconfigured_manager.qotd.add()

    check = get_quote_id(preconfigured_manager.conn, today.day, today.month, today.year)

    assert check == quote["quote_id"]

def test_add_qotd_with_date(preconfigured_manager):
    """
    Add a new quote of the day, for a given day.
    """
    date = datetime.datetime(day=1, year=2025, month=3)

    quote = preconfigured_manager.qotd.add(date)

    check = get_quote_id(preconfigured_manager.conn, 1, 3, 2025)

    assert check == quote["quote_id"]

def test_add_duplicate(preconfigured_manager):
    """
    Try to add an additional quote of the day.
    """
    date = datetime.datetime(day=1, year=2025, month=3)

    preconfigured_manager.qotd.add(date)

    with pytest.raises(sqlite3.IntegrityError):
        preconfigured_manager.qotd.add(date)

def test_get_without_date(preconfigured_manager):
    """
    Get a quote of the day, no date specified. Should create a new QOTD.
    """
    today = datetime.datetime.now()

    quote = preconfigured_manager.qotd.get()

    check = get_quote_id(preconfigured_manager.conn, today.day, today.month, today.year)

    assert check == quote["quote_id"]

def test_get_with_date(preconfigured_manager):
    """
    Get a quote of the day, for a specified date. Should create a new QOTD.
    """
    date = datetime.datetime(day=1, year=2025, month=3)

    quote = preconfigured_manager.qotd.get(date)

    check = get_quote_id(preconfigured_manager.conn, 1, 3, 2025)

    assert check == quote["quote_id"]

def test_all(preconfigured_manager):
    """
    Add and retrieve several quotes of the day.
    """
    date1 = datetime.datetime(day=1, year=2025, month=3)
    date2 = datetime.timedelta(days=1) + date1
    date3 = datetime.timedelta(days=1) + date2

    quote1 = preconfigured_manager.qotd.add(date1)
    quote2 = preconfigured_manager.qotd.add(date2)
    quote3 = preconfigured_manager.qotd.add(date3)

    result = preconfigured_manager.qotd.all()

    assert result[0] == quote1
    assert result[1] == quote2
    assert result[2] == quote3