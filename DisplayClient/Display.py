#! /usr/bin/python3

from pygame.locals import *
from pygame import *
import pygame

from threading import Thread, Lock
import time


class Display:
    def __init__(self):
        pygame.init()
        self._fpsClock = pygame.time.Clock()
        self._keyBuffer = []
        self._window = display.set_mode((520, 480), SWSURFACE)
        pygame.display.set_caption("FlatMountain2D")
        self._displayLock = Lock()
        self._keyBufferLock = Lock()
        self._alive = True
        self._backGroundExecuter = Thread(target=self._run)
        self._backGroundExecuter.start()

    def draw_rectangle(self, pos, size, color):
        """
        Simple function for direct drawing of rectangles. Do not use except for testing and debugging.
        """
        with self._displayLock:
            pygame.draw.rect(self._window, color, Rect(pos, size))

    def _run(self):
        """
        Collects user inputs and stores them in buffers.
        Updates windowcontent and performs fps control.
        designed to run in an seperate thread
        """
        while self._alive:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    with self._keyBufferLock:
                        self._keyBuffer.append(event.unicode)
            with self._displayLock:
                pygame.display.flip()
            self._fpsClock.tick(30)

    def get_keys(self):
        with self._keyBufferLock:
            keys = self._keyBuffer[:]
            self._keyBuffer = []
        return keys

    def close(self):
        self._alive = False
        self._backGroundExecuter.join()
        pygame.quit()

if __name__ == "__main__":
    testwindow = Display()
    testwindow.draw_rectangle((10, 10), (100, 80), (75, 0, 100))
    time.sleep(5)
    testwindow.close()
