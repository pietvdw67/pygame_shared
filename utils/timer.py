import pygame
from enum import Enum


class TimerType(Enum):
    ONCE_OFF = "once-off"
    LOOP = "loop"


class Timer:
    def __init__(self):
        self.timeouts = {}

    def add_timer(self, name: str, timer_type: TimerType, duration_milli: int, active: bool, callback):
        self.timeouts[name] = {
            "time_type": timer_type,
            "duration_milli": duration_milli,
            "callback": callback,
            "active": active,
            "start_time": pygame.time.get_ticks()
        }

    def activate_timer(self, name: str):
        self.timeouts[name]["active"] = True
        self.timeouts[name]["start_time"] = pygame.time.get_ticks()

    def deactivate_timer(self, name: str):
        self.timeouts[name]["active"] = False

    def change_duration(self, name: str, duration_milli):
        self.timeouts[name]["duration_milli"] = duration_milli

    def update(self):
        current_time = pygame.time.get_ticks()

        for key in self.timeouts:
            if not self.timeouts[key]["active"]:
                continue

            # Check if time has expired on current timout object
            if current_time - self.timeouts[key]["start_time"] >= self.timeouts[key]["duration_milli"]:
                self.timeouts[key]["start_time"] = current_time

                # Fire callback
                self.timeouts[key]["callback"]()

                # disable if it was a once off timer
                if self.timeouts[key]["time_type"] == TimerType.ONCE_OFF:
                    self.timeouts[key]["active"] = False
                    continue


