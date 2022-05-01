from tokenize import Ignore
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from scipy.integrate import quad
from venv import create
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
from PyQt6.QtWidgets import *
import qdarktheme #Si no corre hay que instalar esta stylesheet (pip install pyqtdarktheme) o deshabilitar la linea 384
import sys
import csv
import math as m




class ventanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Integrales Definidas")
        self.setWindowIcon(QIcon('./icon.png'))
        self.setMinimumSize(500, 600)
        self.create_layout()  

    def create_layout(self):
           
        layout = QGridLayout()
        
        self.setLayout(layout)
        etiquetas = {}
        self.campos_texto = {}
        
        
        self.campos_texto['LimSup']=QLineEdit()
        self.campos_texto['LimInf']=QLineEdit()
        self.campos_texto['Integral']=QLineEdit()
        
        self.campos_texto['LimSup'].setFixedWidth(60)
        #self.campos_texto['Integral'].setFixedWidth(200)
        self.campos_texto['LimInf'].setFixedWidth(60)
        
        etiquetas['b']=QLabel('Limite superior:')
        etiquetas['a']=QLabel('Limite inferior:')
        etiquetas['Resul']=QLabel('Resultado:')
        etiquetas['Resul'].setFont(QFont('Arial',20))
        
        
        etiquetas['Integral']=QLabel(self)
        pixmap=QPixmap('./icon.png')
        pixmap=pixmap.scaled(150,150)
        etiquetas['Integral'].setPixmap(pixmap)
        
        Pow=QPushButton('Potencia', clicked=self.powtext)
        Log=QPushButton('Logaritmo', clicked=self.logtext)
        Sqrt=QPushButton('Raíz cuadrada', clicked=self.sqrtext)
        Exp=QPushButton('Euler (e)', clicked=self.Etext)
        Pi=QPushButton('Pi', clicked=self.Pitext)
        Sin=QPushButton('Seno', clicked=self.sintext)
        Cos=QPushButton('Coseno', clicked=self.costext)
        Tan=QPushButton('Tangente', clicked=self.tantext)
        Arcsin=QPushButton('Arcoseno', clicked=self.arcsintext)
        Arcos=QPushButton('Arcocoseno', clicked=self.arcostext)
        Enter=QPushButton('Resolver', clicked=self.solve)
        Graph=QPushButton('Graficar Int', clicked=self.graphint)
        Graphfunc=QPushButton('Graficar Fun', clicked=self.graphfunc)
        
        Enter.setIcon(QIcon('./check.png'))
        Graph.setIcon(QIcon('./graph.png'))
        Graphfunc.setIcon(QIcon('./grafico.png'))
        
        self.resultado=QLabel('')
        self.resultado.setFont(QFont('Arial',20))
        
        etiquetas['Creador'] = QLabel('''
Santiago Sepúlveda Landeros
Jose Miguel Muñoz Villalvazo
Edgar Daniel Chacón Amaro''')

        layout.addWidget(etiquetas['b'],0,0,1,1)
        layout.addWidget(etiquetas['a'],2,0,1,1)
        layout.addWidget(etiquetas['Integral'],1,0,1,1)
        layout.addWidget(self.campos_texto['LimSup'],0,1,1,1)
        layout.addWidget(self.campos_texto['Integral'],1,1,1,1)
        layout.addWidget(self.campos_texto['LimInf'],2,1,1,1)
        layout.addWidget(Pow,3,0,1,1)
        layout.addWidget(Log,4,0,1,1)
        layout.addWidget(Sqrt,5,0,1,1)
        layout.addWidget(Exp,6,0,1,1)
        layout.addWidget(Pi,7,0,1,1)
        layout.addWidget(Sin,3,1,1,1)
        layout.addWidget(Cos,4,1,1,1)
        layout.addWidget(Tan,5,1,1,1)
        layout.addWidget(Arcsin,6,1,1,1)
        layout.addWidget(Arcos,7,1,1,1)
        layout.addWidget(Enter,8,0,2,2)
        layout.addWidget(Graph,9,0,2,2)
        layout.addWidget(Graphfunc,10,0,2,2)
        layout.addWidget(etiquetas['Resul'],11,0,2,1)
        layout.addWidget(self.resultado,11,1,2,1)
        layout.addWidget(etiquetas['Creador'],12,0,2,1)
        
    def powtext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"**")
    def sqrtext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.sqrt()")
    
    def logtext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.log()")
        
    def Etext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"m.e")
        
    def Pitext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.pi")
    
    def sintext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.sin()")
        
    def costext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.cos()")
        
    def tantext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.tan()")
        
    def arcsintext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.arcsin()")
        
    def arcostext(self):
        current=self.campos_texto['Integral'].text()
        self.campos_texto['Integral'].setText(current+"np.arcos()")
        
        
    def integrand(self,x,funcstr):
        func=eval(funcstr)
        return func
    

    
    def solve(self):
        inf=int(self.campos_texto['LimInf'].text())
        sup=int(self.campos_texto['LimSup'].text())
        functext=self.campos_texto['Integral'].text()
        I = quad(self.integrand, inf,sup, args=(functext))
        self.resultado.setText(str(abs(round(I[0], 12))))
        
    def graphfunc(self):
       # 100 linearly spaced numbers
        x = np.linspace(-10,10,100)

        functext=self.campos_texto['Integral'].text()
        y = eval(functext)

        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        plt.plot(x,y, 'r')

        # show the plot
        plt.show() 
        
    def graphint(self):
        a, b = int(self.campos_texto['LimInf'].text()), int(self.campos_texto['LimSup'].text())  # integral limits
        x = np.linspace(a-2,b+2,50)
        functext=self.campos_texto['Integral'].text()
        y = self.integrand(x,functext)

        fig, ax = plt.subplots()
        ax.plot(x, y, 'r', linewidth=2)
        #ax.set_ylim(bottom=0)

        # Make the shaded region
        ix = np.linspace(a, b)
        iy = self.integrand(ix,functext)
        verts = [(a, 0), *zip(ix, iy), (b, 0)]
        poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
        ax.add_patch(poly)

        #ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
         #       horizontalalignment='center', fontsize=20)

        fig.text(0.9, 0.05, '$x$')
        fig.text(0.1, 0.9, '$y$')
        
        
       
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        #ax.set_xticks([a, b], labels=[str(a), str(b)])
        ax.yaxis.set_ticks_position('left')


        plt.show()
         
     
         

        
         
    
        
            
        
    
        
app = QApplication(sys.argv)
#app.setStyleSheet(qdarktheme.load_stylesheet()) #esta es la linea que se deshabilita si no corre

start = ventanaPrincipal()
start.show()


app.exec()

        
        