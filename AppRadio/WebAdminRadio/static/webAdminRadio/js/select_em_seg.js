let url = '/api/emisora/';

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