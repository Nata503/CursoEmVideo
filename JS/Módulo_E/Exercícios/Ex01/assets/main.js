function contagem() {
    var inicio = Number(document.getElementById('numInicio').value)
    var fim = Number(document.getElementById('numFim').value)
    var passo = Number(document.getElementById('numPasso').value)
    var msg = document.getElementById('msg')

    if (isNaN(inicio) || isNaN(fim) || isNaN(passo)) {
        alert('Por favor, preencha todos os campos corretamente!')
        msg.innerHTML = 'Impossível contar.'
        return
    }

    if (passo <= 0) {
        alert('Passo inválido! Considerando passo 1.')
        passo = 1
    }

    msg.innerHTML = 'Contando: <br>'

    if (inicio < fim) {
        // Contagem crescente
        for (let n = inicio; n <= fim; n += passo) {
            msg.innerHTML += `${n} \u{1F449} `
        }
    } else {
        // Contagem regressiva
        for (let n = inicio; n >= fim; n -= passo) {
            msg.innerHTML += `${n} \u{1F449} `
        }
    }

    msg.innerHTML += `\u{1F3C1}` // Bandeira de chegada
}



