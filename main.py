import os
from tkinter.filedialog import askdirectory
from tkinter import *
def organizador_pasta():
#Abre uma janela para que selecione a pasta que deseja organizar
    caminho = askdirectory(title='Selecione uma pasta')

#Lista todos os arquivos dentro da pasta selecionada
    lista_arquivos = os.listdir(caminho)

#Lê os arquivos e nomeia-os de acordo com suas extensões (Dicionário)
    locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "mkv": [".mkv"]
}

#Percorre toda a lista de arquivos de novo
    for arquivo in lista_arquivos:
    #01. Arquivo.pdf
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    #Verifica se tem arquivos para cara tipo de extensão
        for pasta in locais:
            if extensao in locais[pasta]:
            #Cria pasta com o nome de acordo com extensão caso já não haja alguma
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
            #Leva os arquivos com suas devidas extensões para dentro de cada uma das pastas criadas
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

janela = Tk()
janela.title('Organizador de pastas')
texto_orientação = Label(janela, text='Clique no botão abaixo para selecionar a pasta')
texto_orientação.grid(column=0,row=0)

botao = Button(janela, text='Clique aqui para selecionar a pasta', command=organizador_pasta)
botao.grid(column=0, row=1)

janela.mainloop()