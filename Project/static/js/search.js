$(document).ready(function () {
    $('.voteIcon1').on('click',function (event) {
        let value = $('img.voteIcon1').attr('src')
        let data = 1
        $.ajax({
            url: "/vote/1",
            type: "POST",
            data: data,
            processData: false,
            contentType: false,
            statusCode: {
                404: function (event) {
                    console.log('La URL solicitada no existe, solicitud no enviada.')
                },
                200: function () {
                    console.log('URL encontrada, solicitud enviada.')
                },
                500: function () {
                    console.log('Error interno del servidor, solicitud no enviada.')
                }
            },
            success: function (status) {
                if (status == 'ok') {
                    let voteStatus = localStorage.getItem('voto');
                    if (value === '../../static/icons/heartEmpty.svg'){
                        $('.voteIcon1').attr('src','../../static/icons/heartBlack.svg')
                        localStorage.setItem('voto', '1');
                    } else if (value === '../../static/icons/heartBlack.svg') {
                        $('.voteIcon1').attr('src','../../static/icons/heartEmpty.svg')
                        localStorage.setItem('voto', '0');
                    }
                }
                else {
                }
            }
        })
    })

    $('.downloadIcon1').on('click', function (event) {
        let value = $('img.downloadIcon1').attr('src')
        let data = 1
        $.ajax({
            url: "/download/1",
            type: "POST",
            data: data,
            processData: false,
            contentType: false,
            statusCode: {
                404: function (event) {
                    console.log('La URL solicitada no existe, solicitud no enviada.')
                },
                200: function () {
                    console.log('URL encontrada, solicitud enviada.')
                },
                500: function () {
                    console.log('Error interno del servidor, solicitud no enviada.')
                }
            },
            success: function (status) {
                if (status == 'ok') {
                    console.log('ok descarga')
                }
                else {
                }
            }
        })
    })


})