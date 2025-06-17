function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')

    if (fano.value.length = 0 || Number(fano.value) > ano) {
        alert('[ERRO] verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gênero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked){
            gênero = 'Homem'
            if(idade >= 0 && idade < 10){
                img.setAttribute('src', './image/bebe-m.png')
            } else if(idade < 21){
                img.setAttribute('src', './image/jovem-m.png')
            } else if(idade < 50) {
                img.setAttribute('src', './image/adulto-m.png')
            } else {
                img.setAttribute('src', './image/idoso-m.png')
            }
        } else if (fsex[1].checked){
            gênero = 'Mullher'
            if(idade >= 0 && idade < 10){
                img.setAttribute('src', './image/bebe-f.png')
            } else if(idade >= 10 && idade < 21){
                img.setAttribute('src', './image/jovem-f.png')
            } else if(idade < 50) {
                img.setAttribute('src', './image/adulto-f.png')
            } else {
                img.setAttribute('src', './image/idosa-f.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`
        res.appendChild(img)
        img.style.padding = '10px'
    }
}