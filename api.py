import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('emo_track_responses.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
# table_exists = cursor.fetchone() is not None 
# if not table_exists:
#     cursor.execute('''CREATE TABLE emo_track_responses
#                     (id INTEGER PRIMARY KEY, Answer TEXT, Responses TEXT)''')


# Insert some data into the table
answers = ["it's okay", "you probably got this", "love you"]
bad_str = ', '.join(answers)

cursor.execute("INSERT INTO emo_track_responses (id, Answer, Responses) VALUES (?, ?, ?)", (0, "Bad", bad_str))

def getResponses(UserInput):
    # Retrieve the list of strings from the Responses column
    cursor.execute("SELECT Responses FROM emo_track_responses WHERE Answer = ?", (UserInput,))
    responses_tuple = cursor.fetchone()
    if responses_tuple is not None:
        my_string = responses_tuple[0]
        responses_list = my_string.split(",")
        random_index = random.randint(0, len(responses_list) - 1)
        response_str = responses_list[random_index]
        print(response_str)  
    else:
        print("Sorry, I don't have a response for that.")






getResponses("Bad")


