import plotly.express as px
gapminder_df=px.data.gapminder()
px.scatter(data_frame=gapminder_df,
           x='gdpPercap',
           y='lifeExp',
           size='pop',
           color='continent',
           title='Lifespan and Wealth 1952-2007',
           labels={'gdpPercap':'Wealth',
                   'lifeExp': 'Life Span'},
           log_x=True,
           range_y=[25,95],
           hover_name='country',
           animation_frame='year',
           height=600,
           size_max=100)
