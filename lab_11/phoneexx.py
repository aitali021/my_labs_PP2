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

def get_records_by_pattern():
    pattern = input("Aty, familiyasy nemese telefon nomiri boyynsha izdeu shablonyn engiziniz: ")
    cursor.execute("SELECT * FROM PhoneBook WHERE username LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR phone_number LIKE %s", 
                   ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("Jazbalar tabyldy.")

def insert_or_update_user():
    username = input("Pajdalanushy atyn engiziniz: ")
    first_name = input("Atyn engiziniz: ")
    last_name = input("Tegyn engiziniz: ")
    phone_number = input("Telefon nomiryn engiziniz: ")

    cursor.execute("SELECT * FROM PhoneBook WHERE username = %s", (username,))
    if cursor.fetchone():
        cursor.execute("""
            UPDATE PhoneBook 
            SET first_name = %s, last_name = %s, phone_number = %s 
            WHERE username = %s
        """, (first_name, last_name, phone_number, username))
        print("Pajdalanushynyn telefonyn zhanartylady.")
    else:
        cursor.execute("INSERT INTO PhoneBook (username, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s)",
                       (username, first_name, last_name, phone_number))
        print("Pajdalanushy kosyldy.")
    conn.commit()

def insert_multiple_users():
    n = int(input("Qansha pajdalanushy qosqynyz keledi? "))
    for _ in range(n):
        username = input("Pajdalanushy atyn engiziniz: ")
        first_name = input("Atyn engiziniz: ")
        last_name = input("Tegyn engiziniz: ")
        phone_number = input("Telefon nomiryn engiziniz: ")
        
        if len(phone_number) != 10 or not phone_number.isdigit():
            print(f"Kate telefon nomiri: {phone_number}. Qaita engiziniz.")
            continue

        cursor.execute("INSERT INTO PhoneBook (username, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s)",
                       (username, first_name, last_name, phone_number))
        conn.commit()
        print(f"{username} kosyldy.")

def query_data_with_pagination():
    limit = int(input("Qansha jazba korsetu kerek? "))
    offset = int(input("Qansha jazbany otkizip zhiberu kerek? "))
    cursor.execute("SELECT * FROM PhoneBook LIMIT %s OFFSET %s", (limit, offset))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print(f"Jazbalar korsetildi. Limit: {limit}, Offset: {offset}")

def delete_data():
    filter_option = input("Joyu ushin ne engizesiz? (1 - Pajdalanushy aty, 2 - Telefon nomiri): ")
    if filter_option == "1":
        username = input("Pajdalanushy atyn engiziniz: ")
        cursor.execute("DELETE FROM PhoneBook WHERE username = %s", (username,))
    elif filter_option == "2":
        phone_number = input("Telefon nomiryn engiziniz: ")
        cursor.execute("DELETE FROM PhoneBook WHERE phone_number = %s", (phone_number,))
    conn.commit()
    print("Derekter joyyldy.")

while True:
    print("\n1. Derekterdi engizu")
    print("2. Derekterdi zhanartu")
    print("3. Derekterdi betlew arqyly surau")
    print("4. Derekterdi joyu")
    print("5. Derekterdi izdew")
    print("6. Shablon boyynsha jazbalarni qaytaru")
    print("7. Exit")
    choice = input("Qaysysyn oryndaysyz? (1-7): ")
    
    if choice == '1':
        insert_or_update_user()
    elif choice == '2':
        insert_or_update_user()
    elif choice == '3':
        query_data_with_pagination()
    elif choice == '4':
        delete_data()
    elif choice == '5':
        get_records_by_pattern()
    elif choice == '6':
        get_records_by_pattern()
    elif choice == '7':
        break
    else:
        print("Qaitadan tandauz.")

cursor.close()
conn.close()
print("Jabyldy!")
