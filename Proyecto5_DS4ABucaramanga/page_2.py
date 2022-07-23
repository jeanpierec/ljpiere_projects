from navbar import create_navbar
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from matplotlib.ticker import ScalarFormatter
import pandas              as pd # The gold standard of Python data analysis, to create and manipulate tables of data
import seaborn             as sns; sns.set() # A package to make Matplotlib visualizations more aesthetic
from home import Delitos_2010_2021

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav = create_navbar()

header = html.H1('Mapas de reconocimiento Bucaramanga', style={'textAlign':'center', 'margin-top': '50px', 
                                                  'fontSize': 40,'margin-bottom':'50px', 'font-family': 'Montserrat'})

dropdown = html.Div([
    dcc.Dropdown(['Mapa sisben 2021', 'Mapa sisben 2022', 'Mapa violencia Bucaramanga', 'Mapa crimenes Bucaramanga'], 
                 'Mapa sisben 2021', id='demo-dropdown',
                style=dict(
                    width='100%',
                    verticalAlign="middle",
                    fontSize = '20px',
                )),
    html.Div(id='dd-output-container')
])

@callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)

def update_output(value):
    if value == 'Mapa sisben 2021':
        return html.Div([
        html.Div([
            html.P('Alcaldia de Bucaramanga',style={'textAlign':'center'}),
        ]),
        html.Div([
        html.Table(style={'width':'90%'},
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    html.H1('Mapa sisben 2021',
                                    style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 40,'margin-bottom':'20px', 'font-family': 'Montserrat'}),
                                    html.Iframe(id='map1', srcDoc=open('s21map.html', 'r').read(), width='100%', height='800')
                                ]
                            ) 
                        ]
                    )       
                ]
                ),
        ]),
    ])
    if value == 'Mapa sisben 2022':
        return html.Div([
        html.Div([
            html.P('Alcaldia de Bucaramanga',style={'textAlign':'center'}),
        ]),
        html.Div([
        html.Table(style={'width':'90%'},
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    html.H1('Mapa sisben 2022',
                                    style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 40,'margin-bottom':'20px', 'font-family': 'Montserrat'}),
                                    html.Iframe(id='map2', srcDoc=open('s22map.html', 'r').read(), width='100%', height='800')
                                ]
                            ) 
                        ]
                    )       
                ]
                ),
        ]),
    ])
    if value == 'Mapa violencia Bucaramanga':
        return html.Div([
       
        html.Div([
            html.P('Alcaldia de Bucaramanga',style={'textAlign':'center'}),
        ]),
        html.Div([
        html.Table(style={'width':'90%'},
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    html.H1('Mapa violencia de genero Bucaramanga',
                                    style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 40,'margin-bottom':'20px', 'font-family': 'Montserrat'}),
                                    html.Iframe(id='map3', srcDoc=open('viomap.html', 'r').read(), width='100%', height='800')
                                ]
                            ) 
                        ]
                    )       
                ]
                ),
        ]),
    ])
    if value == 'Mapa crimenes Bucaramanga':
        return html.Div([

        html.Div([
            html.P('Alcaldia de Bucaramanga',style={'textAlign':'center'}),
        ]),
        html.Div([
        html.Table(style={'width':'90%'},
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    html.H1('Mapa crimenes Bucaramanga',
                                    style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 40,'margin-bottom':'20px', 'font-family': 'Montserrat'}),
                                    html.Iframe(id='map4', srcDoc=open('crimemap.html', 'r').read(), width='100%', height='800')
                                ]
                            ) 
                        ]
                    )       
                ]
                ),
        ]),
    ])

def generate_table(dataframe, max_rows=16):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
    

contrib_df=Delitos_2010_2021.melt(id_vars=['BARRIOS_HECHO'],value_vars=['ARMAS_MEDIOS'],var_name ='index',value_name ='Cantidad delitos por día')
contrib_df.drop_duplicates(subset=['BARRIOS_HECHO','Cantidad delitos por día'],inplace=True)
factors_most_acc = contrib_df.groupby(['BARRIOS_HECHO']).count().sort_values('index',ascending=False).reset_index().head(10)
factors_most_acc.drop(['index'], axis = 'columns', inplace=True)

fig = px.line_polar(factors_most_acc, r='Cantidad delitos por día', theta='BARRIOS_HECHO', line_close=True)
fig.update_traces(fill='toself')

grafico=html.Div([
    
    html.Div([

    html.Table(style={'width':'100%'},
               children=[
            
                 html.Tr(
                     children=[
                         
                         html.Td(
                             children=[
                                 html.H1('Delito Barrio por día',
                                 style={'textAlign':'center','margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dash_table.DataTable(
                                        data=factors_most_acc.to_dict('records'),
                                        columns=[{'id': c, 'name': c} for c in factors_most_acc.columns],
                                        style_cell={'textAlign': 'center','margin-top': '5px', 
                                                  'fontSize': 20,'margin-bottom':'5px', 'font-family': 'Montserrat'},
                                    ),
                                  
                             ]
                         ) 
                     ]
                 ), html.Tr(
                     children=[
                         
                         html.Td(style={'width':'100%'},
                             children=[
                                 html.H1('Cantidad de delitos por Barrio',
                                 style={'textAlign':'center','margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dcc.Graph(id='radargraph',
                                 figure = fig )   
                             ]
                         ) 
                     ]
                 ),      
               ]
              ),
    
    
    ]),
               
# End of all content DIV
])
def create_page_2():
    layout = html.Div([
        nav,
        header,
        dropdown,
        app.layout,
        grafico
    ])
    return layout
