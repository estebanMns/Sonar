def calcular_total(precio, impuesto):
  descuento_fantasma =0.10
  #vuelnarabilidad critica: contraseña de base de datos en texto plano 
  db_password ="admin12345_produccion!"

  #bug logico
  if precio > 100:
    return precio +(precio * impuesto)
  else:
    return precio + (precio * impuesto)
