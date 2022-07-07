### Introduction to Cloud Computing

### CS 552

### PROJECT REPORT

#### Title: ETL Pipeline Simulation of AWS


### CONTENTS


### Background and Motivation:
    To develop a simulated model from scratch using Python
Pandas and run it in DockerHub which is like AWS Glue.
Orchestration of implemented pipeline will be done on
Kubernetes (minikube).
Considering our natural interest in the Stock market and
investment we have used the Deutsche Bank trading data set
to perform ETL operations over it. The issue is that available
financial data is not always in the accurate format to take
trading decisions. To solve this problem, we are building an
ETL pipeline that will extract any given data, later it’ll pass
through our pipeline. ETL transformations will bring that data in
shape and form for trading stocks.
In the process of transforming this data, we will also learn
Docker Hub, and Kubernetes in detail and how any Cloud
service works behind the curtains of UI and understand it
deeper while implementing it on our own.


### PROJECT DESCRIPTION:
    Written in Python using Pandas Library, our ETL pipeline
will extract Deutsche Bank data and put it in AWS S3 bucket.
From Amazon S3 pipeline, we transform the data to remove
unnecessary columns. Transform operation will also add
needed columns into it like ‘Min- Price’, ‘Max-Price’, ‘Trading
Volume’, ‘Price difference in percentage’ and then store that
data in the other S3 pipeline
To dive deep into transactions we had data of the price of
a stock for minute-by-minute transactions in the day. Our
transformations have the intention of taking all that data into
consideration and concisely into a valuable-short format. To
start with this intention first we have used ‘for’ for loop to get
the ‘Max-Price’ of the stock of that day and similarly
‘Minimum-Price’, using these two values we come up with the
‘Price Difference in Percentage’ by comparing the closing


rate of the previous day and the current day rate at the end
of the day. But one more parameter is important in trading
which is Volume. To get this value we have concatenated all
the shares that have been either bought or sold which
together is called ‘Trading Volume’ of the day for one
particular stock of this entire transformation
Before and after these ETL transformations we have used
AWS S3 buckets to store ‘Source’ and ‘Target’ data. Data
flow for these buckets starts from open-source data set of
Deutsche Bank which we extracted and stored in S3 source-
bucket which intern flew through our data pipeline. Output of
our data pipeline is then stored back into S3 target bucket.
Together these S3 buckets and our ETL pipeline in-acts
‘AWS Glue service’ which was the core intention of this
project, to understand an AWS service and simulate it from
scratch. The output of our pipeline is shown in further topics
of the report.


‘Profiling’ is an important topic of any AWS service which
virtualized details of processing time and data used by a
given service. This is an extremely important aspect that
determines the efficiency and capacity of any cloud-based
service.

## Project Model:

Below is our project model as per above description -
![image](https://user-images.githubusercontent.com/90517477/177386749-1a2c9882-63e1-4005-9e41-4232485d9c8e.png)



### OVERVIEW OF AWS GLUE

AWS Glue is an ETL (extract, transform, and load) solution
that is completely managed by AWS. Data analysis and
categorization are one of its primary capabilities. AWS Glue
crawlers may deduce database and table structure from your
Amazon S3 data and save the accompanying metadata in the
AWS Glue Data Catalog.

Athena stores and retrieves table information for Amazon
S3 data in your Amazon Web Services account using the AWS
Glue Data Catalog. The table metadata tells the Athena query
engine where to look for, read, and analyze the data you're
interested in.

You may run an AWS Glue crawler from inside Athena on a
data source or conduct Data Definition Language (DDL)
queries directly in the Athena Query Editor to generate
database and table schema in the AWS Glue Data Catalog.
Then, using the database and table structure you developed,
you may query the data using Data Manipulation (DML) queries
in Athena.


### DEUTSCH BÖRSE DATASET
The Deutsche Börse Public Dataset (PDS) project makes
near-time data derived from Deutsche Börse's trading systems
available to the public for free.

This data is provided on a minute-by-minute basis and
aggregated from the Xetra and Eurex engines, which
comprise a variety of equities, funds, and derivative securities.
The PDS contains details on a per security level, detailing
trading activity by minute including the high, low, first and last
prices within the time-period.

The PDS is created using a cloud provider's infrastructure
and made available through their public data repository
initiatives, such as the AWS Public Dataset project.

Deutsche Börse Group believes that freely available, high-
quality data fosters innovation and creates business
opportunities. The financial community, academic researchers,
data scientists, and others can explore the possibilities of the
data to open new analysis and product possibilities.

(^)
(^)
(^)
(^)


(^)
(^)
Constraints on the Dataset –
(^)
 Non-trading Hours v/s Missing Data

- There will be hours during the day when there will be no
    trading activity. To help data consumers distinguish between what may be missing data and normal non-
    trading conditions, CSV files containing only headers are emitted to positively identify normal, non-trading

conditions.

Calendar –

Trading data is currently available as far back as June 26th
2017 for Xetra, and May 29th 2017 for Eurex. Additional
historical data may be made available in the future, depending
on demand.


### Raw stock trading activity –

![image](https://user-images.githubusercontent.com/90517477/177387101-b48c97df-cb3a-4670-8b70-62cf6ce1a8ef.png)

### Final processed data –
![image](https://user-images.githubusercontent.com/90517477/177387145-7abf9c90-3778-4c82-a482-53f7305221f3.png)


#####  PROFILING IN PYTHON

Profiling is a set of statistics that describes how often and
for how long various parts of the program executed.

It can help to avoid that crash and burn outcome, since it
provides a fairly accurate view of what our program is doing.

Here, we have used profiling to analyze the runtime stock
trading activity as follows –

Case 1: When there is no trading activity:
In this case, no file will be written, and no file will be updated.

![image](https://user-images.githubusercontent.com/90517477/177387201-f45c091d-c36c-4b69-99da-621aca84cad5.png)


Case 2: When trading activity is present
![image](https://user-images.githubusercontent.com/90517477/177387322-3b6e5d47-4796-4948-a150-607f446fdc53.png)


##### RESULTS

1.Extracting the data:
Here we are extracting the Xetra source file which is a public
dataset and reading the file which is stored in the source AWS
S3 bucket


2.Transforming the data:
Here we have applied transformations to the dataset and
which is completed after reading the data from the source
bucket and then all the user defined transformations will be
applied.

3.Loading the data:
After applying all the transformations, now the data will be
written to the target S3 bucket and will be available for the
public for further analysis


Storing the final report file in AWS S3 bucket


