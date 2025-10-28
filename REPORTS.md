# Automated Reports
## Coverage Report
```text
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
cli/cli.py                                      70     15    79%   39, 43, 56-64, 70-72, 76-77
core/backgammon_game/backgammongame.py          98     16    84%   33, 40-43, 47, 77-82, 89-90, 93, 101, 103
core/backgammon_game/game_state_manager.py      18      0   100%
core/backgammon_game/move_calculator.py         57      9    84%   39-41, 46, 60-62, 68, 72
core/backgammon_game/move_validator.py          27      0   100%
core/backgammon_game/turn_manager.py            40      0   100%
core/board.py                                  107      0   100%
core/dice.py                                    15      0   100%
core/player.py                                   8      0   100%
--------------------------------------------------------------------------
TOTAL                                          440     40    91%

```
## Pylint Report
```text
************* Module board
core/board.py:124:0: C0304: Final newline missing (missing-final-newline)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:65:12: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
core/board.py:97:12: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
core/board.py:105:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/board.py:118:4: C0104: Disallowed name "bar" (disallowed-name)
************* Module player
core/player.py:12:0: C0304: Final newline missing (missing-final-newline)
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module dice
core/dice.py:21:0: C0304: Final newline missing (missing-final-newline)
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon_game.turn_manager
core/backgammon_game/turn_manager.py:36:20: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game/turn_manager.py:39:0: C0301: Line too long (119/100) (line-too-long)
core/backgammon_game/turn_manager.py:52:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/turn_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon_game/turn_manager.py:21:47: W0613: Unused argument 'board' (unused-argument)
************* Module backgammon_game.move_validator
core/backgammon_game/move_validator.py:33:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/move_validator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon_game.backgammongame
core/backgammon_game/backgammongame.py:31:0: C0301: Line too long (104/100) (line-too-long)
core/backgammon_game/backgammongame.py:36:0: C0301: Line too long (112/100) (line-too-long)
core/backgammon_game/backgammongame.py:89:0: C0301: Line too long (119/100) (line-too-long)
core/backgammon_game/backgammongame.py:98:0: C0301: Line too long (104/100) (line-too-long)
core/backgammon_game/backgammongame.py:117:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/backgammongame.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon_game/backgammongame.py:1:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)
core/backgammon_game/backgammongame.py:2:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)
core/backgammon_game/backgammongame.py:3:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)
core/backgammon_game/backgammongame.py:8:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
core/backgammon_game/backgammongame.py:75:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
************* Module backgammon_game.move_calculator
core/backgammon_game/move_calculator.py:21:46: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game/move_calculator.py:73:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/move_calculator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon_game/move_calculator.py:10:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game/move_calculator.py:16:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game/move_calculator.py:47:16: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
core/backgammon_game/move_calculator.py:47:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game/move_calculator.py:69:16: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
core/backgammon_game/move_calculator.py:69:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game/move_calculator.py:22:4: R0911: Too many return statements (11/6) (too-many-return-statements)
core/backgammon_game/move_calculator.py:22:4: R0912: Too many branches (19/12) (too-many-branches)
************* Module backgammon_game.game_state_manager
core/backgammon_game/game_state_manager.py:24:0: C0304: Final newline missing (missing-final-newline)
core/backgammon_game/game_state_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module tests.test_cli
tests/test_cli.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_cli.py:5:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_cli.py:14:36: W0613: Unused argument 'input_mock' (unused-argument)
tests/test_cli.py:14:48: W0613: Unused argument 'print_mock' (unused-argument)
tests/test_cli.py:24:39: W0613: Unused argument 'input_mock' (unused-argument)
tests/test_cli.py:24:51: W0613: Unused argument 'print_mock' (unused-argument)
tests/test_cli.py:32:40: W0613: Unused argument 'print_mock' (unused-argument)
tests/test_cli.py:45:34: W0613: Unused argument 'print_mock' (unused-argument)
tests/test_cli.py:55:44: W0613: Unused argument 'input_mock' (unused-argument)
tests/test_cli.py:55:56: W0613: Unused argument 'print_mock' (unused-argument)
tests/test_cli.py:72:41: W0613: Unused argument 'input_mock' (unused-argument)
tests/test_cli.py:72:53: W0613: Unused argument 'print_mock' (unused-argument)
tests/test_cli.py:92:43: W0613: Unused argument 'input_mock' (unused-argument)
tests/test_cli.py:92:55: W0613: Unused argument 'print_mock' (unused-argument)
************* Module tests.test_move_validator
tests/test_move_validator.py:67:43: C0303: Trailing whitespace (trailing-whitespace)
tests/test_move_validator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_move_validator.py:4:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_player
tests/test_player.py:46:0: C0304: Final newline missing (missing-final-newline)
tests/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_player.py:3:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_game_state_manager
tests/test_game_state_manager.py:76:0: C0304: Final newline missing (missing-final-newline)
tests/test_game_state_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_game_state_manager.py:5:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_dice
tests/test_dice.py:8:37: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:18:28: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:27:45: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:43:0: C0301: Line too long (103/100) (line-too-long)
tests/test_dice.py:54:0: C0304: Final newline missing (missing-final-newline)
tests/test_dice.py:54:0: C0301: Line too long (104/100) (line-too-long)
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:3:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_backgammongame
tests/test_backgammongame.py:143:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_backgammongame.py:148:0: C0304: Final newline missing (missing-final-newline)
tests/test_backgammongame.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_backgammongame.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_backgammongame.py:37:8: W0612: Unused variable 'values' (unused-variable)
tests/test_backgammongame.py:100:12: W0702: No exception type(s) specified (bare-except)
tests/test_backgammongame.py:105:17: W0212: Access to a protected member _is_legal_move of a client class (protected-access)
tests/test_backgammongame.py:130:8: W0702: No exception type(s) specified (bare-except)
tests/test_backgammongame.py:4:0: R0904: Too many public methods (24/20) (too-many-public-methods)
************* Module tests.test_move_calculator
tests/test_move_calculator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_move_calculator.py:4:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_turn_manager
tests/test_turn_manager.py:6:41: C0303: Trailing whitespace (trailing-whitespace)
tests/test_turn_manager.py:117:25: C0303: Trailing whitespace (trailing-whitespace)
tests/test_turn_manager.py:146:0: C0304: Final newline missing (missing-final-newline)
tests/test_turn_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_turn_manager.py:6:0: C0115: Missing class docstring (missing-class-docstring)
************* Module tests.test_board
tests/test_board.py:210:0: C0304: Final newline missing (missing-final-newline)
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:167:19: W0718: Catching too general exception Exception (broad-exception-caught)
tests/test_board.py:178:19: W0718: Catching too general exception Exception (broad-exception-caught)
tests/test_board.py:187:19: W0718: Catching too general exception Exception (broad-exception-caught)
tests/test_board.py:4:0: R0904: Too many public methods (28/20) (too-many-public-methods)

-----------------------------------
Your code has been rated at 9.08/10


```
