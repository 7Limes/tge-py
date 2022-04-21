# tge-py
A small game engine using only terminal graphics.

## Initalizing
- Start by creating a `Surface` object with a width and height
- Then fill it with some characters and display it:

```py
import tge

WIDTH, HEIGHT = 5, 5
surf = tge.Surface(WIDTH, HEIGHT)
surf.set_drawchar('.')
surf.fill()
surf.display()
```
Output:
```
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```

You can also change the spacing between characters using the `spacing=` keyword argument in the constructor (default is `1`):
```py
surf = tge.Surface(WIDTH, HEIGHT, spacing=0)
```
Output:
```
.....
.....
.....
.....
.....
```

## Drawing Methods
These methods are all part of the `Surface` class.
- `draw_pixel(self, x: int, y: int, char: str=None) -> bool`
- `draw_straight_line(self, x: int, y: int, length: int, dir: str) -> bool`
- `draw_rect(self, x: int, y: int, width: int, height: int, fill: bool=False)`
- `draw_border(self)`
- `draw_line(self, x1: int, y1: int, x2: int, y2: int)`
- `draw_polygon(self, points: list)`
- `draw_ellipse(self, h: int, k: int, a: int, b: int, fill: bool=False)`
- `draw_text(self, x: int, y: int, text: str)`
- `fill(self)`
- `fill_row(self, row: int)`
- `fill_col(self, col: int)`
- `blit(self, other, x: int, y: int)`

### blit() Method
`blit()` takes in another surface object as input and pastes it on top of the current surface at `x, y`:
```py
import tge

mainsurf = tge.Surface(5, 5)
mainsurf.set_drawchar('.')
mainsurf.fill()

smallsurf = tge.Surface(3, 3)
smallsurf.set_drawchar('#')
smallsurf.fill()
mainsurf.blit(smallsurf, 0, 0)
mainsurf.display()
```
Output:
```
# # # . .
# # # . .
# # # . .
. . . . .
. . . . .
```

## Changing Characters and Colors
To change the draw character, use the `set_drawchar()` method:
```py
import tge

surf = tge.Surface(5,5)
surf.set_drawchar('#')
surf.draw_border()
surf.display()
```
Output:
```
# # # # #
#       #
#       #
#       #
# # # # #
```

To change pixel color, there are three methods:
- `set_color(self, color: str, type='fg', bright=False)`
- `set_color_rgb(self, r: int, g: int, b: int, type='fg')`
- `set_color_code(self, color: str)`

### set_color()
`set_color()` allows you to choose from any of the following ANSI colors:
- `'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'`

You can tweak these colors by changing the `type=` and `bright=` keyword arguments. `type` can be either `'fg'` (default) or `'bg'`, representing foreground and background color respectively.
`bright` is simply an ANSI preset that will make the specified color brighter (is `False` by default).

Examples:
```py
surf.set_color('red')
surf.set_color('green', type='bg')
surf.set_color('magenta', bright=True)
```

### set_color_rgb
`set_color_rgb` sets the color to a specfic rgb value.

Again, you can change the `type=` keyword argument to change between foreground `'fg'`, and background `'bg'`.

Examples:
```py
surf.set_color_rgb(255, 0, 0)
surf.set_color_rgb(0, 127, 255, type='bg')
```

### set_color_code
`set_color_code()` simply sets the color code to whatever string you pass in. There are no checks to make sure that the code is valid, so make sure you know what you're doing.

Example:
```py
surf.set_color_code('\033[31m')
```
