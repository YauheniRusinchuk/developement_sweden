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
                $('.seccess_form').show('fast', ()=>{
                    setTimeout(()=>{
                        $('.seccess_form').hide('fast', ()=>{
                            window.location.href = window.location.origin + "/login"
                        });
                    }, 2000)
                })
            },


            error: function() {
                $('.error_form').show('fast', ()=>{
                    setTimeout(()=>{
                        $('.error_form').hide('fast');
                    }, 2000)
                })
            }




        })



    })

})
