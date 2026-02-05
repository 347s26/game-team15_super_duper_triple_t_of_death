# data model

## big game!
- boards: board[9]
- current_player: player
- active_board: index 0–8 | null
- winner: Player | draw | null

## board!
- cells: cell[9]
- winner: Player | draw | null
- is_full: boolean

## cell!
- value: X | O | null

## player!
- X
- O
