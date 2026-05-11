#  Actividad 1 — APIs REST con Python y Flask

**Nombre:** Arturo Israel Martínez Córdova  
**Matrícula:** 1224100528  
**Grupo:** GTID153  
**Materia:** Aplicaciones Web Orientadas a Servicios

---

## ¿De qué trata esta actividad?

En esta actividad se crearon dos pequeñas APIs (servicios web) usando Python y Flask. Una API es básicamente un programa que escucha peticiones y responde con información. Aquí cada ejercicio resuelve un problema diferente.

---

#  Ejercicio 1 — Calculadora de Promedio de Calificaciones

## ¿Qué hace?

Recibe el nombre de un estudiante y una lista de calificaciones, y devuelve el promedio calculado automáticamente.

**Ejemplo:** Si mandas las calificaciones `[80, 90, 85, 70]`, te regresa `81.25`.

##  Archivos del proyecto

```
ejercicio1/
├── app.py              ← El código principal de la API
├── requirements.txt    ← Las librerías que necesita instalar
├── .gitignore          ← Archivos que Git debe ignorar
└── README.md           ← Documentación original
```

##  Cómo correrlo paso a paso

### Paso 1 — Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd ejercicio1
```

### Paso 2 — Crear el entorno virtual

```bash
python -m venv venv
```

Activarlo en **Windows:**
```bash
venv\Scripts\activate
```

Activarlo en **Mac / Linux:**
```bash
source venv/bin/activate
```

### Paso 3 — Instalar lo necesario

```bash
pip install -r requirements.txt
```

### Paso 4 — Correr la API

```bash
python app.py
```

La API quedará disponible en: `http://127.0.0.1:5000`

---

##  Cómo usarla

### Endpoint: `POST /promedio`

Le mandas un JSON con el nombre y las calificaciones, y te responde con el promedio.

**¿Qué le mandas?**
```json
{
  "nombre": "Juan",
  "calificaciones": [80, 90, 85, 70]
}
```

**¿Qué te regresa si todo está bien? (código 200)**
```json
{
  "nombre": "Juan",
  "calificaciones": [80, 90, 85, 70],
  "promedio": 81.25
}
```

**¿Qué pasa si falta el nombre o las calificaciones? (código 400)**
```json
{
  "error": "Se requiere 'nombre' y 'calificaciones'"
}
```

**¿Qué pasa si mandas la lista vacía? (código 400)**
```json
{
  "error": "La lista de calificaciones no puede estar vacía"
}
```

---

##  Cómo probarlo en Postman

1. Abre Postman
2. Crea una nueva petición
3. Selecciona el método **POST**
4. Pon esta URL: `http://127.0.0.1:5000/promedio`
5. Ve a la pestaña **Body** → elige **raw** → selecciona **JSON**
6. Pega este ejemplo:

```json
{
  "nombre": "Juan",
  "calificaciones": [80, 90, 85, 70]
}
```

7. Haz clic en **Send** y verás la respuesta abajo

![Prueba en Postman](imagenes/prueba.png)

---

##  Tecnologías usadas

- Python 3.8+
- Flask 3.1.0

---
---

#  Ejercicio 2 — Conversor de Temperaturas

## ¿Qué hace?

Convierte temperaturas entre Celsius y Fahrenheit. Le dices cuántos grados tienes y en qué escala, y la API te regresa el equivalente en la otra escala.

**Fórmulas que usa:**

| Conversión | Fórmula |
|---|---|
| Celsius → Fahrenheit | `(°C × 9/5) + 32` |
| Fahrenheit → Celsius | `(°F − 32) × 5/9` |

##  Archivos del proyecto

```
ejercicio2/
├── app.py              ← El código principal de la API
├── requirements.txt    ← Las librerías que necesita instalar
├── .gitignore          ← Archivos que Git debe ignorar
└── README.md           ← Documentación original
```

##  Cómo correrlo paso a paso

### Paso 1 — Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd ejercicio2
```

### Paso 2 — Crear el entorno virtual

```bash
python -m venv venv
```

Activarlo en **Windows:**
```bash
venv\Scripts\activate
```

Activarlo en **Mac / Linux:**
```bash
source venv/bin/activate
```

### Paso 3 — Instalar lo necesario

```bash
pip install -r requirements.txt
```

### Paso 4 — Correr la API

```bash
python app.py
```

La API quedará disponible en: `http://127.0.0.1:5001`

> Nota: este ejercicio corre en el puerto **5001** para no chocar con el ejercicio 1.

---

## 🔌 Cómo usarla

### Endpoint: `POST /convertir-temperatura`

Le mandas un número y la escala de origen, y te regresa el valor convertido.

**¿Qué le mandas?**
```json
{
  "valor": 100,
  "escala": "Celsius"
}
```

El campo `escala` acepta `"Celsius"` o `"Fahrenheit"` (no importa si usas mayúsculas o minúsculas).

**¿Qué te regresa si conviertes Celsius a Fahrenheit? (código 200)**
```json
{
  "valor_original": 100,
  "escala_origen": "Celsius",
  "resultado": 212.0,
  "escala_destino": "Fahrenheit"
}
```

**¿Qué te regresa si conviertes Fahrenheit a Celsius? (código 200)**
```json
{
  "valor_original": 32,
  "escala_origen": "Fahrenheit",
  "resultado": 0.0,
  "escala_destino": "Celsius"
}
```

**¿Qué pasa si falta algún dato? (código 400)**
```json
{
  "error": "Se requiere 'valor' (número) y 'escala' (Celsius o Fahrenheit)"
}
```

**¿Qué pasa si la escala no es válida? (código 400)**
```json
{
  "error": "Escala inválida. Use 'Celsius' o 'Fahrenheit'"
}
```

---

##  Casos de prueba

Puedes probar estos valores para verificar que todo funciona bien:

| Valor | Escala de entrada | Resultado esperado | Escala de salida |
|---|---|---|---|
| 0 | Celsius | 32.0 | Fahrenheit |
| 100 | Celsius | 212.0 | Fahrenheit |
| 37 | Celsius | 98.6 | Fahrenheit |
| 32 | Fahrenheit | 0.0 | Celsius |
| 212 | Fahrenheit | 100.0 | Celsius |
| -40 | Celsius | -40.0 | Fahrenheit |

---

##  Cómo probarlo en Postman

1. Abre Postman
2. Crea una nueva petición
3. Selecciona el método **POST**
4. Pon esta URL: `http://127.0.0.1:5001/convertir-temperatura`
5. Ve a la pestaña **Body** → elige **raw** → selecciona **JSON**
6. Pega uno de estos ejemplos:

**Celsius a Fahrenheit:**
```json
{
  "valor": 100,
  "escala": "Celsius"
}
```

**Fahrenheit a Celsius:**
```json
{
  "valor": 32,
  "escala": "Fahrenheit"
}
```

7. Haz clic en **Send**

![Prueba en Postman](imagenes/prueba.png)

---

##  Tecnologías usadas

- Python 3.8+
- Flask 3.1.0
