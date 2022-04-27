# voltando a mexer com interface grafica
from ctypes import sizeof
import PySimpleGUI as inter

layout = [  [inter.Text('Mat é gay')],
            [inter.Text(' porque ele é gay ? '), inter.InputText()],
            [inter.Button('Gay'), inter.Button('Cancel')],
            [inter.Button("Encerrar programa ele é insamente gay")] 
            
            ]
window = inter.Window("mat gay", layout)
inter.theme('Pink')
while True:
    event, values = window.read()
    if event == inter.WIN_CLOSED or event == 'Cancel': 
       break
       
    elif event=='Gay':                
                                                                      # usuario clica no bota gay
        janela3 = inter.Window("Voce é muito gay ", layout2).maximize
        if event == inter.WIN_CLOSED or event=='Cancelar':
            break
    elif event=="encerrar programa ele é insamente gay":  # usuario clica no bota insamente gay
        layout2= [
            [inter.Text("Tao gay que cancela o programa")],
            [inter.Button(" Cancelar")]
        ]                                                    # caso usuario cancele
        j = inter.Window(" rato",layout2).maximize
        if event == "Cancelar":
            break
          
        
    
# listas
nomesIdades = ["Rodrigo", 18, True ]
nomesIdades[-1] # remover ultima item da lista, ordem negativa
