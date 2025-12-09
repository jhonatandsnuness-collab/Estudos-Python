const form = document.getElementById("formulario");
const resultado = document.getElementById("resultado");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    let nome = document.getElementById("nome").value.trim();
    let idade = Number(document.getElementById("idade").value);

    // === VALIDAÇÃO === 

    if (nome === "") {
    alert("O nome é obrigatório");
    return;
    }

    if (idade <= 0 || isNaN(idade)) {
    alert("Digire uma idade válida!");
    return;
    }

    // === EXIBE RESULTADO ===
    resultado.style.display = "block";
    resultado.innerHTML = '<strong>Dados Recebidos:</strong><br>Nome: ${nome}<br>Idade: ${idade}';
});

// const notas = [80, 55, 90, 72, 60, 88];

// notas.sort((a, b) => a - b);

// const vagas = 3;
// const notaDeCorte = notas[vagas - 1];

// console.log("Nota de corte:", notaDeCorte);

// const soma = notas.reduce((total, n) => total + n, 0);
// const media = soma / notas.length;
// console.log("Média:", media);
