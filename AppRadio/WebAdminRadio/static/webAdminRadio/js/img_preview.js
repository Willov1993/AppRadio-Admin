function previewImg(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(data){
            $('#preview').attr('src', data.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$('#imgSegmento').change(function(){
    previewImg(this);
})