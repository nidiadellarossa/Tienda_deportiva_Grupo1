#Para ver los datos de la table completa#
SELECT * FROM `proyecto_integrador_tienda_deportiva`. `personas`

#Para ver datos con filtro#

select `Documento`, `Razon_Social`
from `proyecto_integrador_tienda_deportiva`. `personas`

#Para ver un DNI#
select *
from `proyecto_integrador_tienda_deportiva`. `personas`
where `Documento` = '16361168'
