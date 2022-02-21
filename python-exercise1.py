print ("Bienvenidos al portal de la Federacion Nacional de Cacaoteros.")
print ("Analicemos el terreno donde tienes previsto plantar cacao.")
precipitacion = int(input("Cuanto es la precipitacion anual promedio en tu region en mm "))
profundidad = int(input("Cuanto es la profundidad efectiva en el suelo en cm "))
if (1800 <= precipitacion <=2599) and (profundidad > 100):
    print ("Sumamente apto")
elif (1800 <= precipitacion <=2599) and (50 <= profundidad <= 100):
    print ("Moderadamente apto")
elif (1800 <= precipitacion <=2599) and (25 <= profundidad < 50):
    print ("Marginalmente apto") 
elif (1800 <= precipitacion <=2599) and (profundidad < 25):
    print ("No apto")
elif ((2600 <= precipitacion <=3199)or(1500 <= precipitacion <=1799)) and (profundidad > 50):
    print ("Moderadamente apto")
elif ((2600 <= precipitacion <=3199)or(1500 <= precipitacion <=1799)) and (25 <= profundidad <= 50):
    print ("Marginalmente apto")
elif ((2600 <= precipitacion <=3199)or(1500 <= precipitacion <=1799)) and (profundidad < 25):
    print ("No apto")
elif ((3200 <= precipitacion <=3800)or(1200 <= precipitacion <=1499)) and (profundidad >= 25):
    print ("Marginalmente apto")
else:
    print ("No apto")
