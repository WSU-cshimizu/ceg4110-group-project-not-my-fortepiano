import time
import fluidsynth
import pygame


velocity = 127  # 127 is max for a.sf2
fs = fluidsynth.Synth()
fs.start()
sfid = fs.sfload(
    "Nice-Steinway-Lite-v3.0.sf2"
)  # from https://sites.google.com/site/soundfonts4u/
fs.program_select(0, sfid, 0, 0)

pygame.init()

octave = 4
note = 0

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                note = octave * 12 + 12
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_j:
                note = octave * 12 + 14
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_k:
                note = octave * 12 + 16
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_l:
                note = octave * 12 + 17
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_SEMICOLON:
                note = octave * 12 + 19
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_f:
                note = octave * 12 + 11
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_d:
                note = octave * 12 + 9
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_s:
                note = octave * 12 + 7
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_a:
                note = octave * 12 + 5
                fs.noteon(0, note, velocity)
            if event.key == pygame.K_u:
                octave += 1
                print(octave)
            if event.key == pygame.K_r:
                octave -= 1
                print(octave)


# fs.noteon(0, 76, velocity)

# time.sleep(2.0)

# fs.delete()
