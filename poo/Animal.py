class Animal :
    def __init__(self,nombre):
        #print("se activo el constuctor")
        self.nombre=nombre
    def SetNombre (self,nombre):
            self.nombre=nombre
    def getNombre(self):
        return self.nombre

        
ob= Animal ("Pantera")
ob1=Animal("gato")
on1.setNombre("Lince")       
print(ob1.getNombre())

#public class Prueba{
#private String nombre;
#public void metodo (String nombre){
  #  this
#