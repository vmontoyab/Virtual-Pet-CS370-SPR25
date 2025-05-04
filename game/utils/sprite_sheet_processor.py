import pygame

def extract_frames(path, frame_width, frame_height, scale):
    sheet = pygame.image.load(path).convert_alpha()
    sheet_rect = sheet.get_rect()
    frames = []

    num_frames = sheet_rect.width // frame_width

    # Loop through cols (each col represents a frame in the action)
    for i in range(num_frames):
        x = i * frame_width
        frame = sheet.subsurface(pygame.Rect(x, 0, frame_width, frame_height))
        scaled_size = (int(frame_width * scale), int(frame_height * scale))
        frame = pygame.transform.scale(frame, scaled_size)
        frames.append(frame)

    return frames
