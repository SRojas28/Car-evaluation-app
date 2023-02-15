import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'text2': '#FFFFFF',
    'text3': '#000000'
}

car_data = pd.read_csv('output.txt')
car_data = car_data.rename(columns={'4':'Puntaje_Precio','4.1':'Puntaje_Mantenimiento','4.2':'Puntaje_Cantidad_Puertas','3':'Puntaje_Cantidad_Personas','3.1':'Puntaje_Tamaño_Maletero','3.2':'Puntaje_Seguridad','29':'Percentil'})
#print(car_data)

data_figura_1 = car_data.drop(columns=['Puntaje_Mantenimiento','Puntaje_Cantidad_Puertas','Puntaje_Cantidad_Personas','Puntaje_Tamaño_Maletero','Puntaje_Seguridad'])
data_figura_1 = data_figura_1.sort_values("Puntaje_Precio",axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

data_figura_2 = car_data.drop(columns=['Puntaje_Precio','Puntaje_Cantidad_Puertas','Puntaje_Cantidad_Personas','Puntaje_Tamaño_Maletero','Puntaje_Seguridad'])
data_figura_2 = data_figura_2.sort_values("Puntaje_Mantenimiento",axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

data_figura_3 = car_data.drop(columns=['Puntaje_Mantenimiento','Puntaje_Precio','Puntaje_Cantidad_Personas','Puntaje_Tamaño_Maletero','Puntaje_Seguridad'])
data_figura_3 = data_figura_3.sort_values("Puntaje_Cantidad_Puertas",axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

data_figura_4 = car_data.drop(columns=['Puntaje_Mantenimiento','Puntaje_Cantidad_Puertas','Puntaje_Precio','Puntaje_Tamaño_Maletero','Puntaje_Seguridad'])
data_figura_4 = data_figura_4.sort_values("Puntaje_Cantidad_Personas",axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

data_figura_5 = car_data.drop(columns=['Puntaje_Mantenimiento','Puntaje_Cantidad_Puertas','Puntaje_Cantidad_Personas','Puntaje_Precio','Puntaje_Seguridad'])
data_figura_5 = data_figura_5.sort_values("Puntaje_Tamaño_Maletero",axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

data_figura_6 = car_data.drop(columns=['Puntaje_Mantenimiento','Puntaje_Cantidad_Puertas','Puntaje_Cantidad_Personas','Puntaje_Tamaño_Maletero','Puntaje_Precio'])
data_figura_6 = data_figura_6.sort_values("Puntaje_Seguridad",axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

figura_1 = px.bar(data_figura_1, x = "Percentil", y = "Puntaje_Precio", color="Puntaje_Precio")
figura_1.update_xaxes(title_text='Percentil general')
figura_1.update_yaxes(title_text='Cantidad de vehículos')
#figura_1.update_layout(barmode="group")

figura_2 = px.bar(data_figura_2, x = "Percentil", y = "Puntaje_Mantenimiento", color="Puntaje_Mantenimiento")
figura_2.update_xaxes(title_text='Percentil general')
figura_2.update_yaxes(title_text='Cantidad de vehículos')
#figura_2.update_layout(barmode="group")

figura_3 = px.bar(data_figura_3, x = "Percentil", y = "Puntaje_Cantidad_Puertas", color="Puntaje_Cantidad_Puertas")
figura_3.update_xaxes(title_text='Percentil general')
figura_3.update_yaxes(title_text='Cantidad de vehículos')
#figura_3.update_layout(barmode="group")

figura_4 = px.bar(data_figura_4, x = "Percentil", y = "Puntaje_Cantidad_Personas", color="Puntaje_Cantidad_Personas")
figura_4.update_xaxes(title_text='Percentil general')
figura_4.update_yaxes(title_text='Cantidad de vehículos')
#figura_4.update_layout(barmode="group")

figura_5 = px.bar(data_figura_5, x = "Percentil", y = "Puntaje_Tamaño_Maletero", color="Puntaje_Tamaño_Maletero")
figura_5.update_xaxes(title_text='Percentil general')
figura_5.update_yaxes(title_text='Cantidad de vehículos')
#figura_5.update_layout(barmode="group")

figura_6 = px.bar(data_figura_6, x = "Percentil", y = "Puntaje_Seguridad", color="Puntaje_Seguridad")
figura_6.update_xaxes(title_text='Percentil general')
figura_6.update_yaxes(title_text='Cantidad de vehículos')
#figura_6.update_layout(barmode="group")

app.layout = html.Div(children=[ #Engloba los divs de las seis gráficas
    #PRIMERA GRÁFICA
    html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Evaluador de vehículos',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Estas gráficas representan el funcionamiento del modelo de Machine Learning según sus entradas.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.H2(
        children='Figura 1. Precio vs percentil',
        style={
            'textAlign': 'center',
            'color': colors['text2']
        }
    ),

    html.Div(
    children='Donde sí la variable Puntaje_Precio tiene valor de 1 equivale a -$10Mill. COP, sí tiene valor de 2 equivale a $10Mill. - 40Mill. COP, sí tiene valor de 3 esquivale a $40Mill. - 70Mill. COP y sí tiene valor de 4 esquivale a +$70Mill. COP',
    style={
        'textAlign': 'center',
        'color': colors['text2']
        }
    ),

    dcc.Graph(
        figure=figura_1
    )

]), 
    #SEGUNDA GRÁFICA
    html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H2(
        children='Figura 2. Mantenimiento vs percentil',
        style={
            'textAlign': 'center',
            'color': colors['text2']
        }
    ),

    html.Div(
    children='Donde sí la variable Puntaje_Mantenimiento tiene valor de 1 equivale a -$300k COP, sí tiene valor de 2 equivale a $300k - $400k COP, sí tiene valor de 3 esquivale a $400k - $500k COP y sí tiene valor de 4 esquivale a +$500k COP',
    style={
        'textAlign': 'center',
        'color': colors['text2']
        }
    ),

    dcc.Graph(
        figure=figura_2
    )
]),
    #TERCERA GRÁFICA
    html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H2(
        children='Figura 3. Cantidad de puertas vs percentil',
        style={
            'textAlign': 'center',
            'color': colors['text2']
        }
    ),

    html.Div(
    children='Donde sí la variable Puntaje_Cantidad_Puertas tiene valor de 1 equivale a más de 5 puertas, sí tiene valor de 2 equivale a 4 Puertas, sí tiene valor de 3 esquivale a 3 Puertas y sí tiene valor de 4 esquivale a 2 Puertas',
    style={
        'textAlign': 'center',
        'color': colors['text2']
        }
    ),

    dcc.Graph(
        figure=figura_3
    )
]),
    #CUARTA GRÁFICA
    html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H2(
        children='Figura 4. Cantidad de personas vs percentil',
        style={
            'textAlign': 'center',
            'color': colors['text2']
        }
    ),

    html.Div(
    children='Donde sí la variable Puntaje_Cantidad_Personas tiene valor de 1 equivale a más de 5 personas, sí tiene valor de 2 equivale a 4 - 5 Personas, sí tiene valor de 3 esquivale a 2 - 3 Personas',
    style={
        'textAlign': 'center',
        'color': colors['text2']
        }
    ),

    dcc.Graph(
        figure=figura_4
    )
]),
    #QUINTA GRÁFICA
    html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H2(
        children='Figura 5. Tamaño del maletero vs percentil',
        style={
            'textAlign': 'center',
            'color': colors['text2']
        }
    ),

    html.Div(
    children='Donde sí la variable Puntaje_Tamaño_Maletero tiene valor de 1 equivale a más de 600L, sí tiene valor de 2 equivale a entre 300L - 600L, sí tiene valor de 3 esquivale a menos de 300L',
    style={
        'textAlign': 'center',
        'color': colors['text2']
        }
    ),

    dcc.Graph(
        figure=figura_5
    )
]),
    #SEXTA GRÁFICA
    html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H2(
        children='Figura 6. Seguridad vs percentil',
        style={
            'textAlign': 'center',
            'color': colors['text2']
        }
    ),

    html.Div(
    children='Donde sí la variable Puntaje_Seguridad tiene valor de 1 equivale a seguridad Alta, sí tiene valor de 2 equivale a seguridad Media, sí tiene valor de 3 esquivale a seguridad Baja',
    style={
        'textAlign': 'center',
        'color': colors['text2']
        }
    ),

    dcc.Graph(
        figure=figura_6
    )
])
])


app.run_server(debug = True)