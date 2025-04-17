import psycopg2




conn = psycopg2.connect(
    dbname="postgres",  
    user="postgres",    
    password="12345",   
    host="localhost",   
    port="5432"         
)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone_number VARCHAR(20)
    );
''')
conn.commit()
print("PhoneBook jasaldy.")
def insert_data():
    username = input("User Aty: ")
    first_name = input("Esimin ")
    last_name = input("Tegi: ")
    phone_number = input("Telephone number: ")
    cursor.execute("INSERT INTO PhoneBook (username, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s)",
                   (username, first_name, last_name, phone_number))
    conn.commit()
    print("engizildi")
def update_data():
    username = input("Jana User Aty: ")
    new_first_name = input("Jana Aty: ")
    new_phone_number = input("Jana Telephone number: ")
    cursor.execute("""
        UPDATE PhoneBook 
        SET first_name = %s, phone_number = %s 
        WHERE username = %s
    """, (new_first_name, new_phone_number, username))
    conn.commit()
    print("derekter janartyldy.")
def query_data():
    filter_option = input("derekterdy qalay sorttau kerek? (1 - User Aty, 2 - Telephone number): ")
    if filter_option == "1":
        username = input("User Aty engiz: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE username = %s", (username,))
    elif filter_option == "2":
        phone_number = input("Telephone number engiz: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE phone_number = %s", (phone_number,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("derekter sorttaldy")
def delete_data():
    filter_option = input("to delete? (1 - User Aty, 2 - Telephone number): ")
    if filter_option == "1":
        username = input("User Aty engiz: ")
        cursor.execute("DELETE FROM PhoneBook WHERE username = %s", (username,))
    elif filter_option == "2":
        phone_number = input("Telephone number engiz: ")
        cursor.execute("DELETE FROM PhoneBook WHERE phone_number = %s", (phone_number,))
    conn.commit()
    print("derekter deleted")
while True:
    print("\n1. derekterdi engizu")
    print("2. derekterdi janartu")
    print("3. derekterdi sorttau")
    print("4. derekterdi joyu")
    print("5. exit")
    choice = input("qaisysyn oryndaisyz? (1-5): ")
    if choice == '1':
        insert_data()
    elif choice == '2':
        update_data()
    elif choice == '3':
        query_data()
    elif choice == '4':
        delete_data()
    elif choice == '5':
        break
    else:
        print("qaitadan tanda")
cursor.close()
conn.close()
print("jabyldy!")
