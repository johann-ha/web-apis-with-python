import sqlite3 as SQL



def connect_to_sqlite():
    return SQL.connect("data/dictionary.db")


def match_exact(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for an exact match
    3. If success return the definition
    4. If not return an empty list
    """

    db = connect_to_sqlite()

    # Query the database for exact matches
    sql_query = "SELECT * FROM entries WHERE word=?"
    exact_match = db.execute(sql_query, (word,)).fetchall()

    # Close the connection to the database
    db.close()

    # Return the results
    return exact_match


def match_like(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for approximate matches
    3. If success return the definition as a list
    4. If not return an empty list
    """
    # Establish connection to the dictionary database
    db = connect_to_sqlite()

   # Query the database for partial matches
    sql_query = "SELECT * FROM entries WHERE word LIKE ?"
    partial_match = db.execute(sql_query, (f"%{word}%",)).fetchall()

    # Close the connection to the database
    db.close()

    # Return the results
    return partial_match
