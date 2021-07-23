
import pandas
import plotly.express as px
read=pandas.read_csv("D:\Daksh\WhiteHatJr\projects whitehat\C103\Copy+of+data+-+data.csv")
fig=px.scatter(read,x="date",y="cases",color="country")
fig.show()










