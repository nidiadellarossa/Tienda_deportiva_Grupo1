dbsetup_script = """
CREATE DATABASE IF NOT EXISTS tienda_ropa;
USE tienda_ropa;

CREATE TABLE IF NOT EXISTS `persona` (
  `documento` int PRIMARY KEY,
  `tipo_documento` varchar(255),
  `razon_social` varchar(255)
);

CREATE TABLE IF NOT EXISTS `direccion_fiscal` (
  `id` int PRIMARY KEY,
  `id_persona` int,
  `calle` varchar(255),
  `numero` int,
  `piso` varchar(255),
  `departamento` varchar(255),
  `id_localidad` int
);

CREATE TABLE IF NOT EXISTS `localidad` (
  `cod_postal` int PRIMARY KEY,
  `nombre` varchar(255),
  `id_provincia` int
);

CREATE TABLE IF NOT EXISTS `provincia` (
  `id` int PRIMARY KEY,
  `nombre` varchar(255)
);

CREATE TABLE IF NOT EXISTS `telefono` (
  `id` int PRIMARY KEY,
  `id_persona` int,
  `numero` varchar(255)
);

CREATE TABLE IF NOT EXISTS `email` (
  `id` int PRIMARY KEY,
  `id_persona` int,
  `direccion` varchar(255)
);

CREATE TABLE IF NOT EXISTS `datos_personas_fisicas` (
  `id` int PRIMARY KEY,
  `id_persona` int,
  `fecha_nacimiento` datetime,
  `genero` varchar(255)
);

CREATE TABLE IF NOT EXISTS `productos` (
  `codigo` int PRIMARY KEY,
  `denominacion` varchar(255),
  `id_categoria` int,
  `id_proveedor` int,
  `precio_unit` decimal,
  `stock` decimal
);

CREATE TABLE IF NOT EXISTS `operaciones` (
  `id` int PRIMARY KEY,
  `fecha` datetime,
  `id_persona` int,
  `tipo_operacion` varchar(255)
  `tipo_pago` varchar(255)
);

CREATE TABLE IF NOT EXISTS `detalle_operacion` (
  `id` int PRIMARY KEY,
  `id_operacion` int,
  `id_producto` int,
  `cantidad` decimal,
  `precio_unidad` decimal,
  `descuento` decimal
);

CREATE TABLE IF NOT EXISTS `categoria_producto` (
  `id` int PRIMARY KEY,
  `nombre` varchar(255)
);

ALTER TABLE `direccion_fiscal` ADD FOREIGN KEY (`id_persona`) REFERENCES `persona` (`documento`);

ALTER TABLE `direccion_fiscal` ADD FOREIGN KEY (`id_localidad`) REFERENCES `localidad` (`cod_postal`);

ALTER TABLE `localidad` ADD FOREIGN KEY (`id_provincia`) REFERENCES `provincia` (`id`);

ALTER TABLE `telefono` ADD FOREIGN KEY (`id_persona`) REFERENCES `persona` (`documento`);

ALTER TABLE `email` ADD FOREIGN KEY (`id_persona`) REFERENCES `persona` (`documento`);

ALTER TABLE `datos_personas_fisicas` ADD FOREIGN KEY (`id_persona`) REFERENCES `persona` (`documento`);

ALTER TABLE `productos` ADD FOREIGN KEY (`id_categoria`) REFERENCES `categoria_producto` (`id`);

ALTER TABLE `productos` ADD FOREIGN KEY (`id_proveedor`) REFERENCES `persona` (`documento`);

ALTER TABLE `operaciones` ADD FOREIGN KEY (`id_persona`) REFERENCES `persona` (`documento`);

ALTER TABLE `detalle_operacion` ADD FOREIGN KEY (`id_operacion`) REFERENCES `operaciones` (`id`);

ALTER TABLE `detalle_operacion` ADD FOREIGN KEY (`id_producto`) REFERENCES `productos` (`codigo`);
"""