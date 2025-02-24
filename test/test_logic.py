import unittest
import sys
sys.path.append("src")
from model.liquidacion_total import LiquidacionEmpleado as Liquidacion

class TestContractDetails(unittest.TestCase):

    def test_normal_1(self):
        
        #variables de entrada 
        fecha_inicio = "01/02/2024"
        fecha_fin = "30/06/2024"
        salario_auxilio = 1462000
        salario_sin_auxilio = 1300000

        #resultado esperado
        prima = 609167.00
        vacaciones = 270833.00
        cesantias = 609167.00
        intereses_cesantias = 30458.00
        liquidacion_total = 1519625.00

        #proceso
        prima_resultados = Liquidacion.calcular_prima(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        vacaciones_resultados = Liquidacion.calcular_vacaciones(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        cesantias_resultados = Liquidacion.calcular_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        intereses_cesantias_resultados = Liquidacion.calcular_intereses_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        liquidacion_total_resultados = Liquidacion.calcular_liquidacion_total(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    
    def test_normal_2(self):
        
        #variables de entrada 
        fecha_inicio = "01/01/2024"
        fecha_fin = "20/12/2024"
        salario_auxilio = 1662000
        salario_sin_auxilio = 1500000

        #resultado esperado
        prima =  784333
        vacaciones = 729167
        cesantias = 1615833
        intereses_cesantias = 188514
        liquidacion_total = 3585347

        #proceso
        prima_resultados = Liquidacion.calcular_prima(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        vacaciones_resultados = Liquidacion.calcular_vacaciones(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        cesantias_resultados = Liquidacion.calcular_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        intereses_cesantias_resultados = Liquidacion.calcular_intereses_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        liquidacion_total_resultados = Liquidacion.calcular_liquidacion_total(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_normal_3(self):
        
        #variables de entrada 
        fecha_inicio = "01/07/2024"
        fecha_fin = "30/10/2024"
        salario_auxilio =  3662000 
        salario_sin_auxilio = 3500000

        #resultado esperado
        prima = 1223445
        vacaciones = 583333 
        cesantias = 1222048
        intereses_cesantias = 48882
        liquidacion_total = 3077708  

        #proceso
        prima_resultados = Liquidacion.calcular_prima(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        vacaciones_resultados = Liquidacion.calcular_vacaciones(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        cesantias_resultados = Liquidacion.calcular_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        intereses_cesantias_resultados = Liquidacion.calcular_intereses_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        liquidacion_total_resultados = Liquidacion.calcular_liquidacion_total(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_extraordinario_1(self):
        
        #variables de entrada 
        fecha_inicio = "01/01/2021"
        fecha_fin = "30/12/2024"
        salario_auxilio =  1462000 
        salario_sin_auxilio = 1300000

        #resultado esperado
        prima = 2600000
        vacaciones = 2600000  
        cesantias = 5200000
        intereses_cesantias = 624000
        liquidacion_total = 14924000  

        #proceso
        prima_resultados = Liquidacion.calcular_prima(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        vacaciones_resultados = Liquidacion.calcular_vacaciones(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        cesantias_resultados = Liquidacion.calcular_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        intereses_cesantias_resultados = Liquidacion.calcular_intereses_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        liquidacion_total_resultados = Liquidacion.calcular_liquidacion_total(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_extraordinario_2(self):
        
        #variables de entrada 
        fecha_inicio = "16/01/2024"
        fecha_fin = "21/12/2024"
        salario_auxilio =  1462000 
        salario_sin_auxilio = 1300000

        #resultado esperado
        prima = 678206
        vacaciones = 597639  
        cesantias = 1396756
        intereses_cesantias = 154109
        liquidacion_total = 2420104 

        #proceso
        prima_resultados = Liquidacion.calcular_prima(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        vacaciones_resultados = Liquidacion.calcular_vacaciones(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        cesantias_resultados = Liquidacion.calcular_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        intereses_cesantias_resultados = Liquidacion.calcular_intereses_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        liquidacion_total_resultados = Liquidacion.calcular_liquidacion_total(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_extraordinario_3(self):
        
        #variables de entrada 
        fecha_inicio = "01/01/2024"
        fecha_fin = "20/12/2024"
        salario_auxilio =  1762000 
        salario_sin_auxilio = 1600000

        #resultado esperado
        prima = 865015
        vacaciones = 695833 
        cesantias = 1622961
        intereses_cesantias = 162837
        liquidacion_total = 3397114 

        #proceso
        prima_resultados = Liquidacion.calcular_prima(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        vacaciones_resultados = Liquidacion.calcular_vacaciones(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        cesantias_resultados = Liquidacion.calcular_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        intereses_cesantias_resultados = Liquidacion.calcular_intereses_cesantias(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        liquidacion_total_resultados = Liquidacion.calcular_liquidacion_total(salario_auxilio, salario_sin_auxilio, fecha_inicio, fecha_fin)
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)


if __name__ == '__main__':
    unittest.main()
