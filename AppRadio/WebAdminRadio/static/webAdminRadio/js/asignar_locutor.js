let url = '/api/emisora/';

$(".info-segmento").hide();

$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    var segmento_select = $('#segmentoSelect');

    segmento_select.find('option').remove();
    segmento_select.append('<option selected="true" disabled>Elija un segmento</option>');
    segmento_select.prop('selectedIndex', 0);

    $.getJSON(url + id_emisora + '/segmentos', function(data){
        $.each(data, function(key, entry){
            segmento_select.append($('<option></option>').attr('value', entry.id).text(entry.nombre));
        })
    })
});

$("#segmentoSelect").change(function () {
    $(".info-segmento").show();

    var id_emisora = $("#emisoraSelect option:selected").val();
    var id_segmento = $("#segmentoSelect option:selected").val();

    $("#segName").find('b').remove();
    $("#segSlogan i").empty();
    $("#segHorarios").find('li').remove();
    
    var seg_json;
    $.getJSON('/api/emisora/' + id_emisora + '/segmento/' + id_segmento, function (data){
        seg_json = data;
        $(".image").attr('src', seg_json.imagen);
        $("#segName").html('<b>' + seg_json.nombre + '</b>');
        $("#segSlogan").html('<i class="fas fa-comment-alt icon"></i>' + seg_json.slogan);
        $.each(seg_json.horarios, function(key, val){
            $("#segHorarios").append('<li>' + this.dia + ': ' + this.fecha_inicio + ' - ' + this.fecha_fin + '</li>');
        });
    })

})