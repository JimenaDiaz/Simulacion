
# Simulacion

## Funcionamiento

Se crean tres clases una para cada microservicio.

### Class Producer
En esta clase se crea un loop el cual genera los eventos, la metricas se generan de manera aleatoria en un rango de (10-100). 

### Class Crud
En esta clase en el constructor se crea el archivo data.csv, mientras que en la función write se escriben en el archivo los eventos, donde el index se utiliza como 
el Id del dispositivo.

### Class Consumer
En esta clase se crea un loop para que se ejecute el numero de eventos de acuerdo a la cantidad establecida y llama a la funcion write de la clase Crud para guardar 
la data que recibe.
 
Para utilizar el proyecto se debe crear un objeto por cada clase, las clases Producer y Consumer heredan de la libreria Thread por lo que para iniciar se debe utilizar 
el metodo start finalmente se utiliza el join para esperar que todos los hilos finalicen y de esta forma comprobar el funcionamiento del sistema.

Se utiliza el time.sleep para corroborar que todos los eventos sean leidos sin importar las demoras del sistema.

## Diseño de Arquitectura

