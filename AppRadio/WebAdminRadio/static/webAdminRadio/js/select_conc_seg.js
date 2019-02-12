let url = '/api/emisora/';
moment.locale('es');

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
    var id_segmento = $('#segmentoSelect option:selected').val();
    fillTable(id_segmento);
})

function fillTable(segmento) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/segmentos/" + segmento + "/encuestas",
            "dataSrc": "",
            "error": function(xhr, status, error){
                console.log("readyState: " + xhr.readyState);
                console.log("responseText: " + xhr.responseText);
                console.log("Status: " + xhr.status);
                console.log("Text Status: " + status);
                console.log("error: " + error);
            },
        },
        "columns": [
            { data: "id" },
            { data: "titulo" },
            { data: function (data) {
                var time = moment(data);
                moment.locale('es');
                time.locale(false);
                return time.format("YYYY-MM-DD, HH:MM:SS");
            }},
            { data: function(data){
                return data.dia_fin + ", " + data.hora_fin;
            }},
            { data: "activo"},
            { data: "id" }
        ],
        columnDefs: [
            { width: 10, className: "text-center", targets: 0 },
            { width: 500, targets: 1 },
            { width: 200, targets: 2 },
            { width: 200, targets: 3 },
            { witdh: 10, className: "text-center", targets: 4 },
            { width: 150, targets: 5, className: "text-center", render: function(data){
                return `<a href="/webadmin/concursos/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye"></i></a>
                        <a href="/webadmin/concursos/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times"></i></a>
                        `
            }}
        ]
    });
};