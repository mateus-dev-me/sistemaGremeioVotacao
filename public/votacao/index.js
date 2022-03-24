function fazGet(url){
    let request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send()
    return request.responseText
}

function criaLinha(usuario){

}

function main(){
    usuarios = fazGet('http://127.0.0.1:8000/nao')
    console.log(usuarios)
}

main()