function buascarDados(){
$.ajax({
    url: 'http://127.0.0.1:5000/votos',
    method: 'get',
    success: function(resposta){
        let votosCp = resposta['quantVotos']
        let totalVt = resposta['quantAlunos']
        atualizaGrafico(votosCp, totalVt)
    },
})
}
function atualizaGrafico(votosCp, totalVt){
let vot = document.getElementById('vot')
let no_vot = document.getElementById('no-vot')
let ctx = document.getElementById("myChart");
let dados = {
    datasets: [{
        data: [votosCp, totalVt-votosCp],
        backgroundColor: ["rgb(121, 232, 178)", "rgb(215, 252, 236)"],
    }, ],

    labels: ["Apurados", "Não apurados"],
};

let opcoes = {
    cutoutPercentage: 40,
};

vot.innerHTML = votosCp
no_vot.innerHTML = totalVt

let meuDonutChart = new Chart(ctx, {
    type: "pie",
    data: dados,
    options: opcoes,
});
}
buascarDados()