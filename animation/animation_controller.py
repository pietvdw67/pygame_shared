class AnimationController:
    """
    Handles different animation states and return current animation image based on delay
    """

    def __init__(self):

        self._animation_images = {}
        self._animation_delays = {}
        self._active_animation = ''
        self._current_frame = 0
        self._frame_count = 0

    def load_animation(self, name, images, delay=0):

        self._animation_images[name] = images
        self._animation_delays[name] = delay

    def get_image(self):
        self._set_current_frame()
        return self._animation_images[self._active_animation][self._current_frame]

    def set_active_animation(self, name):
        self._active_animation = name
        self._current_frame = 0
        self._frame_count = 0

    def _set_current_frame(self):
        if self._active_animation == '':
            self._active_animation = next(iter(self._animation_images))

        if len(self._animation_images[self._active_animation]) == 1:
            self._current_frame = 0
            return

        delay = self._animation_delays[self._active_animation]

        if delay == 0:
            self._current_frame = 0
            return

        self._frame_count += 1
        if self._frame_count < delay:
            return

        self._frame_count = 0
        self._current_frame += 1
        if self._current_frame >= len(self._animation_images[self._active_animation]):
            self._current_frame = 0
