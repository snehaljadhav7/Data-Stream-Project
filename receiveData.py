
import pika
import psycopg2
from parser import binary_to_json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def callback_leads(ch, method, properties, body):
    item = binary_to_json(body)
    connect(item, high_priority=False)



def callback_high_priority(ch, method, properties, body):
    item = binary_to_json(body)
    connect(item, high_priority=True)

def callback(ch, method, properties, body):
  

    item = binary_to_json(body)
    f = open("leads.txt", "a")
    f.write(str(item))
    f.write('\n')
    f.close()



def connect(item, high_priority):
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="userdata", user="postgres", password="postgres")

     
        cur = conn.cursor()
        id = item["id"]
        first_name = item["first_name"]
        last_name =  item["last_name"]
        email = item["email"]
        gender = item["gender"]
        ip_address = item["ip_address"]
        cc = item["cc"]
        country = item["country"]
        birthdate = item["birthdate"]
        salary = item["salary"]
        title = item["title"]

        if birthdate == '':
            birthdate = '01-01-2018'
        if salary == '':
            salary = 0
        else:
            salary = salary.replace("$",'')
            salary = float(salary)
        if cc == '':
            cc = 0

        my_sql_leads = 'INSERT INTO Leads(id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)'
        my_sql_high_priority = 'INSERT INTO high_priority(id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)'
        record_tuple = (id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title)
        if high_priority:
            cur.execute(my_sql_high_priority, record_tuple)
        else:
            cur.execute(my_sql_leads, record_tuple)
        conn.commit()
        print("Record inserted successfully into the table")
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')





channel.basic_consume(queue='db_leads_table', auto_ack=True, on_message_callback=callback_leads)
channel.basic_consume(queue='db_high_priority_table', auto_ack=True, on_message_callback=callback_high_priority)
channel.basic_consume(queue='file_leads', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()




