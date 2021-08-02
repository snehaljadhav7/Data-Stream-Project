import pandas as pd
import json, csv
import boto3
import io

def download_from_s3():
    KEY = 'userdata2.csv'
    BUCKET = 'leads-info-project' 
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket = BUCKET, Key = KEY)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='utf8')
    df.to_csv('userdata.csv', index=False)
    csvfile = open('userdata.csv', 'r')
    reader = csv.DictReader(io.StringIO(csvfile.read()))
    json_data = json.dumps(list(reader))
    return json_data




def data_distribution(data):
    leads_table = []
    high_priority_table = []
    file_data = []
    leads = json.loads(data)
    for lead in leads:
        lead["comments"] = ""
        if lead["country"] == "United States":
            leads_table.append(lead)   
        elif lead["cc"]:
            high_priority_table.append(lead)
        else:
            file_data.append(lead)

   



data = download_from_s3()
data_distribution(data)














