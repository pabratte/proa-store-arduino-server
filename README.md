# PROA Store Arduino Server

Aplicación para consultar por HTTP/HTTPS el código RFID leído por una placa Arduino conectada al servidor

![](docs/architecture.svg)

## Uso

```
python manage.py runserver 7000
```

## Simular lectura de sensores RFID

Con el servidor corriendo, acceder a la siguiente URL:

```
http://localhost:7000/simulate_code
```