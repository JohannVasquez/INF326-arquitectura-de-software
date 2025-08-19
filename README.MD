# Video explicativo de la tarea
```bash
https://youtu.be/i3M0H1xFb-Y
```

# Como correr el codigo
Se necesita tener docker instalado

La forma en que lo corrí yo el codigo es
(Hay que estar dentro de la carpeta "Tarea 1" para que funcione)
```bash
docker compose up --build loki
```
luego probar el comando `curl http://localhost:3100/ready` hasta que diga *ready*

despues de esto levantar los demas contenedores con

```bash
docker compose up --build service-a service-b grafana promtail
```

usuario y contraseña del grafana son admin:admin


---

# Endpoints de servicios
Para el servicio a
```bash
http://localhost:8000/ping
http://localhost:8000/work
```

Para el servicio b
```bash
http://localhost:8001/ping
http://localhost:8001/work
```

---

# Grafana
Para acceder a grafana se tiene que utilizar el siguiente link
```bash
http://localhost:3000
```