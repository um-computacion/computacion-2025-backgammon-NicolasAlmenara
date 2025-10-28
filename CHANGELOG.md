# Changelog
Todos los cambios importantes de este proyecto se documentarán en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
## [0.0.35] - 2024-10-28
### Added
- Se agrega documentacion.
### Fixed
- Se arregla los test, para que no impriman el board cuando se ejecutan.

## [0.0.34] - 2024-10-23
### Added
- Se agrega el diagrama de clases.

## [0.0.33] - 2024-10-22
### Added
- Se agrega documentacion.

## [0.0.32] - 2024-10-21
### Changed
- Se modifican reglas del final de partida, actualización de MoveCalculator y sus tests.
### Added
- Se agrega interfaz visual utilizando pygame.

## [0.0.31] - 2024-10-20
### Added
- Se agregan tests avanzados de juego y CLI, opción de terminar el juego, y corrección de bugs.

## [0.0.30] - 2024-10-19
### Added
- Se agregan tests CLI: test_cli_inicialization, test_cli_can_create_game, test_cli_game_integration, test_cli_exists, test_show_board_with_bar_checkers, test_show_board_empty_bar, test_destination_blocked_by_enemy, test_destination_with_single_enemy.

## [0.0.29] - 2024-10-18
### Added
- Se agrega interfaz por consola (play_turn).

## [0.0.28] - 2024-10-17
### Added
- Se agregan métodos start y play_game en la clase CLI.

## [0.0.27] - 2024-10-16
### Added
- Se agregan tests: test_get_forced_move_message_initial, test_reset_game, test_make_compound_move_without_dice, test_game_state_consistency.

## [0.0.26] - 2024-10-15
### Added
- Se agregan tests del juego: test_game_initialization, test_default_player_names, test_custom_player_names, test_roll_dice, test_initial_turn_state, test_dice_roll_sets_move, test_make_move_without_dice, test_make_move_with_dice, test_has_valid_moves_initial_position, test_get_available_moves, test_count_checkers_on_bar_initial.

## [0.0.25] - 2024-10-14
### Added
- Se crea la clase BackgammonGame y los métodos roll_dice, make_move, make_compound_move, _is_legal_move, switch_turn.
- Se agregan tests relacionados.

## [0.0.24] - 2024-10-12
### Added
- Se crea la clase TurnManager y los métodos set_moves_from_dice, use_move, get_forced_moves, _can_use_both_dice, _can_use_sequence, _can_use_any_move_with_die, switch_player, get_current_player, get_remaining_moves, is_turn_complete, has_move.
- Se agregan tests relacionados.

## [0.0.23] - 2024-10-11
### Added
- Se crea la clase GameStateManager y los métodos check_winner, is_game_over, get_winner, reset_game.
- Se agregan tests relacionados.

## [0.0.22] - 2024-10-09
### Added
- Se crea la clase MoveCalculator y los métodos calculate_destination, _calculate_from_bar, _calculate_normal_move, can_bear_off_exact_or_higher.
- Se agregan tests relacionados a MoveCalculator y MoveValidator.

## [0.0.21] - 2024-10-08
### Added
- Se crea la clase MoveValidator y los métodos is_valid_move, _is_valid_source, _is_valid_destination, must_enter_from_bar.

## [0.0.20] - 2024-10-07
### Added
- Se agregan tests: test_player_initialization, test_player_with_different_colors, test_player_names, test_player_get_methods, test_multiple_players, test_player_immutability.

## [0.0.19] - 2024-10-05
### Changed
- Se modifica la clase Player y se agregan tests: test_dice_initialization, test_rolls_return_values, test_roll_values_in_range, test_roll_updates_properties, test_is_double_detection, test_multiple_rolls_change_values.

## [0.0.18] - 2024-10-03
### Removed
- Se elimina la clase Checker.
### Added
- Se agregan prefijos y sufijos para atributos.
- Se modifica la clase Dice para cumplir con los principios SOLID.
- Se agregan tests: test_move_checker_clear_point, test_has_checkers_on_bar_initial, test_has_checkers_on_bar_with_checkers, test_has_checkers_on_bar_after_removal, test_can_bear_off_initial_position, test_can_bear_off_with_checkers_on_bar, test_can_bear_off_all_in_home_white, test_can_bear_off_all_in_home_black, test_can_bear_off_with_checkers_outside_home, test_is_winner_initial, test_is_winner_white_wins, test_is_winner_black_wins, test_is_winner_partial_off, test_show_board_runs, _setup_all_checkers_in_home.

## [0.0.17] - 2024-10-02
### Added
- Se agregan tests: test_get_point_valid, test_get_point_invalid, test_move_checker_normal, test_move_checker_to_occupied_same_color, test_move_checker_capture, test_move_checker_from_bar, test_move_checker_bear_off.

## [0.0.16] - 2024-09-29
### Changed
- Se modifican métodos de la clase Board.
### Added
- Se agrega format_point.

## [0.0.15] - 2024-09-26
### Added
- Se agrega el archivo coverage.rc y se arreglan reportes de integración continua.

## [0.0.14] - 2024-09-24
### Added
- Se agregan tests: test_bear_off_checker_success, test_bear_off_checker_fail, test_get_position, test_is_move_valid_out_of_bounds, test_is_move_valid_wrong_color, test_is_move_valid_to_pos_with_two_opponent.

## [0.0.13] - 2024-09-23
### Added
- Se agregan tests: test_get_position, test_is_move_valid, test_move_checker_invalid_color,  test_move_checker_to_pos_ocupado.

## [0.0.12] - 2024-09-22
### Added
- Se agregan tests: test_move_checker_invalid, test_bear_off_checker.

## [0.0.11] - 2024-09-16
### Added
- Se agregan tests: test_move_checker_valid, setUp.

## [0.0.10] - 2024-09-15
### Added
- Se agregan tests: test_change_name, test_change_color.
- Se agregan métodos: move_checker, bear_off_checker, get_position.

## [0.0.09] - 2024-09-14
### Added
- Se crea la clase Player y tests: test_init, test_str, test_different_players.

## [0.0.08] - 2024-09-13
### Added
- Se agregan tests: test_init_bar, test_to_bar_and_to_board.

## [0.0.07] - 2024-09-09
### Added
- Se realiza la migración a SonarCloud y se agregan las clases get_bar_off, get_off_count.
### Removed
- Se quita SonarCloud.

## [0.0.06] - 2024-09-08
### Added
- Se agregan métodos to_off, to_board, to_bar en Checker.

## [0.0.05] - 2024-09-04
### Added
- Se agrega el constructor de la clase Checker.

## [0.0.04] - 2024-09-02
### Added
- Se agrega la clase Checker.

## [0.0.03] - 2024-08-29
### Added
- Se agrega la clase Dice y los métodos roll, get_values, is_double.

## [0.0.02] - 2024-08-27
### Added
- Se agrega la clase Board y el método board_inicial.
- Se agregan tests del método board_inicial.

## [0.0.01] - 2024-08-26
### Added
- Se crea la estructura del proyecto como indica la rúbrica.
- Se agrega configuración de CircleCI.
