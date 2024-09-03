from model.autor import Autor


class AutorDAO:


    def __init__(self):
        self.__autor: list[Autor] = list()


    def listar(self) -> list[Autor]:
        return self.__autor


    def adicionar(self, autor: Autor) -> None:
        self.__autor.append(autor)


    def remover(self, autor_id: int) -> bool:
        encontrado = False
        for a in self.__autor:
            if (a.id == autor_id):
                index = self.__autor.index(a)
                self.__autor.pop(index)
                encontrado = True
                break
        return encontrado


    def buscar_por_id(self, autor_id) -> Autor:
        aut = None
        for a in self.__autor:
            if (a.id == autor_id):
                aut = a
                break
        return aut
   
    def ultimo_id(self) -> int:
        index = len(self.__autor) -1
        if (index == -1):
            id = 0
        else:
            id = self.__autor[index].id
        return id
   