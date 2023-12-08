# Connect Four (Ligue Quatro)

Este projeto implementa o jogo Connect Four (Ligue Quatro) em Python, utilizando os recursos disponíveis na linguagem.

## Como Jogar

O Connect Four é um jogo clássico em que dois jogadores alternam jogadas, tentando formar uma linha de quatro fichas consecutivas da mesma cor, seja na horizontal, vertical ou diagonal. O tabuleiro possui sete colunas e seis linhas, e os jogadores escolhem em qual coluna colocar sua ficha.

Para jogar:

1. Execute o arquivo `Main.py`.
2. Siga as instruções para configurar o número de jogadores.
3. Durante o jogo, os jogadores serão alternados, e cada um fará sua jogada escolhendo a coluna desejada.

## Diagrama UML

![Diagrama UML](/UML_Ligue4.png)

O diagrama UML apresenta a estrutura das classes do projeto, destacando a relação entre elas.

## Configuração do Ambiente

1. **Ambiente Virtual (Opcional para Pygame):** Se você pretende rodar o jogo com Pygame, é recomendável criar um ambiente virtual. Para isso, execute:

   ```bash
   python -m venv venv
   ```

   Em seguida, ative o ambiente virtual:

   - No Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - No Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

2. **Execução sem Pygame:**
   Se você não estiver utilizando Pygame, pode executar o projeto normalmente sem a necessidade de um ambiente virtual.

   ```bash
   python Main.py
   ```

## Contribuições

Contribuições são bem-vindas! Se encontrar bugs, problemas ou tiver sugestões para melhorar o jogo, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Melhorias Futuras

- Implementar funcionalidades com Pygame para uma experiência mais interativa.
- Melhorar a organização do código e adicionar mais comentários.
- Adicionar testes automatizados.

## Execução de Testes

Para executar os testes, utilize o seguinte comando:

```bash
python -m pytest -v test/
```

ou

```bash
python -m pytest test/
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE), o que significa que você tem total liberdade para utilizá-lo da maneira que preferir. Divirta-se jogando e contribuindo!