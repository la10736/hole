# La Buca

La buca si trova nella parte sinistra dello schermo e è un cerchio grande il doppio della palla. Ogni volta che facciamo
buca scompare e riappare in un altro punto questa volta preso a caso in tutto lo schermo.

## Il personaggio Buca

Come abbiamo fatto per la pallina prima la aggiungiamo al gioco dandogli coordinate del centro e dimensione. Quindi
in `hole.kv`, dentro a `<HoleGame>:` e prima di `Ball` mettimao:

```
    Hole:
        center: root.width/6, root.center_y
        size: 80, 80
```

Anche questa volta quando proviamo a eseguirlo ci dice che non conosce la `class <Hole>`. E come l'altra volta lo 
accontentiamo aggiungendo a `main.py`

```python
class Hole(Widget):
    pass
```

Ora non si arrabbia più, ma comunque non si vede niente, infatti non gli abbiamo detto come si deve disegnare una buca.
Rimediamo subito.

## Il disegno della Buca

Si tratta di una linea circolare di spessore 3. Quindi nel file `hole.kv` dobbiamo aggiungere prima di `<HoleGame>`

```
<Hole>:
    canvas:
        Line:
            width: 3
            circle: self.center_x, self.center_y, self.width/2
```

Rileggendo: dentro alla tela (`canvas`) abbiamo messo una linea (`Line`) spessa (`width`) 3 di tipo cerchio (`circle`).
Quando definiamo una linea di tipo cerchio bisogna dire dove è il centro e quanto è lungo il raggio,nel nostro caso
il centro lo abbiamo messo nel centro della *buca* e il raggio è metà della larghezza della buca.

Ora proviamo a far partire ... Come era successo per la palla non avviene nulla: infatti questo nuovo personaggio

## La Palla in Buca 

Sia la pallina he la buca hanno le questi campi:

* `x`
* `y`
* `right`
* `top`
