class Autor:


    def __init__(self, id: int, nome: str, endereco: str, telefone: str, bio: str):
        self.__id: int = id
        self.__nome: str = nome
        self.__endereco: str = endereco
        self.__telefone: str = telefone
        self.__bio: str = bio


    @property
    def id(self) -> int:
        return self.__id
   
    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def nome(self) -> str:
        return self.__nome


    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    
    @property
    def endereco(self) -> str:
        return self.__endereco


    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco


    @property
    def telefone(self) -> str:
        return self.__telefone


    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def bio(self) -> str:
        return self.__bio


    @bio.setter
    def bio(self, bio: str):
        self.__bio = bio