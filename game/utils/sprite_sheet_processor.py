import pygame

def extract_frames(path, size, scale):
    sheet = pygame.image.load(path).convert_alpha()
    sheet_rect = sheet.get_rect()
    frames = []

    # Loop through cols (each col represents a frame in the action)
    for x in range(0, sheet_rect.width, size):
        frame = sheet.subsurface(pygame.Rect(x, 0, size, size))
        scaled_size = (int(size * scale), int(size * scale))
        frame = pygame.transform.scale(frame, scaled_size)
        frames.append(frame)

    return frames
