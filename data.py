import pandas as pd 
import plotly.express as px
df = pd.read_csv("covid.csv")

fig = px.line(dx, x = "data",y = "cases", color = "country")
fig.show

fig=ff.create_distplot(["cases"],["casesofcovid"],show_hist=False) 
fig.show()
