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
                Object.keys(days).forEach((i,v)=> {

                    $('#graph').append("<p>" + i + " - " + "<span>" + days[i] + "</span>" + "</p>")
                })
                $('#counts_notes').text(data['counts-note']);
                $('.statistics_graph').show('fast');
            },

            error: function() {
                console.log('error')
            }

    })
})
