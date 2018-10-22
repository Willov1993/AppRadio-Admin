$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    getSegmentos(id_emisora);
});

function getSegmentos(emisora) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/"+ emisora +"/segmentos",
            "dataSrc": "",
            "error": function(xhr, status, error) {
                console.log("readyState: " + xhr.readyState);
                console.log("responseText: "+ xhr.responseText);
                console.log("status: " + xhr.status);
                console.log("text status: " + status);
                console.log("error: " + error);
            },
        },
        "columns": [
            { data: "id"},
            { data: "imagen"},
            { data: "nombre"},
            { data: "horarios"},
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { width: 200, targets: 1, render: function(data) {
                return '<img src="' + data + '" width="100%" >';
            }},
            { width: 250, targets: 2},
            { width: 250, targets: 3, render: function(data) {
                html = ``;
                for (var key in data){
                    html += data[key].dia + " : " + data[key].fecha_inicio + " - " + data[key].fecha_fin + "<br>";
                }
                return html;
            }},
            { width: 150, className: "text-center", targets: 4, render: function(data){
                return `<a href="/webadmin/segmentos/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye"></i></a>
                        <a href="/webadmin/segmentos/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen"></i></a>
                        <a href="#" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times"></i></a>
                        `
            }},
        ],
    });
}