# La Molla Invisibile

Il nostro gioco è quasi completo... ma troppo semplice. Guidare la pallina usando il tocco sullo schermo come direzione
e velocità rende molto semplice guidare la pallina in buca. Vogliamo scrivere un *sistema di guida* più meno diretto.
 
L'idea è quella di usare una molla immaginaria: Ogni volta che appoggiamo il dito creiamo una molla che attrae la palla
verso il dito, quando rilasciamo la molla scompare.

Come funziona una molla:

![Molla](molla.png)

Quando un oggetto è attaccato a una molla come ad esempio la nostra pallina rossa nel disegno, allora La pallina viene 
attratta dal punto in cui la molla è attacata con una forza **F** proporzionalle alla lunghezza **L** (la distanza tra
la palla e dove la molla è collegata. Per semplificare le cose abbiamo parlato di una molla *ideale* che ha come 
lunghezza minima 0, ma il concetto con le molle reali non cambia molto.

Quindi quello che faremo è:

1. Aggiungere a `HoleGame` un oggetto molla
2. In `update()` cambiare la velocità della palla usando la forza che la molla esercita sulla palla
3. In `on_touch_down()` aggiungere la molla e in `on_touch_up()` toglierla

## Aggiungiamo la molla

L'unica cosa che ci interessa della nostra molla sono le coordinate del suo centro. Ci basta quindi qualcosa del tipo
`(350, 200)` per rappresentare la molla con un centro in 350 x e 200 y.
 
In `main.py` nella classe `HoleGame` aggiungiamo:

```python
class HoleGame(Widget):
    spring = ObjectProperty((350, 200))
```

Per ora non abbiamo ancora fatto niente se non dire che `HoleGame` contiene ina molla (`spring`). Ogni molla ha una 
forza caratteristica che descrive quanto è rigida una molla e quindi quanta *fatica* bisogna fare per allungarla e 
quanto forte attrae una volta che è allungata: questa caratteristica è il numero con il quale moltiplichiamo la 
lunghezza per avere l'intensità della forza: useremo 0,0005.

## Aggiorniamo la velocità della palla con la forza della molla

Dobbiamo per prima cosa scrivere una funzione che torna la forza della molla che agisce sulla palla. In `HoleGame`
aggiungiamo 

```python
    def spring_strength(self):
        sx, sy = self.spring
        strength = Vector(sx, sy) - self.ball.center
        return strength * 0.0005
```

Per aggiornare la velocità della palla ci basta in update aggiungere in fondo:

```python
    def update(self, dt):
        ...
        strength = self.spring_strength()
        self.ball.velocity_x += strength.x
        self.ball.velocity_y += strength.y
```
