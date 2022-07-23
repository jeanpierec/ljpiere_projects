import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Graficos", href='/'),
                    #dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Mapas", href='/page-2'),
                    dbc.DropdownMenuItem("Analitics", href='/page-3'),
                    dbc.DropdownMenuItem("Tablas", href='/page-4'),
                    dbc.DropdownMenuItem("Cluster", href='/page-5'),
                ],
            ),
        ],
        brand="Información delitos de Bucaramanga",
        brand_href="/",
        sticky="top",
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar
