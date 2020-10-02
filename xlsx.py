import pandas as pd

wb = pd.read_excel('pandas_column_formats.xlsx') # This reads in your excel doc as a pandas DataFrame

wb.to_html('test.html')
