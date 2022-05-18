import pygame as pyg


class GameObject(pyg.sprite.Sprite):

    # methods
    def __init__(self) -> None:
        pyg.sprite.Sprite.__init__(self)

    def update(self, dt: float) -> None:
        pass

    def get_position(self) -> pyg.Rect:
        return self.rect
