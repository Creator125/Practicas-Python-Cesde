import matplotlib.pyplot as plt

def crearPDF(dataframe, nombre):
    # Crear el gráfico de tabla usando matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('off')  # Ocultar ejes

    tabla = ax.table(cellText=dataframe.values, colLabels=dataframe.columns, loc='center')
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1.2, 1.2)

    # Guardar el gráfico de tabla en un archivo PDF
    plt.savefig(f'pdf/{nombre}.pdf', format='pdf', bbox_inches='tight')