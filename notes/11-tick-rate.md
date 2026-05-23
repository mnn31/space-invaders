# Tick rate

The main loop uses `pygame.time.Clock` to cap frame rate.
Alien and bullet velocities are expressed per-frame, so changing the cap
will change apparent game speed.