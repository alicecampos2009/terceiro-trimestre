//arrays -> vetores, matrizes
// estrutra de dados para armazenar um conjunto de elementos

let frutas = ["Banana", "Maçã", "Melancia"]; //array de tamanho 3
console.log(frutas);
console.log(frutas[1]);

let numeros = new Array(2, 8, 9, 10);
console.log(numeros);

let arrayVazio = [];
console.log(arrayVazio);
arrayVazio[0] = "Alice";
console.log(arrayVazio);

//Tamanho do array -> length
let dados = [10, 50, 30]; //tamanho 3 -> legth 3

console.log(dados.length);

contadorDeChances = -1;
chancesRestantesElement.textContent = MAX_CHANCES; //Mostra o total de chances

// Limpar as mensagens anteriores 
menssagemElement.textContent = '';
palpitesAnterioresElement.textContent = '';
listaDePalpites = []


menssagemElement.style.color = '#f0f0f0'; // Cor padrão do texto
dicaElement.style.color = '#ffeb3b'; // Cor padrão da ética

// Reativar o campo de palpite e o botão de enviar
campoPalpite.disabled = false;
botãoEnviarPalpite.disabled = false;
campoPalpite.value = ''; // Limpa o campo de entrada
campoPalpite.focus(); // Coloca o cursor para o usuário digitar

// Esconder o botão de reiniciar
botaoIniciar.classList.add('hidden');

//2. Função para verificar o palpite do jogador
