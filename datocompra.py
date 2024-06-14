
#Insert

insert into operaciones (id, fecha,id_persona, tipo_operacion, tipo_pago) values ('112233','60555335'20-05-02,'COMPRA', 'CUENTA_CORRIENTE')
self.db.execute_query(query, ('id', 'fecha','id_persona', 'tipo_operacion', 'tipo_pago'))
print ("Compra realizada correctamente")


insert into detalle_operacion, ('id', 'id_operacion', 'id_producto', 'cantidad', 'precio_unidad', 'descuento') values ('123', '112233', '25', '12000', '0.15'); 
self.db.execute_query(query ('id', 'id_operacion', 'id_producto', 'cantidad', 'precio_unidad', 'descuento')
print ("Se creo correctamente el detalle de la operacion")


#Read

Select * from operaciones


#Read con where

Select id, id_persona, tipo_operacion from operaciones
where id_persona =112233


#Eliminar dato de tabla

delete from operaciones where id= 112233
self.db.execute_query(query(id))
print ("Operacion eliminada")

#Update

update operaciones
set cantidad=30, precio_unidad= 15000
where id=112233



