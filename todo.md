## Listado de cosas por hacer según nivel de importancia
Ultima actualización: 26/09/2024

|**NRO** |**Tarea**  | **Finalización**  |
|-----|--|---------------|
|1| Documentar el programa   |       ❌       |
|2|La "sombra" que pasa luego que de un nodo se actualizado debe ser eliminada/actualizada en segundo plano (aplicado a todo objeto que herede desde [BasisSquare](/core/models/base/include/BasisSquare.py)) | ❌ |
|3|cuando el jugador pase por un objeto "pasable no colecionable" debe regresar a su estado anterior (ejemplo anterior) | ❌|
|4| cambiar varias funciones que reciben un nodo por argumento (de cara al desarrollador final, osea, que use un "main.py") pueda ser el nodo o la ID:int de dicho | ❌ |
|5| hacer una función "no lineal" que habra un hilo una vez que el juego empieze y este a la espera que este termine para volver al menos principal (eso incluye una vez que desde un menu de pausa sea definido dicho even)| ❌|
|6|reemplazar varios mensajes de error en diferentes parte del programa (principalmente los Basis y Logic)| ❌|
|7|pasar los @overload necesarios a los .pyi requeridos (incluye logic y otros)| ❌ |
|8|escribir una función para [Structure](/core/models/data/d2/structure.py) "del_geometry" (detalles en el archivo)| ❌|
|9|agregar retornos REALES de cada función| ❌|
|10|revisar el codigo en busca de posibles no verificaciones de tipos usando secure_type_one | ❌ |
|11| reestructurar codigo/importaciones desde [BasisTreeNode](/core/models/base/include/BasisTreeNode.py) o colocar MEJORES verificadores de "valores" | ❌ |
|12| la función "next_to" de "mapa" debe recibir por argumento un nodo para obtener su .vec correspondiente | ❌|
|13| agregar unas instrucciones de "move_to" de [BasisMove](/core/models/base/constant/BasisMover.py) para que actualize el vector usando los .in_y/in_x correspondientes al objeto dado | ❌ |
|14| refactorizar nombres que empiezen con "Basis" o similares | ❌ |
|15| darle a cada variable un tipo (dentro de los posible) | ❌ |
|16| escribir dentro de [init](/core/__init__.py) las clases/tipos que se pueden acceder con la correspondiente documentación FINAL | ❌|
|17| agregar un posible caso donde un jugador este rodeado (por alguna razon) por objetos a su alrededor y no tenga un self.bef para agregar (de preferencia que se use " " o un caracter por defecto) | ❌|
|18| **OPCIONAL**: agregar un tipo de caracter nulo a los heredados de [Object2D](/core/models/data/d2/base/object2d.py) diferentes de " " y .character (previsto que se tiene a este punto) | ❌ | 
|19| agregar un caso si se presionan dos botones para ir en direccional (referido a [Jugador](/core/models/data/d2/interactive/player.py)) | ❌|
|20| agregar "set_meta" a cada nodo declarado | ❌ |
|21| reemplantearze el organigrama de la heredación de cada nodo | ❌|
|22| simplificar funciones _num_in_rng y _inter en [Mov](/core/models/data/d2/base/mov.py) | ❌ |
|23| agregar sistema de logros | ❌ |
|24| agregar secciones para creditos (disporse por todo el motor y [main](/main.py)) | ❌ |
## Autores originales
- [Z3R0_GT](https://github.com/Z3R0GT/)
- EDUARDO OJEDA, DIEGO ANDRES : primer speed runner en acabar el juego (presiono 10 veces una tecla) y primer beta tester

