Livraria SHIFT - Mastering Python
Este projeto foi desenvolvido como parte do curso de Python Fundamentals oferecido pela FIAP. O sistema simula uma aplicação de gerenciamento de uma livraria, permitindo que o usuário cadastre, edite e visualize categorias de livros, editoras, autores e os próprios livros. O projeto segue uma estrutura em camadas que separa a lógica de negócio, acesso a dados e modelagem das entidades.

Funcionalidades
O programa oferece as seguintes funcionalidades:

Gerenciamento de Categorias
Permite criar, listar, editar e remover categorias de livros.

Gerenciamento de Editoras
Permite criar, listar, editar e remover editoras.

Gerenciamento de Autores
Permite criar, listar, editar e remover autores.

Gerenciamento de Livros
Permite cadastrar, listar, editar e remover livros, desde que haja pelo menos uma categoria, editora e autor cadastrados.

Estrutura do Projeto
O projeto foi organizado em três camadas principais:

Model: Representa as entidades do sistema (Categoria, Editora, Autor, Livro) com seus respectivos atributos.

DAO (Data Access Object): Responsável pelo acesso e manipulação de dados (armazenamento, busca, edição e exclusão). Cada entidade tem seu próprio DAO.

Service: Contém as regras de negócio e a lógica das operações para cada entidade. Cada serviço faz uso de seu DAO correspondente.

Diretórios e Arquivos
model/
Contém as classes que representam as entidades do sistema, como:

categoria.py
editora.py
autor.py
livro.py
dao/
Contém os objetos de acesso a dados (DAOs) responsáveis por manipular os dados das entidades:

categoria_dao.py
editora_dao.py
autor_dao.py
livro_dao.py
service/
Contém os serviços responsáveis pelas operações de cada entidade:

categoria_service.py
editora_service.py
autor_service.py
livro_service.py
main.py
Arquivo principal que inicia o programa e exibe o menu de opções ao usuário.

Tecnologias Utilizadas
Python - Linguagem principal do projeto.
Estrutura modular com camadas model, dao e service.
Sobre
Este projeto foi desenvolvido durante o curso Python Fundamentals pela FIAP para consolidar os conceitos aprendidos, como:

Manipulação de dados
Estruturação de código em camadas
Regras de negócio
Desenvolvimento de sistemas orientados a serviços.
