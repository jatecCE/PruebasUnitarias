from database import DataBase
import unittest


class TestDB(unittest.TestCase): 
    def test_IfExistFile (self):
         db = DataBase ("usuarios.txt")
         self.assertEqual(db.Read(),-2)    
    def test_Write(self):
        db = DataBase ("Test1.txt")
        self.assertEqual(db.EscribirArchivo("Test1"),None)  
    def test_ReadFromFile(self): 
        db = DataBase ("Test1.txt")
        self.assertGreater(len(db.Read()),0)
    def test_IngreseUsuario(self):
        db=DataBase("usuarios.txt")
        self.assertEquals(db.IngresarUsuario(apellido="Letion", edad=28, nombre="Jason"),None)
        
if __name__ == "__main__":
    unittest.main()