let listaInscritos = [];

listaInscritos.push("João Silva");
listaInscritos.push("Maria Santos");
listaInscritos.push("Pedro Almeida");

console.log("Lista inicial:", listaInscritos);
console.log("Quantidade de inscritos:", listaInscritos.length);

console.log("Antes de adicionar Ana Pereira:", listaInscritos);
listaInscritos.push("Ana Pereira");
console.log("Depois de adicionar Ana Pereira:", listaInscritos);

console.log("Antes de adicionar Carlos Mendes:", listaInscritos);
listaInscritos.unshift("Carlos Mendes");
console.log("Depois de adicionar Carlos Mendes:", listaInscritos);

let removerUltimo = listaInscritos.pop();
console.log("Participante removido (último):", removerUltimo);
console.log("Lista após remoção do último:", listaInscritos);

let removerPrimeiro = listaInscritos.shift();
console.log("Participante removido (primeiro):", removerPrimeiro);
console.log("Lista após remoção do primeiro:", listaInscritos);

console.log("Antes da ordenação alfabética:", listaInscritos);
listaInscritos.sort();
console.log("Depois da ordenação alfabética:", listaInscritos);