# Pygame Template

A simple template project for Pygame.


## Classes


### `App`

[Source code](src/app.py)

The `App` class is used to handle window events and other "application-level" events. It loads window settings from [settings.json5](data/settings.json5), initializes the PygameGUI manager, initializes the `Game` object, handles drawing the `Game` and GUI, and handles updating the game.

In general, add functionality to `App` that is not game related, but instead window related. If there were a taskbar, I'd put the functionality into `App`.


### `Game`

[Source code](src/game.py)

The `Game` class is used to update and draw `GameObject` objects. It acts as "the world" for the game, allowing game objects to be added to that world and draw into the world. 

* It might be nice to add a camera to the `Game` calss, which will be used to view a specific section of the world. 


### `GameObject`

[Source code](src/game_object.py)

`GameObject` is a base class for more complex game objects you will make. It contains an `update()` method which is called every frame and passes the delta time between frames as the parameter `dt`. All of your game's objects should derive from `GameObject` and then be added to the `Game` class.

>Note to self:
>
> It would be nice to have a `GameObjectFactory` class which would *auto-magically* create and add `GameObject` objects to the `Game` instance.....


### `Settings`

[Source code](src/settings.py)

The `Settings` class contains a static method `load()` to load `JSON5` data from a given `path` attribute and optional `section` attribute.

Setting files should be in [`JSON5`](https://json5.org/) format and can contain sections, which would be other `JSON5` objects within the root `JSON5` object.

## Settings Example

Below will show an example of how settings can be loaded and how the `Settings` class works.

`data/my_settings.json5`

```json5
{
    sectionA: {
        attribute1: 'hello, world!',
        attribute2: 24
    },
    sectionB: {
        attributeX: 11,
        attributeY: [ 1, 2, 3, 4 ]
    }
}
```


### Example 1

```py
settings_obj = Settings.load('data/my_settings.json5')
print(settings_obj)

```

Results

```json5
{'sectionA': {'attribute1': 'hello, world!', 'attribute2': 24}, 'sectionB': {'attributeX': 11, 'attributeY': [1, 2, 3, 4]}}
```


### Example 2

```py
settings_obj = Settings.load('data/my_settings.json5', 'sectionA')
print(settings_obj)

```

Results

```json5
{'attribute1': 'hello, world!', 'attribute2': 24}
```
