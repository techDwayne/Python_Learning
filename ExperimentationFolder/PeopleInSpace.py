import pandas as pd
import plotly.express as px
url='http://api.open-notify.org/astros.json'
df=pd.read_json(url)
#df['people']=df.loc['name', 'people']
df.reset_index(inplace=True)
df=df.drop(['index', 'message','number'], axis=1)
print(df)
