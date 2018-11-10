let visible = false;
let id_segmento = 0;
let url = '/api/emisora/';

$(".info-segmento").hide();
$(".table-container").hide();
$(".table_lbl").hide();

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
    $(".table-container").show()
    $(".table_lbl").show();
    fillTable();

    var id_emisora = $("#emisoraSelect option:selected").val();
    id_segmento = $("#segmentoSelect option:selected").val();

    $("#segName").find('b').remove();
    $("#segSlogan i").empty();
    $("#segHorarios").find('li').remove();
    
    var seg_json;
    $.getJSON('/api/emisora/' + id_emisora + '/segmento/' + id_segmento, function (data){
        seg_json = data;
        console.log(seg_json);
        $(".image").attr('src', seg_json.imagen);
        $("#segName").html('<b>' + seg_json.nombre + '</b>');
        $("#segSlogan").html('<i class="fas fa-comment-alt icon"></i>' + seg_json.slogan);
        $.each(seg_json.horarios, function(key, val){
            $("#segHorarios").append('<li>' + this.dia + ': ' + this.fecha_inicio + ' - ' + this.fecha_fin + '</li>');
        });
    });
});

function fillTable(){
    if (!visible){
        $('#data_table').DataTable({
            "destroy": true,
            "ajax": {
                "method": "GET",
                "url": "/api/usuarios",
                "dataSrc": "",
                "error": function(xhr, status, error){
                    console.log("readyState: " + xhr.readyState);
                    console.log("responseText: " + xhr.responseText);
                    console.log("Status: " + xhr.status);
                    console.log("Text Status: " + status);
                    console.log("error: " + error);
                }
            },
            "columns": [
                { data: "id"},
                { data: "imagen"},
                { data: "username"},
                { data: function(data){
                    return data.first_name + " " + data.last_name;
                }},
                { data: "fecha_nac"},
                { data: "rol"},
                { data: "id"}
            ],
            columnDefs: [
                { width: 10, className: "text-center", targets: 0 },
                { width: 200, targets: 1, render: function(data){
                    var image = '';
                    if (data == null){
                        image = `<img src="/static/webAdminRadio/images/generic_avatar.png" width="100%">`;
                    } else {
                        image = '<img src="' + data + '" width="100%">';
                    }
                    return image;
                }},
                { width: 200, targets: 2 },
                { width: 200, targets: 3 },
                { width: 50, targets: 4 },
                { width: 10, className: "text-center", targets: 5 },
                { width: 100, targets: 6, className: "text-center", render: function(data){
                    return '<a href="#" onclick="showWarning(' + data + ')" class="btn btn-primary btn-sm" role="button">Asignar como locutor</a>'
                }}
            ]
        });
        visible = true;
        console.log("Llamada Ajax");
    }
}

function showWarning(id){
    contenedorLocutor.$data.id_locutor = id;
    contenedorLocutor.$data.id_segmento = id_segmento;
    contenedorLocutor.$data.showModal = true;
}