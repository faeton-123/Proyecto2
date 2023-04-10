DDL_QUERY =  '''

CREATE TABLE IF NOT EXISTS dim_fecha
(
    id_fecha INT PRIMARY KEY,
    fecha TIMESTAMP,
    dia_semana varchar(10),
    mes varchar(10)
);

CREATE TABLE IF NOT EXISTS dim_cajeros
(
    id_cajero INT PRIMARY KEY,
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    id_cargo INT
);

CREATE TABLE IF NOT EXISTS dim_tienda(
    id_tienda INT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE,
    id_gerente INT
);

SELECT * FROM dim_tienda;

CREATE TABLE IF NOT EXISTS dim_producto(
    id_producto INT PRIMARY KEY,
    sku_numero VARCHAR(15) UNIQUE,
    id_gerente INT,
    marca VARCHAR(15),
    categoria VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS dim_promocion(
    id_promocion INT PRIMARY KEY,
    codigo_promocional VARCHAR(15) UNIQUE
);


CREATE TABLE IF NOT EXISTS dim_pago(
    id_pago INT PRIMARY KEY,
    metodo_pago VARCHAR(15) UNIQUE
);


CREATE TABLE IF NOT EXISTS dim_direccionEnvio
(
    id_direccion INT PRIMARY KEY,
    no_casa VARCHAR(15),
    avenida VARCHAR(50),
    calle VARCHAR(50),
    zona INT
);

CREATE TABLE IF NOT EXISTS transacciones
(
	id_transaccion INT PRIMARY KEY,
	cantidad_vendida INT,
	monto DOUBLE PRECISION,
	id_fecha int references dim_fecha(id_fecha),
	id_tienda int references dim_tienda(id_tienda),
	id_cajeros int references dim_cajeros(id_cajeros),
	id_producto int references dim_producto(id_producto),
	id_promocion int references dim_promocion(id_promocion),
	id_pago int references dim_pago(id_pago),
	id_direccion int references dim_direccionEnvio(id_direccion)
);

'''