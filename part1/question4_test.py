from pets_db import create_db, get_connection
from question4 import sql_pets_owned_by_nobody, sql_only_owned_by_bessie, sql_pets_older_than_owner


def test_question4_pets_older_than_owner():
    create_db()

    with get_connection() as con:
        res = con.execute(sql_pets_older_than_owner)
        result = res.fetchone()

    assert len(result) == 1
    assert result[0] == 2


def test_question4_pets_owned_by_nobody():
    create_db()

    with get_connection() as con:
        res = con.execute(sql_pets_owned_by_nobody)
        rows = res.fetchall()

    rows.sort()

    assert len(rows) == 2
    assert rows[0] == ('petey', 'gray whale', 38)
    assert rows[1] == ('shannon', 'cow', 14)


def test_question4_only_owned_by_bessie():
    create_db()

    with get_connection() as con:
        res = con.execute(sql_only_owned_by_bessie)
        rows = res.fetchall()

    rows.sort()

    assert len(rows) == 2
    assert rows[0] == ('bessie', 'leyla', 'gray whale')
    assert rows[1] == ('bessie', 'randolph', 'lemur')
