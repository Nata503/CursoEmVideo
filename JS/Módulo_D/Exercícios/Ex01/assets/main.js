function contagem(){
    var inicio = Number(document.getElementById('numInicio').value)
    var fim = Number(document.getElementById('numFim').value)
    var passo = Number(document.getElementById('numPasso').value)
    var msg = document.getElementById('msg')

    if (inicio <= 0 || fim <= 0 || passo <= 0 || inicio >= fim){
        alert('Esse número É invalido')
        return
    }

        for(var n = inicio; n <= fim; n += passo ){
            msg.innerHTML += `Estamos no passo ${n}<br>`
    }return}
