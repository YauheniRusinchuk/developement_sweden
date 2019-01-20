$(function(){

    let path = window.document.location.href + 'result/'

    $.ajax(
        {
            type:"GET",
            url: path,
            data:{

            },
            success: function(data){
                console.log(data)
            },

            error: function() {
                console.log('error')
            }

    })
})
