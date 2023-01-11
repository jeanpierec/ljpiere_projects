import dash
from dash import html
from matplotlib import container
from navbar import create_navbar
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from home import Delitos_2010_2021
from home import f_sb2022



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav = create_navbar()

#values2 = Delitos_2010_2021['CONDUCTA'].value_counts()
conducta = Delitos_2010_2021['CONDUCTA'].unique()


dropdown = html.Div([
    dcc.Dropdown(['2010', '2011', '2012', '2013','2014','2015','2016','2017','2018','2019','2020','2021'], 
                 placeholder='Seleccione año', id='dropdown2',
                style=dict(
                    width='100%',
                    verticalAlign="middle",
                    fontSize = '20px',
                ),multi=True),
    html.Div(id='dd-output-container2')
])

@callback(
    Output('dd-output-container2', 'children'),
    Input('dropdown2', 'value'),
)
 
                               
def update_output(value):
    lista=[]
    lista.append(value)
    if lista==[None]:
        int_list=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
        new_df = Delitos_2010_2021[(Delitos_2010_2021['ANO'].isin(int_list))]
    else:
        int_list = list(map(int, value))
        new_df = Delitos_2010_2021[(Delitos_2010_2021['ANO'].isin(int_list))]
    return html.Div([

    html.Div([

     html.Table(style={'width':'100%'},
               children=[html.Tr(
                     children=[
                         
                         html.Td(style={'width':'100%'},
                             children=[
                                 html.H1('Conducta delictiva vs años',
                                 style={'textAlign':'center', 'margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dcc.Graph(id='linegraph2',
                                 figure = px.line(new_df, x='ANO', color='CONDUCTA'))   
                             ]
                         ) 
                     ]
                 ),]),
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
    
app.layout=html.Div([

    html.Div([

     html.Table(style={'width':'90%'},
               children=[html.Tr(
                     children=[
                         
                         html.Td(style={'width':'50%'},
                             children=[
                                 html.H1('Curso de vida en el que se comenten delitos',
                                 style={'textAlign':'center', 'margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dcc.Graph(id='bargraph',
                                 figure = px.histogram(Delitos_2010_2021, x='CURSO_DE_VIDA', color='CURSO_DE_VIDA', barmode='group'))   
                             ]
                         ),
                         html.Td(style={'width':'50%'},
                             children=[
                                 html.H1('Clasificacion del delito',
                                 style={'textAlign':'center', 'margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dcc.Graph(id='bargraph',
                                 figure = px.histogram(Delitos_2010_2021, x='CLASIFICACIONES DELITO', color='CLASIFICACIONES DELITO', barmode='group'))   
                             ]
                         )  
                     ]
                 ),
                html.Tr(
                     children=[
                         
                         html.Td(style={'width':'50%'},
                             children=[
                                 html.H1('Indicador de ingreso de estado',
                                 style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dcc.Graph(id='bargraph',
                                 figure = px.histogram(f_sb2022, x='ind_ingr_estado', color='ind_ingr_estado', barmode='group'))   
                             ]
                         ),html.Td(style={'width':'50%'},
                             children=[
                                 html.H1('Indicador de alcantarillado',
                                 style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dcc.Graph(id='bargraph',
                                 figure = px.histogram(f_sb2022, x='ind_tiene_alcantarillado', color='ind_tiene_alcantarillado', barmode='group'))   
                             ]
                         ),
                     ]
                 ),]),
    
    
    ]),
               
])
 

def create_page_3():
    layout = html.Div([
        nav,
        dropdown,
        app.layout
    ])
    return layout
