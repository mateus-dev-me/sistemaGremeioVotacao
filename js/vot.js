let response = fetch('http://localhost:8000/votos', {method: 'get'})



let votosCp = 4;
let totalVt = 40;
let ctx = document.getElementById("myChart");
let dados = {
    datasets: [{
        data: [votosCp, totalVt],
        backgroundColor: ["rgb(121, 232, 178)", "rgb(215, 252, 236)"],
    }, ],

    labels: ["Apurados", "Não apurados"],
};

let opcoes = {
    cutoutPercentage: 40,
};

let meuDonutChart = new Chart(ctx, {
    type: "pie",
    data: dados,
    options: opcoes,
});