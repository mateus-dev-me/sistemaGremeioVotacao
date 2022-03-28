const prevent = document.querySelectorAll("[required]");
function validate(event) {
    event.preventDefault();
}
for (preventerror of prevent) {
    preventerror.addEventListener("invalid", validate);
}
function logar(){
    let matricula = document.getElementById('matricula').value
    let senha = document.getElementById('senha').value
    let urle = 'http://127.0.0.1:5000/login?matricula='+matricula+'&senha='+senha
    $.ajax({
        url: urle,
        method: 'post',
        success: function(resposta){
            if(resposta['status']==2){
                window.alert('Matrícula e/ou senha inválidas')
            }

            redirect(resposta['ID_aluno'])
            
        },
    })
}
function redirect(resposta){
    console.log(resposta)
    window.alert('sjdd')
}