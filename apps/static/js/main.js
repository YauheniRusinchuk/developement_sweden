$(function(){
        $.uploadPreview({
            input_field: "#image-upload",   // Default: .image-upload
            preview_box: "#image-preview",  // Default: .image-preview
            label_field: "#image-label",    // Default: .image-label
            label_default: "Choose File",   // Default: Choose File
            label_selected: "Change File",  // Default: Change File
            no_label: false                 // Default: false
        });


    $('.btn_subscriptions').click((e)=> {
        e.preventDefault();
        $('.post_container').hide();
        $('.not_articles').hide()
        $('.detail_profile_sub').show();
    })

    $('.btn_posts').click((e)=>{
        e.preventDefault();
        $('.detail_profile_sub').hide();
        $('.not_articles').show();
        $('.post_container').show();
    })

});
