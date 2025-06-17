function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()

    msg.innerHTML = `Agora são ${hora} horas`
    if (hora >= 0 && hora < 12) {
        img.src = "./image/bgmanha.png"
        document.body.style.backgroundColor = '#947464'

    } else if(hora >= 12 && hora <= 18){
        img.src = "./image/bgtarde.png"
        document.body.style.backgroundColor = '#ce973c'
    } else {
        img.src = "./image/bgnoite.png"
        document.body.style.backgroundColor = '#424567'
    }
}