import sqlite3

# Connect to the database
conn = sqlite3.connect('reponses.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE string_responses
                  (id INTEGER PRIMARY KEY, Answer TEXT, Responses TEXT)''')


# Insert some data into the table
answers = ["it's okay", "you probably got this", "love you"]
bad_str = ', '.join(answers)

cursor.execute("INSERT INTO string_responses (Answer, Respones) VALUES (?, ?)", ('Bad', bad_str))


