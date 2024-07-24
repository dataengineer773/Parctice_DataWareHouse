# Create a database named practice :
createdb -h localhost -U postgres -p 5432 practice


# In the practice database, create a schema using star-schema.sql :
psql -h localhost -U postgres -p 5432 practice < star-schema.sql




# In the practice database, load the data into all tables using the DimMonth.sql, DimCustomer.sql and FactBilling.sql:
psql  -h localhost -U postgres -p 5432 practice < DimMonth.sql
psql  -h localhost -U postgres -p 5432 practice < DimCustomer.sql
psql  -h localhost -U postgres -p 5432 practice < FactBilling.sql




# Verify that you have correctly loaded the data into the practice database :
psql  -h localhost -U postgres -p 5432 practice < verify.sql




