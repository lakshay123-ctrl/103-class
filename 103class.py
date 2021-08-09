import pandas as pd 
import plotly.express as px

df = pd.read_csv("line_chart.csv")
fig = px.line(df,x = "Year",y = "Per capita income",color = "Country",title = "103 class graphs")

fig.show()

df1 = pd.read_csv("data.csv")
fig2 = px.scatter(df1,x = "Population",y = "Per capita",size = "Percentage",color = "Country",size_max=90)

fig2.show()