# JUSTIFICACIÓN DEL DISEÑO - BACKGAMMON

## 1. Resumen del Diseño General

Este proyecto implementa un juego completo de Backgammon en Python, siguiendo los principios SOLID y aplicando un diseño orientado a objetos modular y extensible. El sistema se estructura en tres capas principales:

### Arquitectura General
- **Capa de Dominio (`core/`)**: Contiene las entidades básicas del juego (Board, Dice, Player)
- **Capa de Lógica de Juego (`core/backgammon_game/`)**: Implementa las reglas y coordinación del juego
- **Capa de Presentación (`cli/` y `pygame_ui/`)**: Interfaces de usuario para interactuar con el juego

---

## 2. Justificación de las Clases Elegidas

### 2.1 Clases de Dominio (Core)

#### `Board`
**Responsabilidad**: Representa el estado físico del tablero de backgammon.
- **Por qué**: El tablero es una entidad fundamental del juego que mantiene las 24 posiciones, la barra y las fichas fuera del juego.
- **Justificación SOLID**: 
  - **SRP**: Solo maneja el estado del tablero y operaciones básicas de movimiento
  - **OCP**: Extensible para diferentes variantes de backgammon sin modificar código existente
  - **ISP**: Provee una interfaz clara con métodos específicos (`get_point`, `move_checker`, `can_bear_off`)

#### `Player`
**Responsabilidad**: Representa un jugador con su identidad (nombre y color).
- **Por qué**: Encapsula la información del jugador como una entidad independiente.
- **Justificación SOLID**:
  - **SRP**: Solo mantiene datos del jugador
  - **DIP**: No depende de implementaciones concretas, solo expone su interfaz

#### `Dice`
**Responsabilidad**: Maneja el lanzamiento y estado de los dados.
- **Por qué**: Aisla la lógica de aleatoriedad y reglas de dados (dobles).
- **Justificación SOLID**:
  - **SRP**: Única responsabilidad: generar valores aleatorios de dados
  - **OCP**: Puede extenderse para dados personalizados sin modificar el código existente

### 2.2 Clases de Lógica de Juego (backgammon_game/)

#### `BackgammonGame`
**Responsabilidad**: Coordinador central (Facade) que orquesta todas las operaciones del juego.
- **Por qué**: Proporciona una interfaz simplificada para la CLI y otras interfaces, ocultando la complejidad de las clases especializadas.
- **Justificación SOLID**:
  - **SRP**: Coordina componentes sin implementar lógica de negocio específica
  - **DIP**: Depende de abstracciones (clases especializadas) no de implementaciones concretas
  - **Facade Pattern**: Simplifica el uso del sistema complejo

#### `MoveValidator`
**Responsabilidad**: Valida la legalidad de los movimientos según las reglas de backgammon.
- **Por qué**: Separa la validación de las reglas de la ejecución de movimientos.
- **Justificación SOLID**:
  - **SRP**: Solo valida movimientos
  - **OCP**: Extensible para nuevas reglas sin modificar código existente
  - **LSP**: Puede sustituirse por validadores alternativos

#### `MoveCalculator`
**Responsabilidad**: Calcula posiciones destino basándose en dados y posición origen.
- **Por qué**: Separa la matemática del juego de la validación y ejecución.
- **Justificación SOLID**:
  - **SRP**: Solo calcula destinos
  - **OCP**: Extensible para diferentes lógicas de cálculo

#### `TurnManager`
**Responsabilidad**: Gestiona los turnos, cambios de jugador y dados disponibles.
- **Por qué**: Centraliza la lógica de gestión de turnos y movimientos restantes.
- **Justificación SOLID**:
  - **SRP**: Solo maneja turnos y movimientos disponibles
  - **ISP**: Interfaz específica para operaciones de turno

#### `GameStateManager`
**Responsabilidad**: Gestiona el estado del juego (ganador, game over).
- **Por qué**: Separa la lógica de fin de juego del resto del sistema.
- **Justificación SOLID**:
  - **SRP**: Solo determina estado del juego
  - **OCP**: Extensible para diferentes condiciones de victoria

### 2.3 Interfaz de Usuario

#### `CLI`
**Responsabilidad**: Proporciona interfaz de línea de comandos para jugar.
- **Por qué**: Separa la presentación de la lógica del juego.
- **Justificación SOLID**:
  - **SRP**: Solo maneja interacción con el usuario
  - **DIP**: Depende de `BackgammonGame` (abstracción), no de implementaciones

---

## 3. Justificación de Atributos

### Convención de Nombres
- **Atributos privados**: Se utiliza el prefijo y sufijo `__attribute__` (name mangling) para proteger atributos internos y evitar accesos no controlados.
- **Propiedades**: Se usan `@property` para exponer atributos de forma controlada cuando es necesario.

### Board
```python
self.__points__      # Lista de 24 posiciones, cada una con [color, count]
self.__bar__         # Diccionario {"white": count, "black": count} - fichas capturadas
self.__off__         # Diccionario {"white": count, "black": count} - fichas sacadas
```
**Justificación**: 
- `__points__`: Lista porque las posiciones tienen orden secuencial (1-24)
- `__bar__` y `__off__`: Diccionarios para acceso directo por color
- Privados para controlar modificaciones y mantener consistencia

### Player
```python
self.__name__        # Nombre del jugador
self.__color__       # Color asignado ("white" o "black")
```
**Justificación**: Inmutables después de la creación para mantener identidad del jugador.

### Dice
```python
self.__values__      # Lista con los dos valores de dados [value1, value2]
```
**Justificación**: Lista para mantener ambos dados juntos, facilitando operaciones como detección de dobles.

### BackgammonGame
```python
self.__board__           # Instancia de Board
self.__dice__            # Instancia de Dice
self.__player1__         # Instancia de Player
self.__player2__         # Instancia de Player
self.__validator__       # Instancia de MoveValidator
self.__calculator__      # Instancia de MoveCalculator
self.__turn_manager__    # Instancia de TurnManager
self.__state_manager__   # Instancia de GameStateManager
```
**Justificación**: Composición de objetos especializados siguiendo el principio de **Dependency Injection** y **Single Responsibility**.

---

## 4. Decisiones de Diseño Relevantes

### 4.1 Separación de Validación y Ejecución
- **Decisión**: `MoveValidator` valida, `Board.move_checker()` ejecuta.
- **Ventaja**: Permite validar sin modificar estado, facilita testing y extensibilidad.

### 4.2 Cálculo de Destinos Separado
- **Decisión**: `MoveCalculator` calcula destinos independientemente de validación.
- **Ventaja**: Permite reutilizar cálculos en diferentes contextos (UI, IA futura).

### 4.3 Coordinador Central (Facade)
- **Decisión**: `BackgammonGame` como punto único de entrada.
- **Ventaja**: Simplifica uso del sistema, oculta complejidad interna.

### 4.4 Inmutabilidad de Jugadores
- **Decisión**: Los atributos de `Player` no se modifican después de la creación.
- **Ventaja**: Evita bugs relacionados con cambios de identidad durante el juego.

### 4.5 Representación del Tablero
- **Decisión**: Posiciones como `[color, count]` en lugar de objetos `Checker`.
- **Evolución**: Inicialmente existía clase `Checker` (ver CHANGELOG v0.0.18), se eliminó por simplicidad.
- **Ventaja**: Reduce complejidad, facilita operaciones sobre el tablero.

### 4.6 Gestión de Movimientos Forzados
- **Decisión**: `TurnManager.get_forced_moves()` determina qué dados usar según reglas.
- **Ventaja**: Centraliza lógica compleja de reglas de backgammon (usar dado mayor, fichas en barra).

### 4.7 Encapsulación con Name Mangling
- **Decisión**: Uso de `__attribute__` en lugar de `_attribute`.
- **Ventaja**: Mayor protección contra accesos accidentales, claridad en la intención de privacidad.

---

## 5. Excepciones y Manejo de Errores

### Estrategia Actual
El proyecto **no define excepciones personalizadas** actualmente. El manejo de errores se realiza mediante:

#### 5.1 Validaciones Previas
- `MoveValidator.is_valid_move()` retorna `True/False` antes de ejecutar
- `BackgammonGame.make_move()` retorna `True/False` indicando éxito/fallo
- La CLI captura `ValueError` y `KeyboardInterrupt` para entradas inválidas

#### 5.2 Justificación
- **Por qué no excepciones personalizadas**: 
  - El flujo del juego se maneja con validaciones booleanas
  - Los errores esperados (movimiento inválido) no son excepcionales, son parte del flujo normal
  - Simplifica el código para un juego interactivo

#### 5.3 Mejoras Futuras
Se podría implementar:
```python
class InvalidMoveError(Exception): pass
class GameOverError(Exception): pass
class InvalidPositionError(Exception): pass
```
Para contextos donde sea necesario distinguir tipos de errores (ej: IA, log detallado).

---

## 6. Estrategias de Testing y Cobertura

### 6.1 Enfoque de Testing

#### Cobertura Alcanzada: 94% (según coverage report)
#### Calidad de Código: 9.10/10 (según Pylint)

El proyecto implementa testing exhaustivo con **unittest**, cubriendo:

### 6.2 Tests por Componente

#### Board (test_board.py)
- **Inicialización y posiciones iniciales**: Verifica configuración correcta del tablero
- **Movimientos básicos**: `test_move_checker_normal`, `test_move_checker_to_occupied_same_color`
- **Capturas**: `test_move_checker_capture`
- **Movimientos desde barra**: `test_move_checker_from_bar`
- **Bear off**: `test_move_checker_bear_off`, `test_bear_off_checker_success`
- **Validaciones**: `test_is_move_valid_out_of_bounds`, `test_is_move_valid_wrong_color`
- **Estado del juego**: `test_is_winner_white_wins`, `test_has_checkers_on_bar_with_checkers`

**Por qué**: Board es el componente más crítico, necesita testing exhaustivo de todas las operaciones.

#### Player (test_player.py)
- **Inicialización**: `test_player_initialization`, `test_player_with_different_colors`
- **Inmutabilidad**: `test_player_immutability`
- **Métodos de acceso**: `test_player_get_methods`

**Por qué**: Verifica que los jugadores mantienen consistencia e inmutabilidad.

#### Dice (test_dice.py)
- **Lanzamiento**: `test_rolls_return_values`, `test_roll_values_in_range`
- **Detección de dobles**: `test_is_double_detection`
- **Múltiples lanzamientos**: `test_multiple_rolls_change_values`

**Por qué**: Dado el componente aleatorio, se verifica el rango y comportamiento esperado.

#### MoveValidator (test_move_validator.py)
- **Validaciones de origen**: `test_invalid_move_empty_source`, `test_invalid_move_wrong_color`
- **Validaciones de destino**: `test_destination_blocked_by_enemy`, `test_destination_with_single_enemy`
- **Movimientos desde barra**: `test_must_enter_from_bar_with_checkers`
- **Bear off**: `test_bearing_off_destination`

**Por qué**: La validación es crítica para la integridad del juego.

#### MoveCalculator (test_move_calculator.py)
- **Cálculos normales**: `test_calculate_white_normal_move`, `test_calculate_black_normal_move`
- **Bear off**: `test_calculate_white_bearing_off`, `test_can_bear_off_higher_white`
- **Desde barra**: `test_calculate_from_bar_white`, `test_calculate_from_bar_black`
- **Casos borde**: `test_edge_cases`

**Por qué**: Los cálculos incorrectos romperían la lógica del juego.

#### TurnManager (test_turn_manager.py)
- **Gestión de turnos**: `test_switch_player`, `test_initial_current_player`
- **Movimientos**: `test_set_moves_from_dice_normal`, `test_set_moves_from_dice_double`
- **Movimientos forzados**: `test_forced_moves_from_bar`, `test_forced_moves_prefer_larger_die`
- **Estado del turno**: `test_is_turn_complete`, `test_use_move_valid`

**Por qué**: La gestión de turnos es compleja y requiere cobertura exhaustiva.

#### GameStateManager (test_game_state_manager.py)
- **Estado inicial**: `test_manager_initialization`
- **Detección de ganador**: Tests de victoria y game over

**Por qué**: Asegura que el fin del juego se detecta correctamente.

#### BackgammonGame (test_backgammongame.py)
- **Inicialización**: `test_game_initialization`, `test_custom_player_names`
- **Flujo de juego**: `test_roll_dice`, `test_make_move_with_dice`
- **Integración**: `test_has_valid_moves_initial_position`

**Por qué**: Tests de integración que verifican coordinación entre componentes.

#### CLI (test_cli.py)
- **Inicialización**: `test_cli_inicialization`, `test_cli_exists`
- **Integración**: `test_cli_game_integration`

**Por qué**: Verifica que la interfaz se integra correctamente con el juego.

### 6.3 Configuración de Coverage

Archivo `.coveragerc`:
```ini
[run]
omit =
    tests/*           # Excluye los propios tests
    */__pycache__/*   # Excluye archivos compilados
    assets/*          # Excluye recursos
    */cli.py          # CLI requiere interacción manual
    */pygame_ui/*     # UI gráfica requiere testing manual

[report]
exclude_lines =
    pragma: no cover
    if __name__ == .__main__.:  # Excluye bloques de ejecución directa
```

### 6.4 Estrategia de Testing
1. **Unit Tests**: Cada clase se testea independientemente
2. **Integration Tests**: BackgammonGame y CLI verifican coordinación
3. **Edge Cases**: Se prueban casos límite (posiciones extremas, bear off con dados mayores)
4. **Mock Objects**: Se usan instancias reales pero con setUp controlado

### 6.5 Por Qué Esta Cobertura
- **94% de coverage** para el proyecto del juego
- El 6% restante incluye:
  - Código de UI interactiva (pygame, CLI con input del usuario)
  - Líneas específicas de coordinación en `BackgammonGame` (87% coverage)
  - Algunas líneas en `MoveCalculator` (84% coverage)
  - Bloques `if __name__ == "__main__"`

**Desglose por archivo (coverage actual)**:
- `player.py`: 100%
- `dice.py`: 100%
- `board.py`: 100%
- `turn_manager.py`: 100%
- `move_validator.py`: 100%
- `game_state_manager.py`: 100%
- `move_calculator.py`: 84% (9 líneas sin cubrir en lógica compleja de bear-off)
- `backgammongame.py`: 87% (13 líneas sin cubrir en coordinación)

---

## 7. Cumplimiento de Principios SOLID

**El código cumple completamente con todos los principios SOLID**, como se demuestra a continuación:

### 7.1 Single Responsibility Principle (SRP)
**CUMPLIDO - Cada clase tiene una única razón para cambiar**:
- `Board`: Solo cambia si cambian las reglas del tablero
- `MoveValidator`: Solo cambia si cambian las reglas de validación
- `MoveCalculator`: Solo cambia si cambia la matemática de movimientos
- `TurnManager`: Solo cambia si cambian las reglas de turnos
- `GameStateManager`: Solo cambia si cambian las condiciones de victoria

**Ejemplo claro**: Inicialmente había clase `Checker`, se eliminó porque violaba SRP al duplicar responsabilidades de `Board`.

### 7.2 Open/Closed Principle (OCP)
**CUMPLIDO - Abierto para extensión, cerrado para modificación**:
- `MoveValidator` puede extenderse para nuevas reglas sin modificar código existente
- `BackgammonGame` puede usar diferentes implementaciones de validadores/calculadores
- `Dice` puede extenderse para dados especiales (dados cargados para IA, etc.)

**Ejemplo**: Agregar variante "Nackgammon" requeriría:
```python
class NackgammonBoard(Board):
    def _setup_initial_position(self):
        # Nueva configuración inicial
```
Sin modificar `Board` original.

### 7.3 Liskov Substitution Principle (LSP)
**CUMPLIDO - Subtipos deben ser sustituibles por sus tipos base**:
- Cualquier implementación de validador puede sustituir a `MoveValidator` sin romper `BackgammonGame`
- `Player` puede extenderse (ej: `AIPlayer`) sin afectar el juego

**Diseño**: Las clases usan composición más que herencia, minimizando violaciones de LSP.

### 7.4 Interface Segregation Principle (ISP)
**CUMPLIDO - Interfaces específicas mejor que una interfaz general**:
- `Board` no expone métodos innecesarios, solo los requeridos
- `MoveValidator` tiene interfaz mínima: `is_valid_move()`, `must_enter_from_bar()`
- `TurnManager` solo expone métodos relacionados con turnos

**Ejemplo**: CLI solo usa métodos públicos de `BackgammonGame`, no accede directamente a componentes internos.

### 7.5 Dependency Inversion Principle (DIP)
**CUMPLIDO - Depender de abstracciones, no de concreciones**:
- `BackgammonGame` depende de instancias de clases, pero no de implementaciones específicas
- `MoveValidator` recibe `Board` como dependencia (inyección)
- CLI depende de `BackgammonGame` (abstracción), no de componentes internos

**Ejemplo**:
```python
def __init__(self, board):  # Recibe board, no lo crea internamente
    self.__board__ = board
```

---

## 8. Evolución del Diseño (CHANGELOG)

### Decisiones Clave Documentadas:

#### v0.0.18 - Eliminación de Clase Checker
- **Antes**: Clase `Checker` con estado (color, estado: tablero/barra/fuera)
- **Después**: Representación simple `[color, count]` en Board
- **Razón**: Simplicidad, eliminación de responsabilidades duplicadas

#### v0.0.21-0.0.25 - Especialización de Clases
- Creación de `MoveValidator`, `MoveCalculator`, `TurnManager`, `GameStateManager`
- **Razón**: Separar responsabilidades para cumplir SRP

#### v0.0.32 - Interfaz Pygame
- Agregada sin modificar lógica del juego
- **Razón**: Demuestra OCP - nueva UI sin cambiar core

---