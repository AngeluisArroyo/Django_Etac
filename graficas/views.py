from django.shortcuts import render

def grafica_view(request):
    ''' 
    datos para la grafica 
    
    Args:
    requests (_type_): _descripcion_
    ''' 
    
    etiquetas = ['Enero','Frebrero','Marzo','Abril','Mayo']
    
    datos = [5,15,10,20,25]
    
    return render (request,'graficas/graficas.html', {
        'etiquetas':etiquetas,
        'datos':datos
    })
def grafica_view_2(request):
    ''' 
    datos para la grafica 
    
    Args:
    requests (_type_): _descripcion_
    ''' 
    
    etiquetas = ['Enero','Frebrero','Marzo','Abril','Mayo']
    
    datos = [5,15,10,20,25]
    
    return render (request,'graficas/graficas_2.html', {
        'etiquetas':etiquetas,
        'datos':datos
    })
def grafica_view_3(request):
    ''' 
    datos para la grafica 
    
    Args:
    requests (_type_): _descripcion_
    ''' 
    
    etiquetas = ['Enero','Frebrero','Marzo','Abril','Mayo']
    
    datos = [50,150,100,200,300]
    
    return render (request,'graficas/graficas_3.html', {
        'etiquetas':etiquetas,
        'datos':datos
    })
