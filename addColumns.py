import pandas as pd
import xlwt
import openpyxl
# List of Tuples
empSalary = [('Jack', 2000, 2010, 2050, 2134, 2111),
             ('Riti', 3000, 3022, 3456, 3111, 2109),
             ('Aadi', 4022, 4022, 2077, 2134, 3122),
             ('Mohit', 3012, 3050, 2010, 2122, 1111),
             ('Veena', 2023, 2232, 4022, 2112, 1099),
             ('Shaun', 2123, 2510, 3050, 3134, 2122),
             ('Mark', 4000, 2000, 2050, 2122, 2111)
             ]


# Create a DataFrame object
df = pd.DataFrame(empSalary,
                  columns=['Name', 'Jan', 'Feb', 'March', 'April', 'May'])
df.set_index('Name',
             inplace=True)
print(df)

# Add two columns together to make a new series
total = df['Jan'] + df['May']
print('total of Jan & May')
print(total)


# Add two columns to make a new column
df['Jan_May'] = df['Jan'] + df['May']
print('Updated DataFrame with new Col:')
print(df)

df.to_excel('df_to_excel.xlsx', sheet_name='sheet1')
