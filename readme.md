# Animation Controller

A controller for handling different states of an animation

## Creating the controller

Initialize the controller
```python
from pygame_shared.animation.animation_controller import AnimationController

    def __init__(self, screen, game_state):
        self.player_animation_controller = AnimationController()
```

## Load animations from images

You can use the image utilities to retrieve the images.
The loading of images was kept separate due to too many parameters that could tweak how the images could be loaded

```python
from pygame_shared.utils.image_utils import ImageUtils

    sheet = os.path.join(Constants.ASSETS_PATH, "spritesheets", "run.png")
    images = ImageUtils.get_animation_frames_from_sprite_sheet(
        sheet_name=sheet,
        cols=12,
        rows=1,
        scale=3
    )
    self.player_animation_controller.load_animation("run", images, 4)
```

## Swap between state

On your keypress events change the state to any loaded animation name

```python
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.player_animation_controller.set_active_animation("idle")
```
