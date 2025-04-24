import pygame

def extract_frames(path, cat_size, scale):
    sheet = pygame.image.load(path).convert_alpha()
    sheet_rect = sheet.get_rect()
    frames = []

    # Loop through cols (each col represents a frame in the action)
    for x in range(0, sheet_rect.width, cat_size):
        frame = sheet.subsurface(pygame.Rect(x, 0, cat_size, cat_size))
        scaled_size = (int(cat_size * scale), int(cat_size * scale))
        frame = pygame.transform.scale(frame, scaled_size)
        frames.append(frame)

    return frames
