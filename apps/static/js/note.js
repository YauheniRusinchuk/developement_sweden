$(function(){


    $(".datetime").datepicker();



    $('.btn_show_form').click((e)=>{
        e.preventDefault();
        $('.form_note').show('fast');
    })

    $('.btn_hide_form').click((e)=>{
        e.preventDefault();
        $('.form_note').hide('fast');
    })

    



});
