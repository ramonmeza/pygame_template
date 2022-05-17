import pygame as pyg

from typing import List


class Game(pyg.Surface):

    # variable declarations
    _game_objects: List[pyg.sprite.Sprite]


    # methods
    def __init__(self, width: int, height: int) -> None:
        # subclass init
        pyg.Surface.__init__(self, size=(width, height))

        # initialize variables
        self._game_objects = []
        spr = pyg.sprite.Sprite()
        spr.rect

    def update(self, dt: float) -> None:
        # do updates
        for game_object in self._game_objects:
            game_object.update(dt)

        # render
        self._render()

    def _render(self):
        for game_object in self._game_objects:
            self.blit(game_object, game_object.get_position())
