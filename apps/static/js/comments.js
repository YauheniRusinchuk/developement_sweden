$(function(){

    $('#btn_edit_comment').click((e)=> {
        e.preventDefault();
        $('.open_form_edit').show('fast');
    })

    $('#close_form').click((e)=>{
        e.preventDefault();
        $('.form_new_comment')[0].reset();
        $('.open_form_edit').hide('fast');
    })

});
