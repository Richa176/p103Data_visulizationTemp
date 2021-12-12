import pandas as pd
import plotly.express as px

df = pd.read_csv("write file name")

fig = px.scatter(df,    x="write column name",
                        y="write column name",
                        color="write column name"
            )
fig.show()
