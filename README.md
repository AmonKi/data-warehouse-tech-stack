# data-warehouse-tech-stack
This project utilizes MySQL, dbt, Airflow and spark to extract data from the sensors, store data in the warehouse, perform transformations and data analysis.
# Data Pipeline
ELT was the most appropriate, that is, we extract data obtained from the sensors, load it to the warehouse, and then perform the transformations. This is because of uncertainty of business needs, therefore, data will be available in the warehouse for any transformation to suit a specific need.
# Airflow
The DAG script was used to schedule when to run the load_data.py once to load data into the warehouse, MySQL database.
# Data Build Tool (dbt)
Data build tool(dbt) is a data engineering tool used primarily for T (transformations) in ELT process. Here, various model codes were written to transform data into varied formats.

