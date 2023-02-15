"""
Software de Evaluación de Vehículos - Curso Integrador II
----------------------------------------------
Esta aplicación tiene como objetivo utilizar técnicas de Machine Learning
para la evaluación de vehículos con respecto a una base de datos.

**Autores**: Paola Castro *Universidad Francisco de Paula Santander*
             Sebastian Rojas *Universidad Francisco de Paula Santander*
             Miguel Bruges *Universidad Francisco de Paula Santander*

..Notas::
    Este software hace uso de `tkinter`, de `PIL`, de `Pandas` y de `SkLearn`
    La documentación correspondiente se presenta a continuación:
    <https://docs.python.org/3/library/tk.html>
    <https://pillow.readthedocs.io/en/stable/>
    <https://pandas.pydata.org/docs/>
    <https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html>
"""

#Sección de importe de librerías
from tkinter import * #Utilizado para la creación de la interfaz gráfica
from PIL import ImageTk, Image #Utilizado para implementar imágenes en Tkinter
import pandas as pd #Librería para manipular la base de datos "Car Evaluation"
from sklearn.tree import DecisionTreeClassifier #Librería para regresión logística

car_data = pd.read_csv('output.txt') #Añadir el dataset a la variable "car_data"
input_data = car_data.drop(columns=['29']) #Crear las entradas sin la variable de salida
output_data = car_data['29'] #Crear una lista de solo las salidas
modeloML = DecisionTreeClassifier() #Creación del modelo de regresión logística
modeloML.fit(input_data, output_data) #Procesamiento del modelo de Machine Learning

def raiz():
    global menu
    menu = Tk() #Creación del objeto ventana
    menu.title("Evaluador de Vehículos") #Título de la ventana
    menu.geometry("300x350") #Dimensiones de la ventana
    menu.resizable(False,False) #Evita que se pueda redimensionar
    menu.iconbitmap("Images/Icono.ico") #Ícono de la aplicación
    #Imagen del menú de la aplicación
    menuImage = ImageTk.PhotoImage(Image.open("Images/Menu.jpg"))
    Label(image = menuImage).place(x=-2,y=0)
    Button(menu, text = "Ingresar", height = "2", width = "30", cursor = "hand2", command = start).place(x = 40, y = 165)
    menu.mainloop()

def start():
    menu.destroy()
    global startMenu
    startMenu = Tk() #Creación del objeto ventana
    startMenu.title("Ingreso de datos") #Título de la ventana
    startMenu.geometry("720x720") #Dimensiones de la ventana
    startMenu.resizable(False,False) #Evita que se pueda redimensionar
    startMenu.iconbitmap("Images/Icono.ico") #Ícono de la aplicación
    #Imagen del fondo
    menuImage = ImageTk.PhotoImage(Image.open("Images/Datos.jpg"))
    Label(image = menuImage).place(x=-2,y=0)
    
    #||Sección de listas||
    
    #Precio del auto
    Label(startMenu, text="Precio del vehículo:").place(x=90,y=230)
    rangoPrecios = ['+$70Mill. COP', '$40Mill. - 70Mill. COP', '$10Mill. - 40Mill. COP', '-$10Mill. COP']
    global lista_precios
    lista_precios = Listbox(startMenu,height=4,exportselection=0)
    lista_precios.place(x=90,y=250)
    for item in rangoPrecios:
        lista_precios.insert(END, item)
    
    #Precio de mantenimiento
    Label(startMenu, text="Costo mantenimiento:").place(x=300,y=230)
    rangoMant = ['+$500k COP', '$400k - $500k COP', '$300k - $400k COP', '-$300k COP']
    global lista_mant
    lista_mant = Listbox(startMenu,height=4,exportselection=0)
    lista_mant.place(x=300,y=250)
    for item in rangoMant:
        lista_mant.insert(END, item)
    
    #Cantidad de puertas
    Label(startMenu, text="Cantidad de puertas:").place(x=510,y=230)
    rangoPuertas = ['Más de 5 puertas', '4 Puertas', '3 Puertas', '2 Puertas']
    global lista_puertas
    lista_puertas = Listbox(startMenu,height=4,exportselection=0)
    lista_puertas.place(x=510,y=250)
    for item in rangoPuertas:
        lista_puertas.insert(END, item)
    
    #Cantidad de personas
    Label(startMenu, text="Cantidad de personas:").place(x=90,y=380)
    rangoPersonas = ['Más de 5 personas', '4 - 5 Personas', '2 - 3 Personas']
    global lista_personas
    lista_personas = Listbox(startMenu,height=4,exportselection=0)
    lista_personas.place(x=90,y=400)
    for item in rangoPersonas:
        lista_personas.insert(END, item)
    
    #Tamaño del maletero
    Label(startMenu, text="Tamaño del maletero:").place(x=300,y=380)
    rangoMaleta = ['Más de 600L', 'Entre 300L - 600L', 'Menos de 300L']
    global lista_maleta
    lista_maleta = Listbox(startMenu,height=4,exportselection=0)
    lista_maleta.place(x=300,y=400)
    for item in rangoMaleta:
        lista_maleta.insert(END, item)
    
    #Seguridad del vehículo
    Label(startMenu, text="Seguridad del vehículo:").place(x=510,y=380)
    rangoSafe = ['Seguridad Alta', 'Seguridad Media', 'Seguridad Baja']
    global lista_safe
    lista_safe = Listbox(startMenu,height=4,exportselection=0)
    lista_safe.place(x=510,y=400)
    for item in rangoSafe:
        lista_safe.insert(END, item)
    
    Button(startMenu, text = "Procesar los datos", height = "2", width = "80", cursor = "hand2", command = procesarData).place(x = 75, y = 600)
    
    startMenu.mainloop()

def procesarData():
    precioCarro = lista_precios.get(ANCHOR)
    mantCarro = lista_mant.get(ANCHOR)
    puertasCarro = lista_puertas.get(ANCHOR)
    personasCarro = lista_personas.get(ANCHOR)
    maletaCarro = lista_maleta.get(ANCHOR)
    safeCarro = lista_safe.get(ANCHOR)
    
    if precioCarro == "+$70Mill. COP":
        precioCarro = 4
    elif precioCarro == "$40Mill. - 70Mill. COP":
        precioCarro = 3
    elif precioCarro == "$10Mill. - 40Mill. COP":
        precioCarro = 2
    elif precioCarro == "-$10Mill. COP":
        precioCarro = 1
    
    if mantCarro == "+$500k COP":
        mantCarro = 4
    elif mantCarro == "$400k - $500k COP":
        mantCarro = 3
    elif mantCarro == "$300k - $400k COP":
        mantCarro = 2
    elif mantCarro == "-$300k COP":
        mantCarro = 1
    
    if puertasCarro == "Más de 5 puertas":
        puertasCarro = 1
    elif puertasCarro == "4 Puertas":
        puertasCarro = 2
    elif puertasCarro == "3 Puertas":
        puertasCarro = 3
    elif puertasCarro == "2 Puertas":
        puertasCarro = 4
    
    if personasCarro == "Más de 5 personas":
        personasCarro = 1
    elif personasCarro == "4 - 5 Personas":
        personasCarro = 2
    elif personasCarro == "2 - 3 Personas":
        personasCarro = 3
    
    if maletaCarro == "Más de 600L":
        maletaCarro = 1
    elif maletaCarro == "Entre 300L - 600L":
        maletaCarro = 2
    elif maletaCarro == "Menos de 300L":
        maletaCarro = 3

    if safeCarro == "Seguridad Alta":
        safeCarro = 1
    elif safeCarro == "Seguridad Media":
        safeCarro = 2
    elif safeCarro == "Seguridad Baja":
        safeCarro = 3
    
    prediccion = modeloML.predict([[precioCarro,mantCarro,puertasCarro,personasCarro,maletaCarro,safeCarro]])
    
    startMenu.destroy()
    global resultado
    resultado = Tk() #Creación del objeto ventana
    resultado.title("Resultado de predicción") #Título de la ventana
    resultado.geometry("300x200") #Dimensiones de la ventana
    resultado.resizable(False,False) #Evita que se pueda redimensionar
    resultado.iconbitmap("Images/Icono.ico") #Ícono de la aplicación
    #Imagen del fondo
    menuImage = ImageTk.PhotoImage(Image.open("Images/Resultado.jpg"))
    Label(image = menuImage).place(x=-2,y=0)
    
    if prediccion[0] < 45:
        colorText = 'red'
    elif prediccion[0] >= 45 and prediccion[0] < 75:
        colorText = "yellow"
    elif prediccion[0] >= 75:
        colorText = "green"
    
    Label(resultado, text = str(prediccion[0]) + " %", fg=str(colorText), bg = "black", pady=10, padx=10, font = 10).place(x=115,y=125)
    Button(resultado, text = "←", height = "1", width = "2", cursor = "hand2", command = Reset).place(x=20,y=162)
    Button(resultado, text = "Dashboard", height = "1", width = "8", cursor = "hand2", command = dashboard).place(x=210,y=162)
    resultado.mainloop()

def Reset():
    resultado.destroy()
    raiz()

# ////////////// DASHBOARD //////////////

def dashboard():
    import webbrowser
    webbrowser.open("http://127.0.0.1:8050/", new=1)

raiz()