# Especificación de Requerimientos: Manual Exhaustivo de Python para SDET

## Tabla de Contenidos

1. [Objetivo General](#1-objetivo-general)
2. [Perfil del Estudiante y Audiencia](#2-perfil-del-estudiante-y-audiencia)
3. [Reglas de Estilo y Código](#3-reglas-de-estilo-y-código)
4. [Temario Detallado por Módulos](#4-temario-detallado-por-módulos)

---

## 1. Objetivo General

Generar un manual técnico, pedagógico y exhaustivo en un único archivo titulado `python-ultimate-course.md`. El documento debe capacitar a una persona sin experiencia previa en programación para convertirse en un **SDET** (*Software Development Engineer in Test*) de alto nivel profesional, utilizando Python como primer lenguaje formal con tipado estricto moderno (**Python 3.10+**) y enfocado en automatización industrial de pruebas (Playwright, pytest, API testing y Page Object Model desacoplado).

## 2. Perfil del Estudiante y Audiencia

- **Punto de partida:** Cero absoluto en código. Aprenderá los conceptos de computación, runtime y tipado directamente en Python sin atajos informales.
- **Rol actual:** QA Manual en transición a SDET / Automatizador de software.
- **Mentalidad didáctica:** No busca snippets aislados. Requiere entender la arquitectura interna (CPython, bytecode, gestión de memoria, recuento de referencias, GIL) combinada con pragmatismo de testing (parsing de payloads JSON, extracción de selectores con expresiones regulares, asincronía, POM con dataclasses y protocolos, fixtures de prueba y assertions de alta confiabilidad).

## 3. Reglas de Estilo y Código

1. **Bloques ejecutables:** Todo el código debe estar dentro de bloques ` ```python ` autocontenidos y listos para ejecutar.
2. **Tipado estricto moderno (Python 3.10+):** Utilizar Type Hints en todo momento (`int | str` en lugar de `Union[int, str]`, `list[str]` en lugar de `List[str]`), empleando el módulo `typing` para construcciones avanzadas (`Callable`, `Protocol`, `TypeVar`, `Any`).

   Ejemplo base de estilo inicial:

   ```python
   name: str = "Joe"
   age: int = 12
   is_active: bool = True
   ```

3. **Estructura pedagógica por concepto:**
   - **Definición conceptual:** Qué problema resuelve y analogía clara.
   - **Bajo el capó:** Cómo se comporta CPython, la memoria o el evaluador de tipos.
   - **Código reproducible:** Ejemplo mínimo ejecutable y comentado.
   - **Aplicación SDET:** Cómo se usa en frameworks de testing (evitar flaky tests, manejo de datos dinámicos, fixtures).
4. **Batería de ejercicios obligatoria:**
   - **Módulos introductorios o de repaso:** mínimo 5 ejercicios con enunciados, entradas/salidas esperadas y solución comentada.
   - **Módulos complejos** (strings/regex, colecciones funcionales, POO/dataclasses, asincronía, decoradores, pytest/fixtures, archivos y configuración, testing de APIs, mocking y framework con CI): mínimo 10 ejercicios con solución completa explicada.
5. **Cero omisiones:** Prohibido usar comentarios de relleno como `# TODO: completar resto` o resumir explicaciones.

---

## 4. Temario Detallado por Módulos

### Módulo 0: Entorno, Aislamiento y Herramientas Modernas de Python

#### Arquitectura de instalación e intérprete

- Qué es Python, CPython y cómo se diferencia el código fuente del bytecode (`.pyc` dentro de `__pycache__`).
- Gestión de versiones de Python y verificación en terminal (`python3 --version`).

#### Entornos virtuales y gestión de dependencias (Fundamento crítico)

- El peligro de instalar librerías en el entorno global del sistema operativo.
- Módulo nativo `venv`: creación (`python3 -m venv .venv`), activación (Windows PowerShell vs. macOS/Linux Bash/Zsh) y desactivación.
- Herramientas modernas de empaquetado y resolución ultrarrápida: introducción práctica a `uv` y `pip`.
- Estructura y propósito de `requirements.txt` vs. el estándar moderno `pyproject.toml`.

#### Configuración de VS Code como IDE profesional de Python

- Extensiones indispensables: Python (Microsoft), Pylance (Language Server), Ruff (linter y formateador ultrarrápido), Python Test Adapter.
- Configuración en `.vscode/settings.json`: selección automática del `.venv`, auto-formateo con Ruff al guardar, activación de type checking estricto en Pylance (`typeCheckingMode: "basic"` o `"strict"`).

#### Verificación estática y linting desde terminal

- Ejecución de `ruff check` y `ruff format`.
- Introducción al type checker estático `mypy` y creación de un archivo básico de configuración (`mypy.ini` o sección en `pyproject.toml`).

> **Ejercicios Módulo 0:** 5 ejercicios prácticos guiados para crear entornos, instalar dependencias y validar la configuración de tipos en VS Code.

---

### Módulo 1: Runtime, Modelo de Memoria y Tipado Moderno

#### Cómo ejecuta Python el código

- Ciclo de vida del script: Código fuente → Compilador de CPython → Bytecode (`.pyc`) → Máquina Virtual de Python (PVM).
- El GIL (*Global Interpreter Lock*): qué es a nivel conceptual y por qué afecta a hilos de CPU pero no a operaciones de red/I/O (Playwright, peticiones HTTP).

#### Modelo de memoria y sistema de objetos

- Todo en Python es un objeto (`PyObject`): identidad (`id()`), tipo (`type()`) y valor.
- Variables como etiquetas/punteros hacia objetos en memoria, no como "cajas contenedoras".
- Recuento de referencias (*Reference Counting*) y ciclo del Garbage Collector para referencias circulares.
- Mutabilidad vs. Inmutabilidad: tipos inmutables (`int`, `float`, `str`, `tuple`, `frozenset`, `bool`) vs. mutables (`list`, `dict`, `set`). Trampas comunes con valores por defecto mutables en funciones.

#### Tipos primitivos y operadores

- `int`, `float`, `str`, `bool`, `NoneType` (`None`).
- Operadores aritméticos, lógicos (`and`, `or`, `not`) y de comparación.
- Igualdad de valor (`==`) vs. Identidad de memoria (`is`): por qué usar siempre `if variable is None:` y nunca `if variable == None:`.
- Evaluación de cortocircuito (*Short-circuit evaluation*) y valores Truthy/Falsy (`0`, `""`, `[]`, `{}`, `None` como falso lógico).

#### Sistema de Type Hints estricto

- Sintaxis moderna de anotación: variables, parámetros y retornos (`def sum(a: int, b: int) -> int:`).
- Tipos opcionales y uniones: `str | None` y `int | float`.
- El tipo especial `Any` (por qué evitarlo) vs. `object`.

#### Control de flujo: condicionales y bucles

- Bloques e indentación como parte de la sintaxis (`IndentationError`).
- `if` / `elif` / `else`, condiciones compuestas, expresión condicional (ternario), *guard clauses* y comparaciones encadenadas.
- Bucle `for`, `range()`, `enumerate()`, `zip()` (incluido `strict=True`) e iteración de diccionarios.
- Bucle `while`, condiciones de salida y patrón de *polling* con timeout (base conceptual del *auto-waiting* de Playwright).
- `break`, `continue`, `pass` y la cláusula `else` en bucles; salida limpia de bucles anidados.
- Operador morsa `:=`.

> **Ejercicios Módulo 1:** 11 ejercicios prácticos sobre mutabilidad, identidad de memoria, refactorización con operadores estrictos, anotaciones de tipo validadas con `mypy` y control de flujo (clasificación de respuestas HTTP, *polling* con timeout, comparación de tablas).

---

### Módulo 2: Dominio Quirúrgico de Strings y Expresiones Regulares (`re`)

*Énfasis prioritario para SDET: extracción, normalización y validación de texto en UIs y APIs.*

#### Manipulación avanzada de cadenas

- Inmutabilidad del string y operaciones en memoria.
- Indexación y Slicing exhaustivo: `s[start:stop:step]`, inversión de cadenas con `[::-1]`.
- Formateo moderno con f-strings: interpolación, especificadores de formato para moneda/decimales (`f"{price:.2f}"`), fechas y alineación (`<`, `>`, `^`).
- Métodos nativos indispensables: `upper()`, `lower()`, `strip()`, `lstrip()`, `rstrip()`, `startswith()`, `endswith()`, `replace()`, `split()`, `join()`, `zfill()`.

#### Algoritmia práctica con Strings para SDET

- Conteo de frecuencias sin dependencias externas.
- Limpieza y normalización de textos con caracteres invisibles o saltos de línea (típico de locators de Playwright).
- Inversión de strings mediante iteradores y algoritmos de dos punteros.

#### Expresiones Regulares con el módulo nativo `re`

- Raw strings (`r"..."`) y compilación de patrones con `re.compile()`.
- Búsqueda y coincidencia: `re.search()`, `re.match()`, `re.findall()`, `re.finditer()`, `re.sub()`.
- Grupos de captura y grupos nombrados: `(?P<group_name>pattern)`.

#### Casos reales de automatización

- Extraer códigos de verificación (OTP de 6 dígitos) de cadenas o correos.
- Parseo de precios complejos con símbolos de divisa (`"Total: $ 1,450.75 USD"` → `float` `1450.75`).
- Validación estricta de formatos UUIDv4, correos RFC 5322 y timestamps ISO 8601.

> **Ejercicios Módulo 2:** 10 ejercicios prácticos centrados en validaciones de UI, limpieza de textos raspados y parsing de logs.

---

### Módulo 3: Colecciones Nativas, Desempaquetado y Comprensiones

#### Listas (`list[T]`) y Tuplas (`tuple[T, ...]`)

- Arrays dinámicos en CPython: costo amortizado de `append()` vs. costo *O(n)* de `insert(0, val)`.
- Métodos principales: `append`, `extend`, `pop`, `sort` (in-place) vs. función `sorted()` (inmutable).
- Tuplas como registros inmutables y claves de diccionarios.

#### Diccionarios (`dict[K, V]`) y Conjuntos (`set[T]`)

- Tablas Hash bajo el capó: funciones de hash (`hash()`), requisitos para que un tipo sea hashable y complejidad temporal *O(1)*.
- Métodos seguros de diccionarios: `get()`, `setdefault()`, `keys()`, `values()`, `items()`.
- Conjuntos (`set` y `frozenset`): operaciones matemáticas de conjuntos (unión `|`, intersección `&`, diferencia `-`) aplicadas a validaciones de datos de prueba.

#### Técnicas avanzadas de Python

- Desempaquetado posicional y extendido (`a, *rest, b = data`).
- Operadores de desempaquetado en colecciones: `*` para iterables y `**` para diccionarios (fusión de payloads de prueba).
- Sentencia `match` / `case` (Pattern Matching introducido en Python 3.10) para evaluar estructuras de respuestas API complejas.

#### List, Dict y Set Comprehensions (Estilo idiomático)

- Sintaxis de comprensión con filtros condicionales: `[transform(x) for x in items if condition(x)]`.
- Comprensiones anidadas para aplanar tablas de datos.
- Diferencia fundamental de memoria entre List Comprehensions y Expresiones Generadoras (`(x for x in data)`).

#### Módulo `collections`

- `defaultdict` para agrupaciones de métricas sin `KeyError`.
- `Counter` para conteos rápidos de elementos repetidos en pruebas.
- `namedtuple` para estructuras de datos ligeras e inmutables.

> **Ejercicios Módulo 3:** 10 ejercicios con payloads JSON simulados, deduplicación de tablas web y transformaciones de datos con comprehensions.

---

### Módulo 4: Funciones, Control de Ámbito (Scope) y Closures

#### Parámetros y firmas de funciones profesionales

- Parámetros posicionales, con nombre (*keyword*) y valores por defecto.
- Argumentos variables arbitrarios: `*args` (tupla) y `**kwargs` (diccionario).
- Parámetros estrictos: solo posicionales (`/`) y solo con nombre (`*`) para forzar APIs limpias en utilitarios de testing.

#### Regla de ámbito LEGB

- **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in.
- Las palabras clave `global` y `nonlocal` (mecanismo y riesgos en pruebas concurrentes).

#### Funciones de primer orden y Closures

- Pasar y retornar funciones como objetos.
- Closures: cómo una función interna retiene referencias a variables del ámbito envolvente en el atributo `__closure__`.
- Fábricas de funciones (*Function Factories*): creación dinámica de funciones de espera y localizadores configurables para Playwright.

#### Funciones Lambda y programación funcional

- Sintaxis y limitaciones de `lambda`.
- Uso de `sorted()` con claves personalizadas (`key=lambda x: ...`).
- Módulo `functools`: `partial` para precargar parámetros fijos en helpers de prueba.

> **Ejercicios Módulo 4:** 8 ejercicios prácticos sobre diseño de firmas estrictas, fábricas de funciones y scopes aislados.

---

### Módulo 5: Programación Orientada a Objetos (POO) Estricta para SDET

#### Fundamentos de Clases e Instancias

- La palabra clave `class`, el método constructor `__init__` y el parámetro explícito `self`.
- Variables de instancia vs. Variables de clase (trampa clásica de listas mutables compartidas entre tests).

#### Métodos Mágicos (Dunder Methods) esenciales

- Representación y depuración: `__repr__` (para desarrolladores/logs) vs. `__str__` (para usuarios).
- Comparación y hashing: `__eq__`, `__hash__` (hacer objetos custom comparables en assertions).
- Longitud y acceso por índice: `__len__`, `__getitem__`.

#### Encapsulamiento y Propiedades

- Convención de privacidad: prefijo simple `_protegido` vs. *Name Mangling* con doble prefijo `__privado`.
- Decorador `@property`, `@prop.setter` y `@prop.deleter` para validación de datos en tiempo de asignación.
- Decoradores `@classmethod` (constructores alternativos a partir de JSON/diccionarios) y `@staticmethod`.

#### Herencia y Polimorfismo

- Herencia simple y múltiple.
- La función `super()` y el MRO (*Method Resolution Order*) analizado mediante `Clase.__mro__`.
- Clases Base Abstractas (módulo `abc`, `ABC`, `@abstractmethod`) para definir interfaces formales.

#### POO Moderna en Python para Automatización

- `dataclasses`: decorador `@dataclass(slots=True, frozen=True)` para modelar datos de prueba inmutables y rápidos sin boilerplate.
- `typing.Protocol` (Duck Typing estricto / Tipado estructural): definir interfaces desacopladas sin obligar a heredar.
- **Caso práctico SDET:** Construcción de una clase base `BasePage` y `LoginPage` aplicando Page Object Model con tipado estricto.

#### Pilares de la POO y principios de diseño

- Los cuatro pilares: abstracción, encapsulamiento, herencia y polimorfismo.
- Composición, agregación y asociación vs. herencia ("es-un" vs. "tiene-un"); componentes reutilizables en el POM.
- Principios SOLID aplicados a un framework de pruebas (incluida una violación de Liskov y su corrección).

#### Polimorfismo avanzado y sobrecarga de operadores

- Sobrescritura de métodos, *duck typing*, `functools.singledispatch` y `singledispatchmethod`.
- Sobrecarga de operadores: `__add__`, `__radd__`, `__iadd__`, comparaciones ricas, `NotImplemented`, `__bool__`, `__contains__`, `__iter__`, `__call__`.

#### Decoradores aplicados a la POO

- Cómo funciona un decorador sobre un método; decorador `@step` tipado para Page Objects; orden de decoradores con `@property`, `@classmethod`, `@staticmethod` y `@abstractmethod`.
- Decoradores de la librería estándar: `@functools.cached_property`, `@functools.total_ordering`, `@typing.override`, `@typing.final`, `@enum.unique` y todas las opciones de `@dataclass` (`field`, `order`, `kw_only`, `__post_init__`, `replace`, `asdict`, `InitVar`).
- Decoradores de clase propios: registro de Page Objects y registro automático de pasos.

#### El modelo de objetos por dentro

- `__dict__`, `vars()`, `getattr`/`setattr`/`hasattr`/`delattr`, `__getattr__` vs. `__getattribute__`.
- Descriptores (`__get__`, `__set__`, `__set_name__`); `property` y los métodos como descriptores; validadores reutilizables.
- `__new__` vs. `__init__`, `__del__`, `__init_subclass__` y metaclases.

#### Enumeraciones y clases genéricas

- `Enum`, `IntEnum`, `StrEnum`, `auto()` y `match` sobre enumeraciones.
- Clases genéricas con `TypeVar` + `Generic[T]` y sintaxis PEP 695 (`class Repository[T]:`, Python 3.12+).

> **Ejercicios Módulo 5:** 15 ejercicios de diseño de arquitectura de clases, dataclasses de prueba, clases base para POM, composición y SOLID, sobrecarga de operadores, decoradores de método y de clase, descriptores y clases genéricas.

---

### Módulo 6: Manejo Integral de Excepciones y Gestores de Contexto (`with`)

#### Mecánica de excepciones en Python

- Qué es una excepción y cómo desenrolla la pila de llamadas (*Traceback*).
- Estructura completa: bloque `try` / `except` / `else` / `finally`.
- Propósito de `else` (código que solo se ejecuta si **no** hubo error) y `finally` (limpieza obligatoria: cerrar navegadores, liberar conexiones a bases de datos).

#### Jerarquía de excepciones y tipado

- Jerarquía nativa: por qué capturar `BaseException` es un antipatrón y por qué heredar de `Exception`.
- Captura múltiple de excepciones y alias con `as e`.
- Encadenamiento de excepciones con `raise NewError() from original_error` (preservación de causa raíz para depuración de fallos de prueba).

#### Diseño de Excepciones Personalizadas para SDET

- Creación de una jerarquía de errores para un framework de testing:

  ```text
  AutomationFrameworkError(Exception)
  ├── ElementNotFoundError(AutomationFrameworkError)
  ├── TestTimeoutError(AutomationFrameworkError)
  └── ApiContractMismatchError(AutomationFrameworkError)
  ```

- Agregar metadatos contextuales a la excepción (selector, tiempo transcurrido, payload recibido).

#### Gestores de Contexto (Context Managers) y la sentencia `with`

- El protocolo de contexto bajo el capó: métodos `__enter__` y `__exit__`.
- Tratamiento de excepciones dentro de `__exit__` (suprimir vs. propagar errores).
- Creación rápida de context managers con el módulo `contextlib` y el decorador `@contextmanager`.
- **Caso de uso SDET:** Medidor de tiempos de ejecución (`with Timer("login_step"):`) y gestor de sesiones de navegador con captura automática de screenshots al fallar.

> **Ejercicios Módulo 6:** 10 ejercicios de captura estricta, diseño de jerarquías de errores y creación de context managers de prueba.

---

### Módulo 7: Asincronía, Concurrencia y el Event Loop con `asyncio`

*Fundamental para el uso de Playwright Async API y pruebas de rendimiento de microservicios.*

#### Modelo de Asincronía vs. Multiprocesamiento/Hilos

- Concurrencia cooperativa frente a paralelismo real.
- Qué es el Event Loop de `asyncio` y cómo gestiona tareas sin bloquear el hilo principal de Python.

#### Sintaxis y conceptos base

- Definición de corrutinas con `async def` y suspensión con `await`.
- Objeto `Task` y creación con `asyncio.create_task()`.
- Estados de una corrutina y por qué invocar una función `async` sin `await` genera una advertencia de corrutina nunca esperada.

#### Orquestación de operaciones asíncronas

- `asyncio.gather()` para lanzar peticiones concurrentes y recopilar resultados.
- `asyncio.as_completed()` para procesar respuestas en el orden en que finalizan.
- Control de límites de tiempo: `asyncio.timeout()` (Python 3.11+) y `asyncio.wait_for()`.
- Iteradores asíncronos (`async for`) y gestores de contexto asíncronos (`async with`).

#### Integración conceptual con Playwright

- Comparación de arquitectura: Playwright Sync API (bloqueante) vs. Playwright Async API (`async_playwright`).
- Cómo evitar bloqueos en el loop asíncrono (evitar `time.sleep()` y utilizar `asyncio.sleep()`).

> **Ejercicios Módulo 7:** 10 ejercicios prácticos ejecutando peticiones concurrentes, pools de tareas asíncronas y timeouts con recuperación.

---

### Módulo 8: Metaprogramación, Decoradores y Generadores

#### Generadores e Iteradores

- Protocolo iterable (`__iter__` y `__next__`).
- Funciones generadoras con `yield`: procesamiento eficiente de grandes archivos de datos de prueba (CSV/JSONL) con uso constante de memoria *O(1)*.
- Métodos de generadores: `send()`, `close()`.

#### Decoradores en profundidad

- Anatomía de un decorador: funciones que envuelven funciones.
- Importancia crítica de `@functools.wraps(func)` para preservar el nombre `__name__` y la documentación `__doc__`.
- Decoradores sin argumentos vs. Decoradores con argumentos (fábricas de decoradores con 3 niveles de anidación).
- Decoradores de clases: transformar atributos y métodos automáticamente.

#### Decoradores esenciales para un SDET

- Implementación manual de un decorador `@retry(max_attempts=3, delay=1.0)` con reintento ante excepciones específicas.
- Decorador `@step_logger` para registrar el inicio, fin y duración de cada acción del Page Object Model.
- Decorador `@benchmark` para auditar tiempos de respuesta de endpoints.

> **Ejercicios Módulo 8:** 10 ejercicios diseñando generadores de datos sintéticos y decoradores avanzados de logging y reintentos.

---

### Módulo 9: Fundamentos del Ecosistema de Pruebas con `pytest`

#### Filosofía y Arquitectura de pytest

- Convenciones de descubrimiento de archivos, clases y funciones (`test_*.py`).
- La aserción nativa de Python (`assert expr`) y el sistema de introspección / reescritura de bytecode de pytest para mensajes de fallo detallados.

#### Sistema de Fixtures (El pilar de pytest)

- El decorador `@pytest.fixture`.
- Inyección de dependencias modular: fixtures que consumen otras fixtures.
- Ciclo de vida y scopes: `function`, `class`, `module`, `package`, `session`.
- Patrón Setup / Teardown mediante `yield` dentro de la fixture.
- Fixture flag `autouse=True` (cuándo usarlo y por qué evitarlo en exceso).
- Fixtures nativas útiles: `tmp_path`, `monkeypatch`, `capsys`.

#### Parametrización y Marcadores

- `@pytest.mark.parametrize`: pruebas basadas en datos (*Data-Driven Testing*) con combinaciones dinámicas.
- Marcadores estándar: `@pytest.mark.skip`, `@pytest.mark.skipif`, `@pytest.mark.xfail`.
- Marcadores personalizados (ej. `@pytest.mark.smoke`, `@pytest.mark.regression`) y configuración en `pytest.ini` para evitar advertencias.

#### Verificación de Excepciones y Logging

- Gestión de assertions de error con `with pytest.raises(ExpectedException) as exc_info:`.
- Configuración de logging capturado en consola durante la ejecución de pruebas.

> **Ejercicios Módulo 9:** 10 ejercicios completos modelando suites de pruebas, fixtures con teardown de limpieza y parametrizaciones exhaustivas.

---

### Módulo 10: Módulos, Paquetes, Archivos, Configuración y Logging

#### Módulos e imports

- Qué hace `import`: `sys.modules`, ejecución única del módulo, `sys.path` y *shadowing*.
- `import` vs. `from ... import`, alias, `__all__` y `if __name__ == "__main__":`.
- Imports circulares: por qué ocurren y cómo resolverlos (`TYPE_CHECKING`).

#### Paquetes

- `__init__.py`, paquetes regulares vs. *namespace packages*.
- Imports absolutos vs. relativos y `python -m paquete.modulo`.
- Diseño `src/` para un framework de pruebas e instalación editable.

#### Archivos y formatos de datos

- `pathlib.Path` en profundidad, codificación UTF-8 explícita, modos de `open()` y archivos grandes línea a línea.
- `shutil`, `tempfile` y carpeta de artefactos (screenshots, reportes).
- `json` (`dump`/`load`, `default=`, `object_hook=`) y `csv` (`DictReader`/`DictWriter`) para pruebas basadas en datos.

#### Configuración, fechas y logging

- Variables de entorno, configuración tipada validada, parser de `.env`, selección de entorno (dev/qa/staging) y enmascarado de secretos.
- `datetime` *naive* vs. *aware*, ISO 8601, `zoneinfo` y `time.monotonic()` para medir esperas.
- Módulo `logging`: jerarquía de loggers, handlers, formatters, niveles, propagación y `dictConfig`.

#### Depuración

- `breakpoint()`, comandos de `pdb`, *post-mortem* y `launch.json` de VS Code para pytest.

> **Ejercicios Módulo 10:** 10 ejercicios sobre organización de paquetes, lectura y escritura de datos de prueba, configuración por entorno, fechas y logging profesional.

---

### Módulo 11: Testing de APIs y Validación de Contratos

#### Fundamentos HTTP para SDET

- Anatomía de petición y respuesta, métodos e idempotencia, familias de códigos de estado, cabeceras, ruta, query y cuerpo.
- API falsa local con `http.server` para practicar sin depender de internet.

#### Clientes HTTP

- `requests`: verbos, `params`, `json=`, timeouts obligatorios, `raise_for_status`, `Session`, autenticación y reintentos con `HTTPAdapter` + `Retry`.
- `httpx`: `Client` y `AsyncClient`, `base_url`, *event hooks*, peticiones concurrentes con `asyncio.gather` y `MockTransport`.
- Playwright `APIRequestContext`: peticiones, `expect(response).to_be_ok()` y combinación API + UI (sembrar datos por API y verificarlos en la UI).

#### Tipado y validación de contratos

- `TypedDict` (`Required`/`NotRequired`), `Literal`, `NewType`, `Final`, `cast` vs. validación, `TypeGuard`/`TypeIs`.
- pydantic v2: `BaseModel`, `Field`, validadores, modo estricto, `extra="forbid"` para detectar cambios de contrato, serialización y JSON Schema.
- Integración con `ApiContractMismatchError` (Módulo 6).

#### Diseño y estrategia

- Patrón API Object (análogo al POM): cliente base, clientes por recurso y logs con secretos enmascarados.
- Casos positivos, negativos y de borde; idempotencia, paginación, presupuesto de latencia y limpieza de datos de prueba.

> **Ejercicios Módulo 11:** 10 ejercicios de clientes HTTP, validación de contratos con pydantic, API Objects y suites de API con pytest.

---

### Módulo 12: Mocking, pytest Avanzado y Framework Profesional con CI

#### Dobles de prueba y `unittest.mock`

- Dummy, stub, spy, mock y fake: cuándo usar cada uno.
- `Mock` vs. `MagicMock`, `return_value`, `side_effect`, aserciones de llamadas, `spec`/`autospec`/`create_autospec`.
- `patch` (decorador y gestor de contexto), regla "parchea donde se busca", `patch.object`, `patch.dict`, `AsyncMock`, `PropertyMock`; mock vs. `monkeypatch` y el antipatrón del exceso de mocks.

#### pytest avanzado

- Jerarquía de `conftest.py` y hooks: `pytest_addoption` (`--env`), `pytest_configure`, `pytest_collection_modifyitems`, `pytest_runtest_makereport`.
- Fábricas de fixtures, fixture `request` y parametrización indirecta.
- Configuración profesional en `pyproject.toml` (`addopts`, `markers`, `log_cli`, `xfail_strict`, `filterwarnings`).

#### Ejecución a escala, reportes y artefactos

- `pytest-xdist` (`-n auto`, estrategias de distribución, aislamiento entre workers) y `pytest-rerunfailures`.
- Taxonomía de causas de *flaky tests* y cómo corregirlas.
- JUnit XML, `pytest-html`, trazas, screenshots y videos de Playwright.

#### Framework profesional e integración continua

- Arquitectura completa de un framework (config, api, pages, components, utils; tests de api, ui y e2e) y *capstone* ejecutable que integra los módulos 0 a 11.
- GitHub Actions (matriz, `uv` con caché, smoke en cada PR y regresión nocturna, artefactos, secretos), equivalente en GitLab CI y `pre-commit`.

> **Ejercicios Módulo 12:** 10 ejercicios de mocking, hooks y fixtures avanzadas, ejecución en paralelo, reportes y configuración de CI.
