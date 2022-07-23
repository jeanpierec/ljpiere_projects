from dash import html
from navbar import create_navbar
from dash import Dash, dcc, html, Input, Output, callback, dash_table

nav = create_navbar()



header = html.H1('Mapas de segmentación por factores de riesgo socio-económico en Bucaramanga', style={'textAlign':'center', 'margin-top': '50px', 
                                                  'fontSize': 40,'margin-bottom':'50px', 'font-family': 'Montserrat'})

dropdown = html.Div([
    dcc.Dropdown(['Segmentación por factores de riesgo socio-económico 2021', 'Segmentación por factores de riesgo socio-económico 2022'], 
                 'Segmentación por factores de riesgo socio-económico 2021', id='dropdown',
                style=dict(
                    width='100%',
                    verticalAlign="middle",
                    fontSize = '20px',
                )),
    html.Div(id='output-container')
])

@callback(
    Output('output-container', 'children'),
    Input('dropdown', 'value')
)

def update_output(value):
    if value == 'Segmentación por factores de riesgo socio-económico 2021':
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
                                    html.H1('Segmentación por factores de riesgo socio-económico 2021',
                                    style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 40,'margin-bottom':'20px', 'font-family': 'Montserrat'}),
                                    html.Iframe(id='map5', srcDoc=open('cluster2021.html', 'r').read(), width='100%', height='800')
                                ]
                            ) 
                        ]
                    )       
                ]
                ),
        ]),
    ])
    if value == 'Segmentación por factores de riesgo socio-económico 2022':
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
                                    html.H1('Segmentación por factores de riesgo socio-económico 2022',
                                    style={'textAlign':'center', 'margin-top': '20px', 
                                                  'fontSize': 40,'margin-bottom':'20px', 'font-family': 'Montserrat'}),
                                    html.Iframe(id='map6', srcDoc=open('cluster2022.html', 'r').read(), width='100%', height='800')
                                ]
                            ) 
                        ]
                    )       
                ]
                ),
        ]),
    ])


def create_page_5():
    layout = html.Div([
        nav,
        header,
        dropdown 
    ])
    return layout