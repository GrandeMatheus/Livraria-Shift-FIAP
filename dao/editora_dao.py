from model.editora import Editora


class EditoraDAO:


    def __init__(self):
        self.__editora: list[Editora] = list()


    def listar(self) -> list[Editora]:
        return self.__editora


    def adicionar(self, editora: Editora) -> None:
        self.__editora.append(editora)


    def remover(self, editora_id: int) -> bool:
        encontrado = False
        for e in self.__editora:
            if (e.id == editora_id):
                index = self.__editora.index(e)
                self.__editora.pop(index)
                encontrado = True
                break
        return encontrado


    def buscar_por_id(self, editora_id) -> Editora:
        edi = None
        for e in self.__editora:
            if (e.id == editora_id):
                edi = e
                break
        return edi
   
    def ultimo_id(self) -> int:
        index = len(self.__editora) -1
        if (index == -1):
            id = 0
        else:
            id = self.__editora[index].id
        return id