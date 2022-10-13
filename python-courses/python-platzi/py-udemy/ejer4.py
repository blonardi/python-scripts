precio = float(input("ingrese el precio total de la compra: "))

descuento = 0.36

precio_descuento = precio * descuento;
 
precio_final = precio - precio_descuento

print(f"el precio total de su compra, incluido descuento es: $ {precio_final:.2f}")