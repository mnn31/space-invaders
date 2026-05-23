# Input handling

Uses `pygame.event.get()` each frame and dispatches on `KEYDOWN` / `KEYUP`.
Key state is held between events so movement persists while a key is down.