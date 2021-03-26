aliens = []

for alien_nu in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print(len(aliens))

for alien in aliens[:5]:
    print(alien)
