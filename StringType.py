print("String Type Topic")

str7="Etl Automation testing"
print("Before capitalise str7 is",str7)
print("After capitalise str7 is",str7.capitalize())
print("After title sr7 is",str7.title())
print("After capitalise str7 is",str7.upper())
print("After capitalise str7 is",str7.lower())
print("After capitalise str7 is",str7.casefold())
print("After capitalise str7 is",str7.swapcase())

txt="ETL Testing"
x=txt.center(100,'-')
print(x)

str8='BIG DATA TESTING | ETL TESTING | AUTOMATION TESTING'
print(f"Count of A in {str8}", str8.count('E'))

str1='ETL TEST'
print("Count of E", str1.count('T',1,4))

table1='emp3'
table2='dept3'
col='deptno3'

query= f""""" select * from {table1} a, {table2} b
where a.{col}=b.{col} """
print(query)

str9='ETL TESTING'
print("Ends with 'ING'", str9.endswith('TESTING'))
print("Starts with 'ING'", str9.startswith('TESTING'))

print("is alpha", str9.isalpha())
print("is alphanum", str9.isalnum())

print("is upper", str9.isupper())


columns = 'col1,col2,col3'
print("Type of Columns, Split Output, Split Output Type", type(columns), columns.split(","))