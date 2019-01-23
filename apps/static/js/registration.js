$(function(){


    $('.form_registation').on('submit',(e)=>{
        e.preventDefault();
        console.log("CLICK REGISTATION FORM")

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: {
                username : $('.registration_username_form').val(),
                firstname : $('.registration_firstname_form').val(),
                lastname : $('.registration_last_form').val(),
                password : $('.registration_password_form').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },

            success: function(res) {
                $('.seccess_form').show('fast')
            },


            error: function() {
                console.log("Error ...")
            }




        })



    })

})
