# Automated Reports
## Coverage Report
```text
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
core/backgammon_game/backgammongame.py         122     34    72%   33, 36-37, 39, 51-68, 72, 94, 102-107, 114-115, 118, 126, 128
core/backgammon_game/game_state_manager.py      18      0   100%
core/backgammon_game/move_calculator.py         37     14    62%   28-33, 38-45
core/backgammon_game/move_validator.py          27      1    96%   29
core/backgammon_game/turn_manager.py           110     50    55%   27-35, 42-50, 55-57, 69-73, 75-77, 85, 88, 91-114
core/board.py                                  107      2    98%   80, 82
core/dice.py                                    15      0   100%
core/player.py                                   8      0   100%
--------------------------------------------------------------------------
TOTAL                                          444    101    77%

```
## Pylint Report
```text
************* Module dice
core/dice.py:21:0: C0304: Final newline missing (missing-final-newline)
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module player
core/player.py:12:0: C0304: Final newline missing (missing-final-newline)
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module board
core/board.py:76:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:86:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:65:12: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
core/board.py:99:12: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
core/board.py:107:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/board.py:120:4: C0104: Disallowed name "bar" (disallowed-name)
************* Module backgammon_game.move_validator
core/backgammon_game/move_validator.py:33:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/move_validator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon_game.game_state_manager
core/backgammon_game/game_state_manager.py:24:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/game_state_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon_game.turn_manager
core/backgammon_game/turn_manager.py:39:0: C0301: Line too long (105/100) (line-too-long)
core/backgammon_game/turn_manager.py:41:28: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game/turn_manager.py:42:0: C0301: Line too long (102/100) (line-too-long)
core/backgammon_game/turn_manager.py:43:0: C0301: Line too long (104/100) (line-too-long)
core/backgammon_game/turn_manager.py:48:32: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game/turn_manager.py:50:20: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game/turn_manager.py:54:23: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game/turn_manager.py:80:0: C0301: Line too long (112/100) (line-too-long)
core/backgammon_game/turn_manager.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game/turn_manager.py:117:0: C0301: Line too long (119/100) (line-too-long)
core/backgammon_game/turn_manager.py:130:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/turn_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon_game/turn_manager.py:44:12: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/backgammon_game/turn_manager.py:21:4: R0911: Too many return statements (7/6) (too-many-return-statements)
core/backgammon_game/turn_manager.py:51:4: R0913: Too many arguments (6/5) (too-many-arguments)
core/backgammon_game/turn_manager.py:51:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
core/backgammon_game/turn_manager.py:58:4: R0912: Too many branches (13/12) (too-many-branches)
core/backgammon_game/turn_manager.py:58:47: W0613: Unused argument 'game_validator' (unused-argument)
************* Module backgammon_game.backgammongame
core/backgammon_game/backgammongame.py:31:0: C0301: Line too long (104/100) (line-too-long)
core/backgammon_game/backgammongame.py:36:0: C0301: Line too long (112/100) (line-too-long)
core/backgammon_game/backgammongame.py:56:0: C0301: Line too long (113/100) (line-too-long)
core/backgammon_game/backgammongame.py:114:0: C0301: Line too long (119/100) (line-too-long)
core/backgammon_game/backgammongame.py:123:0: C0301: Line too long (104/100) (line-too-long)
core/backgammon_game/backgammongame.py:142:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/backgammongame.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon_game/backgammongame.py:1:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)
core/backgammon_game/backgammongame.py:2:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)
core/backgammon_game/backgammongame.py:3:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)
core/backgammon_game/backgammongame.py:8:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
core/backgammon_game/backgammongame.py:100:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
************* Module backgammon_game.move_calculator
core/backgammon_game/move_calculator.py:45:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/move_calculator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon_game/move_calculator.py:10:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game/move_calculator.py:16:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game/move_calculator.py:22:4: R0911: Too many return statements (7/6) (too-many-return-statements)
************* Module tests.test_move_calculator
tests/test_move_calculator.py:22:36: C0303: Trailing whitespace (trailing-whitespace)
tests/test_move_calculator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_move_calculator.py:4:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_turn_manager
tests/test_turn_manager.py:6:41: C0303: Trailing whitespace (trailing-whitespace)
tests/test_turn_manager.py:117:25: C0303: Trailing whitespace (trailing-whitespace)
tests/test_turn_manager.py:121:0: C0304: Final newline missing (missing-final-newline)
tests/test_turn_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_turn_manager.py:6:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_player
tests/test_player.py:46:0: C0304: Final newline missing (missing-final-newline)
tests/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_player.py:3:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_backgammongame
tests/test_backgammongame.py:98:0: C0304: Final newline missing (missing-final-newline)
tests/test_backgammongame.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_backgammongame.py:3:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_backgammongame.py:36:8: W0612: Unused variable 'values' (unused-variable)
************* Module tests.test_board
tests/test_board.py:193:0: C0304: Final newline missing (missing-final-newline)
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:3:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:162:8: C0415: Import outside toplevel (io) (import-outside-toplevel)
tests/test_board.py:163:8: C0415: Import outside toplevel (sys) (import-outside-toplevel)
tests/test_board.py:169:15: W0718: Catching too general exception Exception (broad-exception-caught)
tests/test_board.py:3:0: R0904: Too many public methods (26/20) (too-many-public-methods)
************* Module tests.test_dice
tests/test_dice.py:8:37: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:18:28: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:27:45: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:43:0: C0301: Line too long (103/100) (line-too-long)
tests/test_dice.py:54:0: C0304: Final newline missing (missing-final-newline)
tests/test_dice.py:54:0: C0301: Line too long (104/100) (line-too-long)
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:3:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_game_state_manager
tests/test_game_state_manager.py:76:0: C0304: Final newline missing (missing-final-newline)
tests/test_game_state_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_game_state_manager.py:5:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_move_validator
tests/test_move_validator.py:56:0: C0304: Final newline missing (missing-final-newline)
tests/test_move_validator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_move_validator.py:4:0: C0115: Missing class docstring (missing-class-docstring)

-----------------------------------
Your code has been rated at 9.06/10


```
