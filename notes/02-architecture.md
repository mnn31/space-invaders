# Architecture

The game is a single-file Pygame loop:

1. Initialize display + sounds
2. Spawn player ship at bottom-center
3. Spawn alien row(s) at top
4. Loop: poll input, move sprites, detect collisions, render, tick
5. Exit on quit event or game-over