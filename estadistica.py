from tkinter import *


class View ():
    def __init__(self, frame, width=100, height=100, color="Gray9") -> None:
        #Height = altura
        #Width = ancho
        self.width = width
        self.height = height
        self.color = color
        self.frame = frame
        self.create_canvas()

    def create_canvas(self):
        self.CANVAS = Canvas(self.frame, width=self.width,
                             height=self.height, bg=self.color, relief="flat", border=0, insertborderwidth=0, highlightbackground=self.color)
        self.CANVAS.pack(side=RIGHT)

    def make_table(self, data, tam=20, labels=[], max_top='100', font=("Verdana", 8), sep_labels=15, box_tam=7, fg="white"):
        """Config and show the table \n
        data -> a list of the data that you want to see *for example data = [10,50,32]*\n
        tam -> the width of each block\n
        labels -> a list of labels\n
        max_top -> if you have a max range that you want to show in the table (default 100)\n
        font -> font for the text\n
        sep_labels -> vertical separation beetwen the labels\n
        box_tam -> size of the rectangle of the labels
        fg -> colors for the text"""
        self.CANVAS.destroy()
        self.create_canvas()
        colors = ["Green", "Blue", "red", "orange", "violet"]
        font = font
        cant = len(data)
        max_top = max_top
        block_width = tam
        self.labels = labels

        # PORCENTAJE PARA DETERMINAR EL PUNTO DE ORIGEN
        percent_x = int(0.1*self.width)
        percent_y = int(0.99*self.height)

        # PUNTOS DONDE TERMINAN LOS EJES 'X' E 'Y'
        top_y = percent_x, int(0.05*self.height)
        top_x = int(0.45*self.width), percent_y

        # ORIGEN DE LOS EJES DE COORDENADAS
        origin = percent_x, percent_y

        # COORDENADAS PARA LA POSICIÓN DE LAS ETIQUETAS
        eje_x = origin, top_x
        eje_y = origin, top_y

        # SE CREAN LOS EJES COORDENADOS
        self.CANVAS.create_line(eje_x, fill=fg)
        self.CANVAS.create_line(eje_y, fill=fg)
        # self.CANVAS.create_line(pos_labels)

        # Colocando los labels
        x_ini = top_x[0]+25
        y_ini = top_y[1]
        x_fin = x_ini+box_tam
        count = 0
        for label in self.labels:
            y_fin = y_ini+box_tam
            self.CANVAS.create_rectangle(
                x_ini, y_ini, x_fin, y_fin, fill=colors[count])
            self.CANVAS.create_text(
                x_ini+box_tam+2, y_ini+int(font[1]/2)-1, text=label, anchor="w", font=font, fill=fg)
            y_ini = y_ini + sep_labels
            count += 1

        # Colocamos los rectangulos indicadores
        rango = origin[1]-top_y[1]
        space = int((top_x[0]-origin[0]-cant*block_width)/cant)
        x_ini = origin[0]+space
        count = 0
        for x in data:
            y_fin = top_y[1]+(rango-(x*rango/100))
            self.CANVAS.create_rectangle(
                x_ini, origin[1], x_ini+block_width, y_fin, fill=colors[count], activefill="Gray9", outline=colors[count],)

            self.CANVAS.create_text(
                (x_ini+block_width)-int(tam/2), y_fin-(font[1]/1.2), text=x, fill=fg)
            x_ini = space+x_ini+block_width
            count += 1

        self.CANVAS.create_text(
            top_y[0]-12, top_y[1], text=max_top, font=font, fill=fg)
        self.CANVAS.create_text(
            origin[0]-10, origin[1]-2, text="0", font=font, fill=fg)


if __name__ == "__main__":
    master = Tk()
    canvas_width = 200
    canvas_height = 100
    """w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack()

    checkered(w, 10)"""
    view = View(master, 450, 300)
    view.make_table([45, 38, 92, 54, 100], 20, ["Geometria",
                    "Fisica", "Aritmetica", "Matematica"])

    master.mainloop()
