$(function(){

    let path = window.document.location.href + 'result/'

    $.ajax(
        {
            type:"GET",
            url: path,
            data:{

            },
            success: function(data){
                let days = data['Days'];
                console.log(days)
                $('#counts_notes').text(data['counts-note']);
                $('.statistics_graph').show('fast');
            },

            error: function() {
                console.log('error')
            }

    })
})
