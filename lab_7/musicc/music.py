import pygame
import os



pygame.init()
pygame.mixer.init()
music_folder = r"C:\Users\Aitali\Documents\new folder\labs\lab_7\musicc"
music_files = [
    "Escape - Nemzzz (Remix by AJ).mp3",
    "matt-johnson-earths-mysteries.mp3",
    "Metro Boomin (Travis Scott, YoungThug) - Trance.mp3"]
current_track = 0
pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
ekran = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont('Times', 20)
pygame.mixer.music.play()
def display_text(text):
    ekran.fill((0, 0, 0))
    text_surface = font.render(text, True, (255, 255, 255))
    ekran.blit(text_surface, (100, 150))
    pygame.display.flip()
def draw_buttons():
    pygame.display.flip()
display_text("Playing: " + music_files[current_track])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    display_text("Pausada: " + music_files[current_track])
                else:
                    pygame.mixer.music.unpause()
                    display_text("Oynauda: " + music_files[current_track])
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
                pygame.mixer.music.play()
                display_text("Oynauda: " + music_files[current_track])
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
                pygame.mixer.music.play()
                display_text("Oynauda: " + music_files[current_track])
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                display_text("Toktady")
    draw_buttons()

pygame.quit()
