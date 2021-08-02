# Data-Stream-Project
The first is a data integration which provides lists of users as potential leads for purchasing of Widgets. Every day a new list of leads are deposited on S3 by a marketing partner, and the leads must be processed in order to determine how they should be contacted. The existing lead integration hub is a RabbitMQ cluster, and the Office of Architecture has decreed that this integration must maintain that approach. In addition, existing marketing integrations rely on a message routing approach to ship leads to different databases which support the sales teams. If a lead is in the United States then they should be put into a PostgreSQL database table named leads. If they are not and they have a known CC number, then they should go into a database table named high_priority, and otherwise all leads should be deposited into a text file. This plan must be expressed using the EIP symbols for draw.io and deployed to AWS cloud.
Assignment Guidelines:

    List of leads are deposited on S3

    List of leads are parsed using JSON
    Leads determine how they should be contacted

    Filter Data

    Queues the filtered data to correct databases/files

    Leads rely on a message routing approach to ship leads to different databases which support the sales teams:

    If a lead is in the United States then they should be put into a PostgreSQL database table named leads.
    If they are not and they have a known CC number, then they should go into a database table named high_priority.
    Otherwise, all leads should be deposited into a text file.

    Send and receive the filtered data into queues using RabbitMQ

    We will use two channels and three queues.
    For the database, we will use two queues, one for high priority and one for leads in the US. We will receive the data via each channel and it will be deposited into the database.
    For the text file, we will have one queue. We will receive the data via each channel and it will be deposited into the leads.txt file.

    Setting up the PostgreSQL database for lead deposits

List of Leads are deposited on S3

Use boto3, Amazon Web Services (AWS) Software Development Kit (SDK) for Python, to download the leads from the S3 bucket.
Parse leads using JSON

Here Using JSON we are cleaning the user data like id, first name, last name, email, gender, ip_address, cc, country, birthdate, salary, title.
Filter Data

Leads rely on a message routing approach to ship leads to different databases which support the sales teams:

    If a lead is in the United States then they should be put into a PostgreSQL database table named leads.
    If they are not and they have a known CC number, then they should go into a database table named high_priority.
    Otherwise, all leads should be deposited into a text file.

RabbitMQ

Using the Python client, Pika, create three channels and two queues for the leads. There should be two channels dedicated to sending leads into the database queue and one channel dedicated to sending the the text file queue. When you recieve the leads, this is when you connect to either the database or the text file to dump the leads into its desired location.
PostgreSQL database

PostgreSQL is a general-purpose object-relational database management system. It allows you to add custom functions developed using different programming languages such as C/C++, Java, etc. ... In PostgreSQL, we can define your own data types, index types, functional languages.
Deploying Locally

    Open your terminal
    Start the RabbitMQ server
    Run receiveData.py
    Run the data_source.py file