# Amazon_Vine_Analysis

## Overview 

## Resources
### Data Source 
- 

### Software
- 


## Results
### Deliverable 1: Perform ETL on Amazon Product Reviews
Using the cloud ETL process, an AWS RDS database with tables in pgAdmin will be created, a dataset from the [Amazon Review datasets](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt) will be picked and extracted into a DataFrame. The DataFrame will be transformed into four separate DataFrames that match the table schema in pgAdmin. Then, the transformed data will be uploaded into the appropriate tables and queries will be run in pgAdmin to confirm that the data has been uploaded.

1. An Amazon Review dataset is extracted as a DataFrame:

2. The extracted dataset is transformed into four DataFrames with the correct columns:

3. All four DataFrames are loaded into their respective tables in pgAdmin:


### Deliverable 2: Determine Bias of Vine Reviews
Using PySpark, Pandas, or SQL, we’ll determine if there is any bias towards reviews that were written as part of the Vine program. For this analysis, we'll determine if having a paid Vine review makes a difference in the percentage of 5-star reviews.

1. There is a DataFrame or table for the vine_table data using one of three methods above:

2. The data is filtered to create a DataFrame or table where there are 20 or more total votes:

3. The data is filtered to create a DataFrame or table where the percentage of helpful_votes is equal to or greater than 50%:

4. The data is filtered to create a DataFrame or table where there is a Vine review:

5. The data is filtered to create a DataFrame or table where there isn’t a Vine review:

6. The total number of reviews, the number of 5-star reviews, and the percentage 5-star reviews are calculated for all Vine and non-Vine reviews:

### Deliverable 3: A Written Report on the Analysis

1. How many Vine reviews and non-Vine reviews were there?
2. How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars?
3. What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?

## Summary 
In your summary, state if there is any positivity bias for reviews in the Vine program. Use the results of your analysis to support your statement. Then, provide one additional analysis that you could do with the dataset to support your statement.

1. The summary states whether or not there is bias, and the results support this statement 
2. An additional analysis is recommended to support the statement
