import pygame


class Ship():
    """Klasa przeznaczona do opisu statku"""

    def __init__(self, screen):
        """Inicjalizacja statku początkowego i jego położenie początkowe"""
        self.screen = screen

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Każdy nowy statek kosmiczny pojawia sie na dole ekranu
        self.rect_centerx = self.screen_rect.centerx
        self.rect_bottom = self.screen_rect.bottom

    def blitime(self):
        """Wyświetlenie statku kosmicznego w jego akutalnym położeniu"""
        self.screen.blit(self.image, self.rect)
      