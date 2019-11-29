import utils.message

# import mysql.connector
from MySQLdb import connect


def connection(return_cursor=False):
    try:
        mydb = connect(host="localhost", user="root", passwd="Waiheke01", database="my_db")
        print(mydb.get_host_info())
        return mydb.cursor() if return_cursor else mydb
    except (Exception, AttributeError):
        print(f'Error when connecting to database.')


def read(table_name='', print_result=False):
    cursor = connection(True)
    if cursor is not None:
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        if print_result:
            showDataResult(table_name, result, cursor.description)
        return result
    else:
        print('It was not possible to access the database.')


def showDataResult(title, data, data_description):
    utils.message.showMessage(title.upper())
    # Print the columns
    for i, column_name in enumerate(data_description):
        spaces = f' ' * (int(column_name[2]) - len(column_name[0])) + '\t\t'
        print(column_name[0], end=spaces)
    print()
    # Print the data
    for row in data:
        for item in row:
            print(f"{item}", end='\t\t')
        print()


def execute_query(_query=''):
    db = connection()
    if db is not None:
        try:
            db.begin()
            db.query(_query)
            db.commit()
        except Exception as e:
            print(f'Error when creating data. Details: {e}')
        finally:
            db.close()
    else:
        print('It was not possible to access the database.')


def update(_query=''):
    db = connection()
    if db is not None:
        try:
            db.begin()
            db.query(_query)
            db.commit()
        except Exception as e:
            print(f'Error when creating data. Details: {e}')
        finally:
            db.close()
    else:
        print('It was not possible to access the database.')


# execute_query("INSERT INTO users (name, status, birth) VALUES ('Leo', '1', '1995-01-12')")


newName = 'Leonardo Rossetti'
id = 2
# execute_query(f"UPDATE users SET name = '{newName}' WHERE id={id}")


# execute_query(f"DELETE FROM users WHERE id = {id}")

users = read("users", print_result=True)


