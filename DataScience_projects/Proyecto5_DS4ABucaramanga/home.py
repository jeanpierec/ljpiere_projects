import dash
from dash import html
from matplotlib import container
from navbar import create_navbar
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

f_sb2021 = pd.read_csv("f_sb2021.csv", on_bad_lines='skip', sep=';')
f_sb2022 = pd.read_csv("f_sb2022.csv", on_bad_lines='skip', sep=';')
C2021 = pd.read_csv("C2021.csv", on_bad_lines='skip', sep=',')
C2022 = pd.read_csv("C2022.csv", on_bad_lines='skip', sep=',')
Delitos_2010_2021 = pd.read_csv("Delitos_2010_2021.csv", on_bad_lines='skip', sep=',')
Violencia_G_2015_2022 = pd.read_csv("Violencia_G_2015_2022.csv", on_bad_lines='skip', sep=',')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav = create_navbar()

nivel_sisben= f_sb2021['nivel_sisben']
grupo_sisben= f_sb2022["Grupo"]
values = Delitos_2010_2021['GENERO'].value_counts()
Genero = Delitos_2010_2021['GENERO'].unique()

values2 = Delitos_2010_2021['DIA_SEMANA'].value_counts()
armas = Delitos_2010_2021['DIA_SEMANA'].unique()

delitos_ano_mes= pd.DataFrame({'count' : Delitos_2010_2021.groupby( [ "ANO", "MES"] ).size()}).reset_index()

#gb21_sex = f_sb2021.groupby("sexo_persona")['sexo_persona'].count()
#fig = px.histogram(f_sb2021, x=gb21_sex.index, y=gb21_sex, histfunc='sum')

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
    
    html.H1('Data Visualization',style={'textAlign':'center'}),
    html.Div([
        html.P('Alcaldia de Bucaramanga',style={'textAlign':'center'}),
    ]),

    html.Div([

    html.Table(style={'width':'90%'},
               children=[
                html.Tr(style={'width':'50%'},
                     children=[
                         
                         html.Td(
                             children=[
                                 html.H1('Grupo de delitos por mes',
                                 style={'textAlign':'center'}),
                                 dcc.Graph(id='linegraph',
                                 figure = px.line(delitos_ano_mes, x="MES", y='count', color='ANO'))  
                                 
                             ]
                         ),html.Td(
                             children=[
                                 html.H1('Delitos por Género',
                                 style={'textAlign':'center'}),
                                 dcc.Graph(id='piegraph',
                                 figure = px.pie(Delitos_2010_2021, values=values, names=Genero))  
                                 
                             ]
                         )  
                     ]
                 ),
            
                 html.Tr(style={'width':'50%'},
                     children=[
                         
                         html.Td(style={'width':'50%'},
                             children=[
                                 html.H1('Nivel de Sisben Año 2021',
                                 style={'textAlign':'center'}),
                                 dcc.Graph(id='bargraph',
                                 figure = px.histogram(f_sb2021, x=nivel_sisben, color=nivel_sisben, barmode='group'))   
                             ]
                         ),html.Td(style={'width':'50%'},
                             children=[
                                 html.H1('Grupo de Sisben Año 2022',
                                 style={'textAlign':'center'}),
                                 dcc.Graph(id='bargraph2',
                                 figure = px.histogram(f_sb2022, x=grupo_sisben, color=grupo_sisben, barmode='group'))   
                             ]
                         )  
                     ]
                 ), 
                 
                       
               ]

              ),
     html.Table(style={'width':'90%'},
               children=[html.Tr(
                     children=[
                         
                         html.Td(style={'width':'100%'},
                             children=[
                                 html.H1('Días de la semana vs Delitos',
                                 style={'textAlign':'center'}),
                                 dcc.Graph(id='piegraph2',
                                 figure = px.pie(Delitos_2010_2021, values=values2, names=armas))   
                             ]
                         ) 
                     ]
                 ),]),
    
    
    ]),
               
# End of all content DIV
])


def create_page_home():
    layout = html.Div([
        nav,
        #header,
        app.layout
    ])
    return layout
