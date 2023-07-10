class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda=None
        self.derecha=None

class Arbol:
    def __init__(self,valor):
        self.raiz=Nodo(valor)

    def insertar(self, nodo, valor):
        if valor<nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda=Nodo(valor)
            else:
                self.insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha=Nodo(valor)
            else:
                self.insertar(nodo.derecha, valor)
    
    def recorrerPreorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.recorrerPreorden(nodo.izquierda)
            self.recorrerPreorden(nodo.derecha)
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_nodo(self.raiz, valor)
    
    def eliminarNodo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_nodo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_nodo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._encontrar_min_valor(nodo.derecha)
            nodo.derecha = self._eliminar_nodo(nodo.derecha, nodo.valor)
        return nodo
    
    def recorrerNiveles(self):
        if self.raiz is None:
            return
        nivelActual = [self.raiz]
        while nivelActual:
            nivelSiguiente = []
            for nodo in nivelActual:
                print(nodo.valor, end=" ")
                if nodo.izquierda:
                    nivelSiguiente.append(nodo.izquierda)
                if nodo.derecha:
                    nivelSiguiente.append(nodo.derecha)
            nivelActual = nivelSiguiente
