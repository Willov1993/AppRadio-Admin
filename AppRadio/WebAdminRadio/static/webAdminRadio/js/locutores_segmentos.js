$('#emisoraSelect').on('change', function(){
    // Habilitar los SelectBox para segmentos y el botón de agregar
    $('#segmentoSelect').removeAttr('disabled');
    $('#btn_agregar').removeAttr('disabled');
    var id_emisora = this.value;

    // Llenando el SelectBox de segmentos con los programas de la emisora seleccionada
    $.getJSON("/api/" + id_emisora + "/segmentos", function(data){
        $.each(data, function(key, val){
            console.log(key + ": " + val)
        });
    });
})