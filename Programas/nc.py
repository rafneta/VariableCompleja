
# coding: utf-8

# In[ ]:


#Numero complejo
#nc
from modulos import *
def Granum(uno,dos,malla,
               actilim, xmin, xmax, ymin,\
              ymax, real1=1.5,imag1=-2.5,real11=1.5,imag11=-2.5,guarda=False):
    ancho_cuadro=1.4
    marcador="o"
    tam_marcador=6
    
    
    if dos==True: 
        z=real11+imag11*I
    
    if uno==True:
        z=real1+imag1*I
    
    fig=plt.figure(figsize=(8,4))
    plt.rc('text', usetex=False)
    #plt.rc('font', family='serif')
    #plt.rc('font', family='cm')
    ax = fig.add_subplot(121)
    
    
    sns.set()
    cp=sns.color_palette("Set2", 10)

    ax.plot([0, re(z)],[0,im(z)],color=cp[0],lw=3,label=r"$z=(%s$ "%latex(re(z))+"$,%s)$" %latex(im(z)))
    ax.plot(re(z),im(z),color=cp[0], marker=marcador,markersize=tam_marcador)
    #plt.legend(loc = "best")
    plt.legend(bbox_to_anchor=(1.3, 0.5, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    
    ax.grid(malla) 
        
        
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)


    #xlabel = ax.xaxis.get_label()                               
    #lpos = xlabel.get_position()
    #xlabel.set_position((1.04, lpos[1]))

    #ylabel = ax.yaxis.get_label()
    #lpos = ylabel.get_position()
    #ylabel.set_position((1.04, lpos[1]))

    ax.xaxis.set_label_coords(0.5, -0.05)
    ax.yaxis.set_label_coords(-0.08,0.5)
    #ax.
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlabel(r"$a$ ",fontsize=20)
    ax.set_ylabel(r"$b$",fontsize=20)
    title=ax.set_title("Ver "+r"$z=(a,b)$", y=1.05,        fontsize=14, color="k")
          
    #ax.axis([x0,x1,y0,y1])
    if  actilim==False or xmin>=xmax or ymin>=ymax :
        xlim=ax.get_xlim()
        ylim=ax.get_ylim()
        ax.set_xlim(min(min(xlim[0],ylim[0])*1.2,-10),max(max(xlim[1],ylim[1])*1.2,10))
        ax.set_ylim(min(min(xlim[0],ylim[0])*1.2,-10),max(max(xlim[1],ylim[1])*1.2,10))
    else:
        ax.set_xlim(xmin,xmax)
        ax.set_ylim(ymin,ymax)
    
    if guarda:
        plt.savefig("nc.png")
        plt.savefig("nc.svg")
        plt.savefig("nc.pdf")
        # No se soporta en binder el JPG 
        #plt.savefig("nc.jpg")
        plt.close()
    guardanota.value=""

        
        
    
    
    #plt.show()
    


titulo=widgets.HTML(
    value='''<div class="alert alert-warning"><h2>Operaciones unitarias</h2></div>''',
    placeholder='Some HTML')


def nc(real1=1.5,imaginario1=-2.5,real2=-1,imaginario2=-0.5):
    style = {'description_width': 'initial'}
    global guardanota
    
    r1=widgets.FloatSlider(
    value=7.5,
    min=-10.0,
    max=10.0,
    step=0.1,
    description=r'\(a\)',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',)

    ima1=widgets.FloatSlider(
    value=7.5,
    min=-10.0,
    max=10.0,
    step=0.1,
    description=r'\(b\)',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',)
    
    
    Uno=widgets.Checkbox(
        value=False,
        description='Activar'
    )
    
    r11=widgets.FloatText(
        value=1.5,
        description=r'\(a\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    ima11=widgets.FloatText(
        value=-2.5,
        description=r'\(b\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    
    Dos=widgets.Checkbox(
        value=True,
        description='Activar'
    )
    
    guardanota=widgets.Label(
        value=""
    )

   
    Malla=widgets.Checkbox(
        value=True,
        description='Malla'
    )
    
    Actilim=widgets.Checkbox(
        value=False,
        description='Activar limites'
    )
    
    Xmin=widgets.FloatText(value=-0.5,
            description='Xmin',
            step=0.5,
            continuous_update=False)
    
    Xmax=widgets.FloatText(value=0.5,
            description='Xmax',
            step=0.5,
            continuous_update=False)
    
    Ymin=widgets.FloatText(value=-0.5,
            description='Ymin',
            step=0.5,
            continuous_update=False)
    
    Ymax=widgets.FloatText(value=0.5,
            description='Ymax',
            step=0.5,
            continuous_update=False)

    
    
    boton=widgets.Button(
    description='Borrar seleccion',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Borrar',
    icon='')
    
    Guardar=widgets.Button(
    description='Guardar',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Guardar',
    icon='')
    
    lasx=widgets.FloatRangeSlider(
    value=[.1, 2],
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',)
    
    lasy=widgets.FloatRangeSlider(
    value=[.1, 2],
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='vertical',
    readout=True,
    readout_format='.1f',)

    
    form_items1 = [
        Box([r1]),
        Box([ima1]),
        Box([Uno])
        ]
    
    form_items2 = [
        Box([r11]),
        Box([ima11]),
        Box([Dos])
        ]

    
    form_items5 = [Box([Actilim]),Box([Malla]), Box([Guardar])]
    form_items6 = [Box([Xmin]),Box([Xmax]),Box([guardanota])]
    form_items7 = [Box([Ymin]),Box([Ymax])]


    
    box1 = widgets.VBox(form_items1)
    box2 = widgets.VBox(form_items2)
    box5 = widgets.VBox(form_items5)
    box6 = widgets.VBox(form_items6)
    box7 = widgets.VBox(form_items7)

    

    caja=Layout(
        border='solid 2px',
        width='100%'
    )

    aa=widgets.HBox([box1,box2], layout=caja)
    bb=widgets.HBox([box5,box6, box7], layout=caja)

    
    children = [aa, bb]
    tab = widgets.Tab(layout=caja)
    tab.children = children
    tab.set_title(0,'Grafica')
    tab.set_title(1, 'Vista')

    r11.value=real1
    ima11.value=imaginario1
    
    #display(titulo)
    guardanota.value=""
    display(interactive_output(Granum,{'real1':r1,'real11':r11,'imag11':ima11,                                       'uno':Uno,'dos':Dos,         'imag1':ima1, 'malla':Malla,'actilim':Actilim, 'xmin':Xmin, 'xmax':Xmax, 'ymin':Ymin,                                           'ymax':Ymax, }))
    
    
    display(tab)
    
    def on_guardar_clicked(b):
        guardanota.value="IMAGEN GUARDADA"
        Granum(uno=Uno.value,dos=Dos.value, malla=Malla.value,               actilim=Actilim.value, xmin=Xmin.value, xmax=Xmax.value, ymin=Ymin.value,              ymax=Ymax.value, real1=r1.value,imag1=ima1.value,real11=r11.value,imag11=ima11.value,
               guarda=True)
        
        


    Guardar.on_click(on_guardar_clicked)
    #def on_button_clicked(b):
     #   Suma.value=False
     #   Resta.value=False
     #   Multiplicacion.value=False
      #  Division.value=False
        


    #boton.on_click(on_button_clicked)
    
    def uno_value_change(change):
        Dos.value=not Uno.value
        

    Uno.observe(uno_value_change, names='value')
    
    def dos_value_change(change):
        Uno.value=not Dos.value

    Dos.observe(dos_value_change, names='value')




