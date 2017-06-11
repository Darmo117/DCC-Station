# -*- coding: utf-8 -*-

import abc

class Sign:
  def __init__(self):
    self._previous_signs = []

  def add_sign_to_update(self, sign):
    self._previous_signs.append(sign)

  def remove_sign(self, sign):
    self._previous_signs.remove(sign)

# Interfaces

class Freeable(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def set_track_free(self):
    """Sets the track free."""
    return

  @abc.abstractmethod
  def is_track_free(self):
    """Tells if the track is free."""
    return

class Semaphore(Freeable):
  @abc.abstractmethod
  def close_semaphore(self):
    """Closes the semaphore."""
    return

  @abc.abstractmethod
  def is_semaphore_closed(self):
    """Tells if the semaphore is closed."""
    return

class Square(Freeable):
  @abc.abstractmethod
  def close_square(self):
    """Closes the square."""
    return

  @abc.abstractmethod
  def is_square_closed(self):
    """Tells if the square is closed."""
    return
