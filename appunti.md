# Appunti

## Init

Inizializzare `buildozer` e configurarlo

```
buildozer init
```

* `title = Hole`
* `package.name = hole`

## `main.py`

FIle di riferimento: creare `main.py` con dentro 

```
from kivy.app import App
from kivy.uix.widget import Widget

__version__ = "1.0"


class HoleGame(Widget):
    pass


class HoleApp(App):
    def build(self):
        return HoleGame()


if __name__ == '__main__':
    HoleApp().run()
```


* Eseguirlo in locale.
* Costruire la App

```buidozer android debug deploy```

## Pallina

Aggiungere la pallina: file `hole.kv` (nome deve essere la classe di `App` in minuscolo, meno App:
nel nostro caso `hole.kv`.

```
#:kivy 1.0.9

<Ball>:
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size

<HoleGame>:
    Ball:
        center_x: self.parent.center_x
        center_y: self.parent.center_y
        size: 20, 20
```

Proviamo a eseguirlo in locale e troviamo degligli errori:

```
kivy.factory.FactoryException: Unknown class <Ball>
```

Ci sta dicendo che l'elemento `<Ball>` che abbiamo descritto in `hole.kv` non esiste nel programma:
ha ragione.

Aggingiamo quindi

```python
class Ball(Widget):
    pass
```

Il **`Widget`** è l'elemento grafico di kivy piè semplice: tutti gli elementi grafice sono dei 
`Widget`

## Spostiamo la Pallina con il ditino

Dove mettiamo il dito spostiamo la pallina. Agganciare la property `ball` a `HoleGame` con l'id nel 
file `kw`. Ora che abbiamo la palla ad ogni `o_touch_down`spostiamo il `ball.center` in `touch.pos`.

### Esecizio

1. Quando rilasciamo (`on_touch_up`) deve tornare al centro
2.Facciamolo seguirenel trascinamento (`on_touch_move`)