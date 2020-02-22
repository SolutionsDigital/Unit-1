from pandas import DataFrame

cars = {'Brand': ['Honda Civic', 'Toyota Corolla', 'Ford Focus', 'Audi A4'],
        'Price': [22000, 25000, 27000, 35000]
        }

# Don't forget to add '.csv' at the end of the path
df = DataFrame(cars, columns=['Brand', 'Price'])
export_csv = df.to_csv(
    r'C:\Users\mmathews\Desktop\export_dataframe.csv', index=None, header=True)
print(df)
