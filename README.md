#  Ejercicio 3.2 — Pruebas de la API de Estudiantes

**Nombre:** Arturo Israel Martínez Córdova  
**Matrícula:** 1224100528  
**Grupo:** GTID153  
**Unidad:** 3 — Aplicaciones Web Orientadas a Servicios

---

## ¿De qué trata este ejercicio?

Aquí probamos que nuestra API de estudiantes funcione bien. Básicamente le hacemos preguntas a la API y comprobamos que nos responda correctamente.

Las operaciones que probamos son:

| Qué hace | Endpoint |
|---|---|
|  Crear un estudiante | `POST /api/estudiantes/` |
|  Ver la lista de estudiantes | `GET /api/estudiantes/` |
|  Buscar un estudiante por ID | `GET /api/estudiantes/<id>` |
|  Actualizar datos de un estudiante | `PUT /api/estudiantes/<id>` |
|  Eliminar un estudiante | `DELETE /api/estudiantes/<id>` |

---

##  Cómo debe quedar organizada tu carpeta

```
mi_api/
├── pytest.ini                ← Configuración de las pruebas
├── tests/
│   ├── __init__.py           ← Archivo vacío (necesario para Python)
│   ├── conftest.py           ← Configuración compartida de las pruebas
│   └── test_estudiantes.py  ← Las pruebas del ejercicio 3.2
├── app/
│   ├── __init__.py
│   ├── config.py             ← Aquí hay que agregar TestingConfig
│   ├── models/
│   │   └── estudiante.py
│   └── routes/
│       └── estudiantes.py
└── run.py
```

---

##  Cómo correr las pruebas (paso a paso)

### Paso 1 — Agregar la configuración de pruebas

Abre el archivo `app/config.py` y pega esto al final:

```python
class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Base de datos temporal
    WTF_CSRF_ENABLED = False
    JWT_ACCESS_TOKEN_EXPIRES = False
```

>  Esto le dice a la app que use una base de datos temporal solo para pruebas, sin tocar la real.

---

### Paso 2 — Instalar las herramientas necesarias

Abre la terminal en VS Code con `Ctrl + ñ` y escribe:

```bash
pip install pytest pytest-flask pytest-cov
```

Para verificar que se instaló bien:

```bash
pytest --version
```

Deberías ver algo como: `pytest 8.x.x`

---

### Paso 3 — Ejecutar las pruebas

Desde la carpeta raíz del proyecto (`mi_api/`), corre:

```bash
pytest tests/test_estudiantes.py -v
```

---

##  Resultado esperado

Si todo está bien, deberías ver esto:

```
tests/test_estudiantes.py::TestCrearEstudiante::test_crear_estudiante_exitoso        PASSED
tests/test_estudiantes.py::TestCrearEstudiante::test_matricula_duplicada_retorna_409 PASSED
tests/test_estudiantes.py::TestCrearEstudiante::test_campo_email_requerido           PASSED
tests/test_estudiantes.py::TestCrearEstudiante::test_body_vacio_retorna_400          PASSED
tests/test_estudiantes.py::TestObtenerEstudiante::test_lista_devuelve_200            PASSED
tests/test_estudiantes.py::TestObtenerEstudiante::test_lista_vacia_retorna_lista_vacia PASSED
tests/test_estudiantes.py::TestObtenerEstudiante::test_obtener_por_id_existente      PASSED
tests/test_estudiantes.py::TestObtenerEstudiante::test_id_inexistente_retorna_404    PASSED
tests/test_estudiantes.py::TestObtenerEstudiante::test_paginacion[1-5-5]             PASSED
tests/test_estudiantes.py::TestObtenerEstudiante::test_paginacion[2-5-5]             PASSED
tests/test_estudiantes.py::TestObtenerEstudiante::test_paginacion[1-100-10]          PASSED
tests/test_estudiantes.py::TestActualizarEstudiante::test_actualizar_semestre        PASSED
tests/test_estudiantes.py::TestEliminarEstudiante::test_borrado_logico               PASSED

13 passed 
```

---

##  ¿Qué prueba cada parte?

###  Crear estudiante (`TestCrearEstudiante`)

| Prueba | ¿Qué verifica? |
|---|---|
| `test_crear_estudiante_exitoso` | Que crear un estudiante con datos correctos devuelva código 201 |
| `test_matricula_duplicada_retorna_409` | Que no se pueda crear dos veces el mismo estudiante |
| `test_campo_email_requerido` | Que si falta el email, la API lo rechace con error 400 |
| `test_body_vacio_retorna_400` | Que enviar una petición vacía no rompa el servidor |

###  Obtener estudiante (`TestObtenerEstudiante`)

| Prueba | ¿Qué verifica? |
|---|---|
| `test_lista_devuelve_200` | Que la lista de estudiantes siempre responda correctamente |
| `test_lista_vacia_retorna_lista_vacia` | Que si no hay nadie, devuelva una lista vacía (no un error) |
| `test_obtener_por_id_existente` | Que buscar por ID devuelva al estudiante correcto |
| `test_id_inexistente_retorna_404` | Que buscar un ID que no existe devuelva error 404 |
| `test_paginacion` | Que la paginación funcione con distintas combinaciones |

###  Actualizar estudiante (`TestActualizarEstudiante`)

| Prueba | ¿Qué verifica? |
|---|---|
| `test_actualizar_semestre` | Que modificar un campo del estudiante funcione y se refleje en la respuesta |

###  Eliminar estudiante (`TestEliminarEstudiante`)

| Prueba | ¿Qué verifica? |
|---|---|
| `test_borrado_logico` | Que eliminar un estudiante lo marque como inactivo (no lo borra de verdad) |

---

##  Comandos útiles

```bash
# Correr solo un grupo de pruebas
pytest tests/test_estudiantes.py::TestCrearEstudiante -v

# Correr solo una prueba específica
pytest tests/test_estudiantes.py::TestCrearEstudiante::test_crear_estudiante_exitoso -v

# Ver los print() dentro de las pruebas
pytest tests/test_estudiantes.py -v -s

# Parar al primer error
pytest tests/test_estudiantes.py -v -x

# Ver cuánto del código cubren las pruebas
pytest tests/test_estudiantes.py -v --cov=app --cov-report=term-missing
```

---

##  Solución a errores comunes

| Error que ves | Qué hacer |
|---|---|
| `ModuleNotFoundError: app` | Asegúrate de correr pytest desde la carpeta `mi_api/`, no desde dentro de `tests/` |
| `ImportError: cannot import TestingConfig` | Revisa que hayas pegado la clase `TestingConfig` en `config.py` |
| `404` en todos los endpoints | Verifica que el blueprint de estudiantes esté registrado en `create_app()` |
| `AssertionError` en el status code | Tu API está respondiendo con un código diferente — revisa la lógica del endpoint |

---

##  Archivos incluidos

| Archivo | Para qué sirve |
|---|---|
| `test_estudiantes.py` | Contiene las 13 pruebas del ejercicio |
| `conftest.py` | Prepara la app, la base de datos y el cliente HTTP antes de cada prueba |
| `pytest.ini` | Le dice a pytest dónde buscar las pruebas y cómo ejecutarlas |
| `__init__.py` | Archivo vacío necesario para que Python reconozca la carpeta `tests/` |
