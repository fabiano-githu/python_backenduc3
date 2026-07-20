'''
1.	Crie um dicionário com dados de um funcionário: nome, idade e cargo.

'''


print("\n--------Menu escolha-------\n")

funcionário = {
    "nome": "Carlos",
    "idade": 23,
    "cargo": "programador"
}

print(funcionário)

print("\n---------------------------\n")


# -------------------------------------------------------------


'''
################# EM 🟨 JAVASCRIPT ##################
// Crie um objeto com dados de um funcionário.

// Criando um objeto chamado funcionario
const funcionario = {
    nome: "Carlos",
    idade: 23,
    cargo: "Programador"
};

// Mostrando o objeto na tela
console.log(funcionario);



            (const funcionario = {)
| Palavra       | Tradução    | Explicação                                                |
| ------------- | ----------- | --------------------------------------------------------- |
| `const`       | constante   | Cria uma variável que não pode apontar para outro objeto. |
| `funcionario` | funcionário | Nome da variável.                                         |
| `=`           | recebe      | Atribui um valor à variável.                              |
| `{`           | abre chaves | Início do objeto.                                         |


nome: "Carlos",
| Palavra    | Tradução         |
| ---------- | ---------------- |
| `nome`     | nome             |
| `:`        | recebe / associa |
| `"Carlos"` | valor            |


idade: 23,
| Palavra | Tradução       |
| ------- | -------------- |
| `idade` | idade          |
| `23`    | valor numérico |


cargo: "Programador"
| Palavra         | Tradução |
| --------------- | -------- |
| `cargo`         | cargo    |
| `"Programador"` | valor    |


Indica o fim do objeto.
};

            (console.log(funcionario);)
| Palavra       | Tradução            | Explicação                       |
| ------------- | ------------------- | -------------------------------- |
| `console`     | console             | Área onde aparecem as mensagens. |
| `log`         | registrar / mostrar | Exibe informações no console.    |
| `funcionario` | funcionário         | Objeto que será exibido.         |




'''

# -------------------------------------------------------------


'''
################# EM ☕ JAVA ##################

import java.util.HashMap;

public class Main {
    public static void main(String[] args) {

        HashMap<String, Object> funcionario = new HashMap<>();

        funcionario.put("nome", "Carlos");
        funcionario.put("idade", 23);
        funcionario.put("cargo", "Programador");

        System.out.println(funcionario);
    }
}

               (import java.util.HashMap;)
| Palavra   | Tradução    | Explicação                                   |
| --------- | ----------- | -------------------------------------------- |
| `import`  | importar    | Importa uma biblioteca.                      |
| `java`    | Java        | Linguagem Java.                              |
| `util`    | utilitários | Pacote com classes úteis.                    |
| `HashMap` | mapa hash   | Estrutura que guarda dados em chave e valor. |



                   (public class Main)
| Palavra  | Tradução  | Explicação                            |
| -------- | --------- | ------------------------------------- |
| `public` | público   | Pode ser acessada por qualquer lugar. |
| `class`  | classe    | Modelo para criar objetos.            |
| `Main`   | principal | Nome da classe.                       |




         (public static void main(String[] args))
| Palavra  | Tradução   | Explicação                                 |
| -------- | ---------- | ------------------------------------------ |
| `public` | público    | Pode ser acessado pelo Java.               |
| `static` | estático   | Não precisa criar um objeto para executar. |
| `void`   | vazio      | Não retorna nenhum valor.                  |
| `main`   | principal  | Método onde o programa começa.             |
| `String` | texto      | Tipo de dado textual.                      |
| `args`   | argumentos | Recebe informações da linha de comando.    |




(HashMap<String, Object> funcionario = new HashMap<>();)

        | Palavra       | Tradução               |
        | ------------- | ---------------------- |
        | `HashMap`     | mapa hash              |
        | `String`      | texto                  |
        | `Object`      | objeto (qualquer tipo) |
        | `funcionario` | nome da variável       |
        | `=`           | recebe                 |
        | `new`         | novo                   |
        | `HashMap()`   | cria um novo HashMap   |




    (funcionario.put("nome", "Carlos");)

        | Palavra       | Tradução |
        | ------------- | -------- |
        | `funcionario` | variável |
        | `put`         | colocar  |
        | `"nome"`      | chave    |
        | `"Carlos"`    | valor    |



        
        (System.out.println(funcionario);)
        | Palavra   | Tradução       |
        | --------- | -------------- |
        | `System`  | sistema        |
        | `out`     | saída          |
        | `println` | imprimir linha |





'''


# -------------------------------------------------------------


'''
################# EM 🎯 DART ##################

void main() {

  Map<String, dynamic> funcionario = {
    "nome": "Carlos",
    "idade": 23,
    "cargo": "Programador"
  };

  print(funcionario);

}


            void main() {
| Palavra | Tradução    | Explicação                                   |
| ------- | ----------- | -------------------------------------------- |
| `void`  | vazio       | A função não retorna nenhum valor.           |
| `main`  | principal   | É a função principal onde o programa começa. |
| `()`    | parênteses  | Indicam que `main` é uma função.             |
| `{`     | abre chaves | Início do bloco de código.                   |


         Map<String, dynamic> funcionario = {
         | Palavra       | Tradução    | Explicação                                     |
| ------------- | ----------- | ---------------------------------------------- |
| `Map`         | mapa        | Estrutura que armazena dados em chave e valor. |
| `String`      | texto       | Tipo das chaves do Map.                        |
| `dynamic`     | dinâmico    | Aceita qualquer tipo de valor.                 |
| `funcionario` | funcionário | Nome da variável.                              |
| `=`           | recebe      | Atribui um valor à variável.                   |
| `{`           | abre chaves | Início do Map.                                 |


        "nome": "Carlos",
| Palavra    | Tradução         |
| ---------- | ---------------- |
| `"nome"`   | chave            |
| `:`        | recebe / associa |
| `"Carlos"` | valor            |


        "idade": 23,
| Palavra   | Tradução |
| --------- | -------- |
| `"idade"` | chave    |
| `23`      | valor    |


    "cargo": "Programador",
| Palavra         | Tradução |
| --------------- | -------- |
| `"cargo"`       | chave    |
| `"Programador"` | valor    |


Indica o fim do Map.
};


print(funcionario);
| Palavra       | Tradução    | Explicação                    |
| ------------- | ----------- | ----------------------------- |
| `print`       | imprimir    | Exibe informações no console. |
| `funcionario` | funcionário | Variável que será exibida.    |



Indica o fim da função main().
}

Saída
{nome: Carlos, idade: 23, cargo: Programador}


'''
