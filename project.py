# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
df = pd.read_csv (r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2012_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
# %%
latitude_data= df['Latitude'].tolist()
longitude_data=df['Longitude'].tolist()
#%%
x = df["Longitude"]
y = df["Latitude"]
# %%
plt.xlabel("Latitude", fontsize=20)
plt.ylabel("Longitude", fontsize=20)
#%%
plt.xlabel("Latitude", fontsize=20)
plt.ylabel("Longitude", fontsize=20)
#%%
plt.scatter(x, y)
plt.show()
#FIELD COORDINATES
# %%
import plotly.graph_objects as go
import pandas as pd
# %%
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2012_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Elevation: ' + df['Elevation(ft)'].apply(str)
df['Elevation(ft)'] = df['Elevation(ft)'].astype(float)
#%%
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            colorscale = 'Blues',
            cmin = df['Elevation(ft)'].min(),
            color = df['Elevation(ft)'],
            cmax = df['Elevation(ft)'].max(),
            colorbar_title='Elevation (ft)'
        )))
fig.update_layout(
        title = 'Elevation Map from 2012 Field Data',
        geo_scope='usa',
    )
fig.update_geos(fitbounds = 'locations')
fig.update_layout(height=400, margin={'r':0,'t':0,'l':0,'b':0})
fig.write_html('plotly_j4.html')
fig.show()
#ELEVATION MAP 2012
# %%
import plotly.graph_objects as go
import pandas as pd
# %%
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2012_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Yield Mass (Dry)(lb/ac): ' + df['Yield Mass (Dry)(lb/ac)'].apply(str)
df['Yield Mass (Dry)(lb/ac)'] = df['Yield Mass (Dry)(lb/ac)'].astype(float)
#%%
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            cmin = df['Yield Mass (Dry)(lb/ac)'].min(),
            color = df['Yield Mass (Dry)(lb/ac)'],
            cmax = df['Yield Mass (Dry)(lb/ac)'].max(),
            colorbar_title='Yield Mass (Dry)(lb/ac)'               
        )))
fig.update_layout(
        title = 'Elevation Map from 2012 Field Data',
        geo_scope='usa',
    )
fig.update_geos(fitbounds = 'locations')
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.write_html('plotly_j5.html')
fig.show()
#YIELD MASS 2012
#%%
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2011_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Yield Mass (Dry)(lb/ac): ' + df['Yield Mass (Dry)(lb/ac)'].apply(str)
df['Yield Mass (Dry)(lb/ac)'] = df['Yield Mass (Dry)(lb/ac)'].astype(float)
# %%
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2011_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Estimated Volume (Dry)(bu/ac): ' + df['Estimated Volume (Dry)(bu/ac)'].apply(str)
df['Estimated Volume (Dry)(bu/ac)'] = df['Estimated Volume (Dry)(bu/ac)'].astype(float)
# %%
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            cmin = df['Estimated Volume (Dry)(bu/ac)'].min(),
            color = df['Estimated Volume (Dry)(bu/ac)'],
            cmax = df['Estimated Volume (Dry)(bu/ac)'].max(),
            colorbar_title='Estimated Volume (Dry)(bu/ac)'               
        )))
fig.update_layout(
        title = 'Elevation Map from 2011 Field Data',
        geo_scope='usa',
    )
fig.update_geos(fitbounds = 'locations')
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.write_html('plotly_j2011.html')
fig.show()
#2011 VOLUME- CORN
# %%
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2012_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Estimated Volume (Dry)(bu/ac): ' + df['Estimated Volume (Dry)(bu/ac)'].apply(str)
df['Estimated Volume (Dry)(bu/ac)'] = df['Estimated Volume (Dry)(bu/ac)'].astype(float)
# %%
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            cmin = df['Estimated Volume (Dry)(bu/ac)'].min(),
            color = df['Estimated Volume (Dry)(bu/ac)'],
            cmax = df['Estimated Volume (Dry)(bu/ac)'].max(),
            colorbar_title='Estimated Volume (Dry)(bu/ac)'               
        )))
fig.update_layout(
        title = 'Elevation Map from 2012 Field Data',
        geo_scope='usa',
    )
fig.update_geos(fitbounds = 'locations')
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.write_html('plotly_j2012.html')
fig.show()
#2012 VOLUME- SOYBEAN
# %%
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2013_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Estimated Volume (Dry)(bu/ac): ' + df['Estimated Volume (Dry)(bu/ac)'].apply(str)
df['Estimated Volume (Dry)(bu/ac)'] = df['Estimated Volume (Dry)(bu/ac)'].astype(float)
# %%
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            cmin = df['Estimated Volume (Dry)(bu/ac)'].min(),
            color = df['Estimated Volume (Dry)(bu/ac)'],
            cmax = df['Estimated Volume (Dry)(bu/ac)'].max(),
            colorbar_title='Estimated Volume (Dry)(bu/ac)'               
        )))
fig.update_layout(
        title = 'Elevation Map from 2013 Field Data',
        geo_scope='usa',
    )
fig.update_geos(fitbounds = 'locations')
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.write_html('plotly_j2013.html')
fig.show()
#2013 VOLUME- CORN
# %%
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2014_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Estimated Volume (Dry)(bu/ac): ' + df['Estimated Volume (Dry)(bu/ac)'].apply(str)
df['Estimated Volume (Dry)(bu/ac)'] = df['Estimated Volume (Dry)(bu/ac)'].astype(float)
# %%
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            cmin = df['Estimated Volume (Dry)(bu/ac)'].min(),
            color = df['Estimated Volume (Dry)(bu/ac)'],
            cmax = df['Estimated Volume (Dry)(bu/ac)'].max(),
            colorbar_title='Estimated Volume (Dry)(bu/ac)'               
        )))
fig.update_layout(
        title = 'Elevation Map from 2014 Field Data',
        geo_scope='usa',
    )
fig.update_geos(fitbounds = 'locations')
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.write_html('plotly_j2014.html')
fig.show()
#2014 VOLUME- SOYBEAN
# %%
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r'/Users/makennarozelle/Documents/REU Purdue/Re__Ault_Harvest_Data (1)/gott_east93_2014_harvest.csv', dtype="unicode", encoding= 'unicode_escape')
df['text'] = 'Speed(mph): ' + df['Speed(mph)'].apply(str)
df['Speed(mph)'] = df['Speed(mph)'].astype(float)

# %%
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            cmin = df['Speed(mph)'].min(),
            color = df['Speed(mph)'],
            cmax = df['Speed(mph)'].max(),
            colorbar_title='Speed(mph)'               
        )))
fig.update_layout(
        title = 'Elevation Map from 2014 Field Data',
        geo_scope='usa',
    )
fig.update_geos(fitbounds = 'locations')
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.write_html('plotly_j2014speed.html')
fig.show()
#2014  SPEED-SOYBEAN
# %%
