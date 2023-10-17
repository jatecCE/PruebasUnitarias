class DataBase: 
    def __init__(self, fileName):
        self.fileName=fileName
        
    def Read(self): 
        try :
            archivo=open(self.fileName) # coloca el contenido en memoria
            contenido=archivo.readlines()
            archivo.close()
        except:
            return -1
        return contenido # retorna el contenido del archivo
    def EscribirArchivo(self,dato):
        archivo=open(self.fileName,"a")#a->append
        archivo.write(dato+"\n") # escribe el dato en el archivo
        archivo.close()
    def IngresarUsuario(self,nombre,apellido,edad):
        registro=nombre+","+apellido+","+str(edad)
        try :
            self.EscribirArchivo(registro)
        except:
            return -1
    ########################################################
    def VerificaLogin(self,nombre):
        if isinstance(nombre,str):
                return self.VerificaUsuario(self.LeerArchivo(),nombre)

    #Verifica si un usuario está en el archivo
    def VerificaUsuario(self,listaUsuarios,usuario):
        if listaUsuarios==[]:
            return False
        elif listaUsuarios[0].split(",")[0]==usuario:#["jason","leiton","16\n"]
            return True
        else:
            return self.VerificaUsuario(listaUsuarios[1:],usuario)
