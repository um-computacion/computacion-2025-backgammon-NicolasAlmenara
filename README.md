# Backgammon - Proyecto Final

Implementación completa del juego de Backgammon en Python siguiendo los principios SOLID.

## Descripción

Este proyecto implementa un juego funcional de Backgammon con:
- Lógica completa de reglas del juego
- Interfaz de línea de comandos (CLI)
- Interfaz gráfica con Pygame
- Testing exhaustivo con 94% de cobertura
- Diseño modular siguiendo principios SOLID

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/um-computacion/computacion-2025-backgammon-NicolasAlmenara.git
cd computacion-2025-backgammon-NicolasAlmenara
```

### 2. Crear Entorno Virtual (Recomendado)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

## Modo Juego

### Opción 1: Jugar con Interfaz CLI (Línea de Comandos)

La interfaz CLI permite jugar directamente desde la terminal con una representación visual del tablero en texto.

**Ejecutar:**
```bash
python -m cli.cli
```

**Cómo jugar:**
1. Ingresa los nombres de los jugadores cuando se solicite
2. El juego lanza los dados automáticamente en cada turno
3. Se muestra el tablero y los dados disponibles
4. Ingresa:
   - Posición origen (1-24) o 25 para fichas en la barra
   - Dado a usar
5. El juego valida automáticamente los movimientos según las reglas
6. Gana el primer jugador en sacar todas sus 15 fichas

**Opciones durante el juego:**
- `1`: Realizar un movimiento
- `2`: Salir del juego

**Ejemplo de tablero CLI:**
```
======================================================================
                    TABLERO DE BACKGAMMON
======================================================================
    13  14  15  16  17  18  19  20  21  22  23  24 
    B5   .   .  W3   .  W5   .   .   .   .   .  B2 
   ------------------------------------------------
BARRA:                  vacía                      
   ------------------------------------------------
    W5   .   .  B3   .  B5   .   .   .   .   .  W2 
    12  11  10   9   8   7   6   5   4   3   2   1 

        FUERA - Blancas: 0  |  Negras: 0         
======================================================================
```

### Opción 2: Jugar con Interfaz Pygame (Gráfica)

La interfaz gráfica proporciona una experiencia visual completa con tablero dibujado, fichas de colores y controles con mouse.

**Ejecutar:**
```bash
python pygame_ui\backgammon_pygame.py
```

**Controles:**
- Click izquierdo: Seleccionar ficha o posición destino.
- Con espacio lanzamos los dados.
- El tablero se actualiza visualmente en tiempo real.

---

## Modo Testing

### Ejecutar Todos los Tests

```bash
python -m unittest discover tests
```

### Ejecutar Tests de un Módulo Específico

**Board:**
```bash
python -m unittest tests.test_board
```

**Dice:**
```bash
python -m unittest tests.test_dice
```

**Player:**
```bash
python -m unittest tests.test_player
```

**MoveValidator:**
```bash
python -m unittest tests.test_move_validator
```

**MoveCalculator:**
```bash
python -m unittest tests.test_move_calculator
```

**TurnManager:**
```bash
python -m unittest tests.test_turn_manager
```

**GameStateManager:**
```bash
python -m unittest tests.test_game_state_manager
```

**BackgammonGame:**
```bash
python -m unittest tests.test_backgammongame
```

**CLI:**
```bash
python -m unittest tests.test_cli
```

### Testing con Cobertura

#### Ejecutar Tests con Coverage

```bash
python -m coverage run -m unittest; python -m coverage report -m; python -m coverage xml
```

#### Ver Reporte de Cobertura en Terminal

```bash
python -m coverage report -m
```

**Salida esperada:**
```
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
core\backgammon_game\backgammongame.py            98     13    87%   33, 39, 47, ...
core\backgammon_game\game_state_manager.py        18      0   100%
core\backgammon_game\move_calculator.py           57      9    84%   39-41, 46, ...
core\backgammon_game\move_validator.py            27      0   100%
core\backgammon_game\turn_manager.py              40      0   100%
core\board.py                                    107      0   100%
core\dice.py                                      15      0   100%
core\player.py                                     8      0   100%
----------------------------------------------------------------------------
TOTAL                                            370     22    94%
```

### Configuración de Coverage

El archivo `.coveragerc` está configurado para excluir:
- Tests (no se miden a sí mismos)
- Archivos de cache (`__pycache__`)
- Assets y recursos
- CLI y UI (requieren interacción manual)

---

## Estructura del Proyecto

```
proyecto/
├── core/                           # Lógica del juego
│   ├── board.py                   # Tablero y estado
│   ├── dice.py                    # Dados
│   ├── player.py                  # Jugadores
│   └── backgammon_game/           # Lógica avanzada
│       ├── backgammongame.py      # Coordinador principal
│       ├── move_validator.py      # Validación de reglas
│       ├── move_calculator.py     # Cálculo de movimientos
│       ├── turn_manager.py        # Gestión de turnos
│       └── game_state_manager.py  # Estado del juego
├── cli/                           # Interfaz de línea de comandos
│   └── cli.py
├── pygame_ui/                     # Interfaz gráfica
│   └── __init__.py
├── tests/                         # Suite de tests
│   ├── test_board.py
│   ├── test_dice.py
│   ├── test_player.py
│   ├── test_move_validator.py
│   ├── test_move_calculator.py
│   ├── test_turn_manager.py
│   ├── test_game_state_manager.py
│   ├── test_backgammongame.py
│   └── test_cli.py
├── .coveragerc                    # Configuración de coverage
├── requirements.txt               # Dependencias
├── CHANGELOG.md                   # Historial de cambios
├── JUSTIFICACION.md              # Diseño y principios SOLID
└── README.md                      # Este archivo
```

---

## Reglas del Backgammon Implementadas

### Movimientos Básicos
- Las fichas blancas se mueven de 1 a 24
- Las fichas negras se mueven de 24 a 1
- Se mueve según el valor de los dados

### Reglas Especiales
- **Dados dobles**: Si ambos dados son iguales, se juegan 4 movimientos
- **Barra**: Fichas capturadas deben entrar antes de mover otras
- **Bear off**: Sacar fichas cuando todas están en el home (últimos 6 puntos)
- **Bear off con dado mayor**: Si no hay ficha exacta, se puede sacar desde la más alta
- **Bloqueo**: No se puede mover a un punto con 2+ fichas enemigas
- **Captura**: Se puede capturar una ficha enemiga solitaria

### Condición de Victoria
El primer jugador en sacar todas sus 15 fichas del tablero gana.


---

## Autor

**Nicolas Almenara**  
Computación 2025  
Universidad de Mendoza

---

## Documentación Adicional

- **JUSTIFICACION.md**: Diseño detallado, principios SOLID y decisiones técnicas
- **CHANGELOG.md**: Historial completo de cambios y versiones
- **prompts-desarrollo.md**: Prompts de IA utilizados en el desarrollo
- **prompts-testing.md**: Prompts de IA utilizados para testing
- **prompts-documentacion.md**: Prompts de IA para documentación
