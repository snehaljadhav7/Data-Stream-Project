import pika

def send_to_DB(leads_table, high_priority_table):
     
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='db_leads_table')
    channel.queue_declare(queue='db_high_priority_table')
    

    def send_to_leads_table(leads_table):
        for lead in leads_table:
            channel.basic_publish(exchange='', routing_key='db_leads_table', body=str(lead))

    def send_to_high_priority_table(high_priority_table):
       for lead in high_priority_table: 
            channel.basic_publish(exchange='', routing_key='db_high_priority_table', body=str(lead))

    send_to_leads_table(leads_table)
    send_to_high_priority_table(high_priority_table)
    connection.close()


def send_to_file(file_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel() 

    channel.queue_declare(queue='file_leads')
    def send_to_txt(file_data):
        for lead in file_date:
            channel.basic_publish(exchange='', routing_key='file_leads', body=str(lead))
    connection.close()



