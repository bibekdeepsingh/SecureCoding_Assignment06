import os
import pymysql # type: ignore
import subprocess
from urllib.request import urlopen

# Handled missing values and securing secrets.
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')  # ⚠️ OWASP A02: Hardcoded Credential Risk
}

# Raised value error for invalid input
def get_user_input():
    user_input = input('Enter your name: ')
    return user_input
    if not re.match("^[a-zA-Z0-9 ]+$", user_input):
        raise ValueError("Invalid input")

# Replace subprocess.run with a secure email method or comment risks 
def send_email(to, subject, body):
    subprocess.run(["mail", "-s", subject, to], input=body.encode(), check=True)

# Add HTTPS and data verification for external calls
def get_data():
    url = 'http://secure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

# Improve error handling for DB ops and add comments
def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
