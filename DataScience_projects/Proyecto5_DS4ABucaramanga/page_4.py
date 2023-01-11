
from navbar import create_navbar
from dash import Dash, dcc, html, Input, Output, callback, dash_table
from home import Delitos_2010_2021
from home import f_sb2021
from home import f_sb2022
from home import Violencia_G_2015_2022

nav = create_navbar()

header = html.H3('TABLAS DE DATOS',style={'textAlign':'center','margin-top': '10px', 
                                                  'fontSize': 40,'margin-bottom':'10px', 'font-family': 'Montserrat'})

Delitos_2010_2021 = Delitos_2010_2021.head(10).iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
f_sb2021 = f_sb2021.head(10).iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
f_sb2022 = f_sb2022.head(10).iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
Violencia_G_2015_2022 = Violencia_G_2015_2022.head(10).iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]

grafico=html.Div([
    
    html.Div([

    html.Table(style={'width':'50%'},
               children=[
            
                 html.Tr(
                     children=[
                         
                         html.Td(
                             children=[
                                 html.H1('Delitos desde el año 2010 hasta el 2021',
                                 style={'textAlign':'left','margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dash_table.DataTable(
                                        data=Delitos_2010_2021.to_dict('records'),
                                        columns=[{'id': c, 'name': c} for c in Delitos_2010_2021.columns],
                                        style_cell={'textAlign': 'center','margin-top': '5px', 
                                                  'fontSize': 10,'margin-bottom':'5px', 'font-family': 'Montserrat'},
                                    ),
                                  
                             ]
                         ) 
                     ]
                 ),      
               ]
              ),
    html.Table(style={'width':'20%'},
               children=[
            
                 html.Tr(
                     children=[
                         
                         html.Td(
                             children=[
                                 html.H1('Sisben año 2022',
                                 style={'textAlign':'left','margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dash_table.DataTable(
                                        data=f_sb2022.to_dict('records'),
                                        columns=[{'id': c, 'name': c} for c in f_sb2022.columns],
                                        style_cell={'textAlign': 'center','margin-top': '5px', 
                                                  'fontSize': 10,'margin-bottom':'5px', 'font-family': 'Montserrat'},
                                    ),
                                  
                             ]
                         ) 
                     ]
                 ),  
     
               ]
              ),
    html.Table(style={'width':'40%'},
               children=[
            
                html.Tr(
                     children=[
                         
                         html.Td(
                             children=[
                                 html.H1('Datos de Violencia desde el año 2015 al 2022',
                                 style={'textAlign':'left','margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dash_table.DataTable(
                                        data=Violencia_G_2015_2022.to_dict('records'),
                                        columns=[{'id': c, 'name': c} for c in Violencia_G_2015_2022.columns],
                                        style_cell={'textAlign': 'center','margin-top': '5px', 
                                                  'fontSize': 10,'margin-bottom':'5px', 'font-family': 'Montserrat'},
                                    ),
                                  
                             ]
                         ) 
                     ]
                 ),
     
               ]
              ),
    html.Table(style={'width':'30%'},
               children=[
            
                 html.Tr(
                     children=[
                         
                         html.Td(
                             children=[
                                 html.H1('Sisben año 2021',
                                 style={'textAlign':'left','margin-top': '10px', 
                                                  'fontSize': 20,'margin-bottom':'10px', 'font-family': 'Montserrat'}),
                                 dash_table.DataTable(
                                        data=f_sb2021.to_dict('records'),
                                        columns=[{'id': c, 'name': c} for c in f_sb2021.columns],
                                        style_cell={'textAlign': 'center','margin-top': '5px', 
                                                  'fontSize': 10,'margin-bottom':'5px', 'font-family': 'Montserrat'},
                                    ),
                                  
                             ]
                         ) 
                     ]
                 ),        
               ]
              ),
    
    
    ]),
               
# End of all content DIV
])

def create_page_4():
    layout = html.Div([
        nav,
        header,
        grafico
    ])
    return layout