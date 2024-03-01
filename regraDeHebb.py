import tkinter as tk
import numpy as np

entradas = [np.zeros((8,8)),np.zeros((8,8))]
deltaw = np.zeros((8,8))
w = np.zeros((8,8))
bias = 0
deltab = 0
deltaTeste = 0
y = [1,-1]
test = np.zeros((2,1))

def toggle_value(event, matrix, label_matrix, row, col):
    # Alterna o valor na matriz
    matrix[row, col] = 1 - matrix[row, col]
    
    # Atualiza o rótulo com o novo valor
    label_matrix[row][col].config(text=matrix[row, col])

def clear_matrices(matrix1, matrix2, label_matrix1, label_matrix2):
    # Limpa as matrizes e atualiza os rótulos
    matrix1.fill(0)
    matrix2.fill(0)
    for i in range(8):
        for j in range(8):
            label_matrix1[i][j].config(text=matrix1[i, j])
            label_matrix2[i][j].config(text=matrix2[i, j])

def train_model():
    global matrix1,matrix2,entradas,deltaw,bias,w,deltab
    entradas[0] = matrix1
    entradas[1] = matrix2
    
    for i in range(2):
        deltaw = entradas[i]*y[i]
        deltab = y[i]
        w = w + deltaw
        bias = bias + deltab;
    print('treinado')
    
    for i in range(2):    
        deltaTeste = 0
        for j in range(8):
            for z in range(8):
                deltaTeste = deltaTeste + (w[j][z]*entradas[i][j][z])
        deltaTeste = deltaTeste + bias
        if(deltaTeste>=0):
            test[i][0] = 1
        else:
            test[i][0] = -1
    print('image 1: ' + str(test[0]))  
    print('image 2: ' + str(test[1])) 
    pass

def test_model():
    global deltaw,bias,matrix1,w,deltab,deltaTeste
    result = 0
       
    deltaTeste = 0
    for j in range(8):
        for z in range(8):
            deltaTeste = deltaTeste + (w[j][z]*matrix1[j][z])
    deltaTeste = deltaTeste + bias
    if(deltaTeste>=0):
        result = 1
    else:
        result = -1
    print('image 1: ' + str(result))  
    pass

# Cria uma janela
root = tk.Tk()
root.title("Matrizes 8x8")

# Obtém o tamanho da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcula o tamanho das células da matriz com base no tamanho da tela
cell_size = min(screen_width, screen_height) // 8

# Cria duas matrizes 8x8 preenchidas com zeros
matrix1 = np.zeros((8, 8), dtype=int)
matrix2 = np.zeros((8, 8), dtype=int)

# Cria uma moldura para as matrizes
frame = tk.Frame(root)
frame.pack()

# Cria uma matriz de rótulos para exibir a matriz 1
label_matrix1 = [[tk.Label(frame, text=matrix1[i, j], width=2, height=1, relief="raised", borderwidth=1) for j in range(8)] for i in range(8)]
for i in range(8):
    for j in range(8):
        label_matrix1[i][j].grid(row=i, column=j, padx=1, pady=1)
        label_matrix1[i][j].bind("<Button-1>", lambda event, row=i, col=j, matrix=matrix1, label_matrix=label_matrix1: toggle_value(event, matrix, label_matrix, row, col))

# Adiciona um espaço entre as matrizes
tk.Label(frame, text=" " * 5).grid(row=0, column=8)

# Cria uma matriz de rótulos para exibir a matriz 2
label_matrix2 = [[tk.Label(frame, text=matrix2[i, j], width=2, height=1, relief="raised", borderwidth=1) for j in range(8)] for i in range(8)]
for i in range(8):
    for j in range(8):
        label_matrix2[i][j].grid(row=i, column=j+9, padx=1, pady=1)
        label_matrix2[i][j].bind("<Button-1>", lambda event, row=i, col=j, matrix=matrix2, label_matrix=label_matrix2: toggle_value(event, matrix, label_matrix, row, col))

# Cria um frame para os botões
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)

# Adiciona os botões "Limpar", "Treinar" e "Testar" na parte inferior da tela
clear_button = tk.Button(button_frame, text="Limpar", command=lambda: clear_matrices(matrix1, matrix2, label_matrix1, label_matrix2))
clear_button.pack(side=tk.LEFT, padx=10)
train_button = tk.Button(button_frame, text="Treinar", command=train_model)
train_button.pack(side=tk.LEFT, padx=10)
test_button = tk.Button(button_frame, text="Testar", command=test_model)
test_button.pack(side=tk.LEFT, padx=10)
exit_button = tk.Button(button_frame, text="Sair", command=root.quit)
exit_button.pack(side=tk.RIGHT, padx=10)

# Executa o loop principal da interface gráfica
root.mainloop()
