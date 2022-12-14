# Amazon_Vine_Analysis

## Overview 
Since the work with the SellBy project was so successful, we will now be analyzing Amazon reviews written by members of the paid Amazon Vine program in order to present it to the SellBy stakeholders. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies like SellBy pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review. The Amazon Review Datasets consists of approximately 50 datasets and each contains reviews of a specific product, from clothing apparel to wireless products. For this analysis, we will select one of these datasets and use PySpark to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin. Then, PySpark, Pandas, or SQL will be used to determine if there is any bias toward favorable reviews from Vine members in the selected dataset. 

## Resources
### Data Source 
-  Amazon Review [Datasets](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt)
    - Amazon [Book Reviews](https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Books_v1_02.tsv.gz)

### Software
- PostgreSQL and pgAdmin 6.8
- Google Colaboratory and Python 3.7.6
- Visual Studio Code 1.69

## Results
### Deliverable 1: Perform ETL on Amazon Product Reviews
Using the cloud ETL process, an AWS RDS database with tables in pgAdmin will be created, a dataset from the [Amazon Review datasets](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt) will be picked and extracted into a DataFrame. The DataFrame will be transformed into four separate DataFrames that match the table schema in pgAdmin. Then, the transformed data will be uploaded into the appropriate tables and queries will be run in pgAdmin to confirm that the data has been uploaded. The completed Amazon_Reviews_ETL Google Colab notebook can be referenced [here](https://github.com/lkachury/Amazon_Vine_Analysis/blob/main/Amazon_Reviews_ETL.ipynb).

1. An Amazon Review dataset is extracted as a DataFrame: <br /> ![image](https://user-images.githubusercontent.com/108038989/197368910-2cda65d4-d91d-466f-a3af-5759b7b98a65.png)

2. The extracted dataset is transformed into four DataFrames with the correct columns:
  - ![image](https://user-images.githubusercontent.com/108038989/197368941-64710340-7026-4639-8db2-524d1d42ab72.png)
  - ![image](https://user-images.githubusercontent.com/108038989/197368951-7f9e722b-8b4a-4740-b776-f9eb6031fe1a.png)
  - ![image](https://user-images.githubusercontent.com/108038989/197368960-03de0ff5-efdb-4d31-9a0f-12c72fbf4165.png)
  - ![image](https://user-images.githubusercontent.com/108038989/197368965-2e0d1521-73fd-4c34-8e35-5d8c497b5e97.png)

3. All four DataFrames are loaded into their respective tables in pgAdmin:
  - ![image](https://user-images.githubusercontent.com/108038989/197367003-4fd169b0-3a8b-4dbd-857c-4f8b211fbfa9.png)
  - ![image](https://user-images.githubusercontent.com/108038989/197367106-6a304499-a719-4f02-91d2-848a7dac8cbc.png)
  - ![image](https://user-images.githubusercontent.com/108038989/197367397-8010e696-4230-4b65-87d5-79c825f419be.png)
  - ![image](https://user-images.githubusercontent.com/108038989/197368811-b050063a-c02d-4e51-9877-b878a5333a58.png)

### Deliverable 2: Determine Bias of Vine Reviews
Using PySpark, Pandas, or SQL, we???ll determine if there is any bias towards reviews that were written as part of the Vine program. For this analysis, we'll determine if having a paid Vine review makes a difference in the percentage of 5-star reviews. The completed Vine_Review_Analysis Google Colab notebook can be referenced [here](https://github.com/lkachury/Amazon_Vine_Analysis/blob/main/Vine_Review_Analysis.ipynb)

1. There is a DataFrame or table for the vine_table data using one of three methods above:
<br /> ![image](https://user-images.githubusercontent.com/108038989/197371706-2e85bfe0-c470-4aae-b992-9a10758cfaaa.png)
<br /> ![image](https://user-images.githubusercontent.com/108038989/197371722-4618708a-947a-4b45-9a09-85a5fa44936e.png)

2. The data is filtered to create a DataFrame or table where there are 20 or more total votes:
<br /> ![image](https://user-images.githubusercontent.com/108038989/197371736-7f8f093c-1ae3-4a41-8cb1-d6a0de789355.png)

3. The data is filtered to create a DataFrame or table where the percentage of helpful_votes is equal to or greater than 50%:
<br /> ![image](https://user-images.githubusercontent.com/108038989/197371749-41ced94c-6333-4609-af59-77dbba2a9a66.png)

4. The data is filtered to create a DataFrame or table where there is a Vine review:
<br /> ![image](https://user-images.githubusercontent.com/108038989/197371999-8c797b00-a99d-4d0b-b8b3-985df1b71936.png)

5. The data is filtered to create a DataFrame or table where there isn???t a Vine review:
<br /> ![image](https://user-images.githubusercontent.com/108038989/197371819-2dca8afd-f023-4e6a-a0b1-46149241cc6c.png)

6. The total number of reviews, the number of 5-star reviews, and the percentage 5-star reviews are calculated for all Vine (Paid) and non-Vine (Unpaid) reviews:
    - ![image](https://user-images.githubusercontent.com/108038989/197377396-001cdaee-81db-4e77-bc1c-0a46c2b1796d.png)
    - ![image](https://user-images.githubusercontent.com/108038989/197377406-e584676b-b025-4211-9744-532182490775.png)
    - ![image](https://user-images.githubusercontent.com/108038989/197377421-1cd62fb6-c002-4c05-a5af-4b464a38f121.png)

## Summary 
The purpose of this analysis was to determine if there was any bias toward favorable reviews from Vine members in the selected Amazon Review dataset. The dataset was filtered and a new DataFrame was created that displayed all the rows where the total_votes count was equal to or greater than 20 to pick reviews that were more likely to be helpful and to avoid having division by zero errors. This new DataFrame was filtered and a new DataFrame was created that displayed all the rows where the number of helpful_votes divided by total_votes is equal to or greater than 50%. 

From the analysis performed in Deliverable 2 above, the percentage of 5 stars Non-Vine (Unpaid) reviews is 60.15% while the percentage of 5 stars Vine (Paid) reviews is 0%. Since 5 stars Non-Vine reviews have a higher percentage than 5 stars Vine reviews, the results indicate that there is no positivity bias for reviews in the Vine program.  

One additional analysis that is recommedned with the dataset to support this statement is to perform percentage calculations for the remaining star ratings. Based on the Deliverable 2 results above, the remaining star ratings comprise roughly 40% of the dataset and we might expect to see similar rsults between the Vine (Paid) and Non-Vine (Unpaid) reviews of star ratings 1 through 4.
