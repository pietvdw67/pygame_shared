# Timer

Timer that can execute multiple timers either in loops or once off

## Create the timer

```pyton
from pygame_shared.utils.timer import Timer, TimerType

    def __init__(self, screen, game_state):
        self.timer = Timer()
```

## Add a once off timer

After the time was fired, it will be disabled
Pass a callback function that will be called when the timer expired

```python
self.timer.add_timer(
    name="test",
    timer_type=TimerType.ONCE_OFF,
    active=True,
    duration_milli=1000,
    callback=lambda: print("timeout"))
```

## Add a repeating timer

After every amount of milli seconds the timer will fire

```python
self.timer.add_timer(
    name="test_loop",
    timer_type=TimerType.LOOP,
    active=True,
    duration_milli=1000,
    callback=lambda: print("loop_timeout"))
```

## Call timer to update

In your game loop call timer.update to update timers and check for timeouts

```python
self.timer.update()
```

## Activate or disactivate timers

Call activate_timer or deactivate_timer to either enable or disable a timer

```python
self.timer.activate_timer("test_loop")
self.timer.deactivate_timer("test_loop")
```

## Change timer duration

Call the change_duration method to change the duration of the timer
The below will change the timer duration to execute every 2 seconds

```python
self.timer.change_duration("test_loop", 2000)
```

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

---
# Image Packer

Tool that creates a sprite sheet from images in a folder

## Executing

```python
Execute: pygame_shared.tools.image_packer.image_packer_ui.py
```