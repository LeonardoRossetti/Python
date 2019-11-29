import pyodbc


def read(connection):
    print('READ')
    cursor = connection.cursor()
    cursor.execute("select * from My_Table")
    for row in cursor:
        print(f' {row}')
    print()


def create(connection):
    print('CREATE')
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO My_Table(id, name) values(?, ?)", (123, 'Leo')
    )
    connection.commit()
    read(connection)


def update(connection):
    print('UPDATE')
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE My_Table SET name=? WHERE id=?;", ('Leonardo', 123)
    )
    connection.commit()
    read(connection)


def delete(connection):
    print('DELETE')
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM My_Table WHERE id=?;", 123
    )
    connection.commit()
    read(connection)


connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=MyComputer-01-SQL;"
    "Database=Test"
    "Trusted_Connection=yes"
)
