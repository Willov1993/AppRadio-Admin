$("#segmentoSelect").change(function () {
    var id_segmento = $("#segmentoSelect option:selected").val();
    getSegmentos(id_segmento);
});

function getSegmentos(segmento) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/segmento/"+ segmento +"/locutores",
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
            { data: function(data){
                return data.first_name + " " + data.last_name;
            }},
            { data: "emisora"},
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, className: "text-center", targets: 0},
            { width: 200, targets: 1, render: function(data) {
                return '<img src="' + data + '" width="100%">';
            }},
            { width: 250, targets: 2},
            { width: 250, targets: 3},
            { width: 150, className: "text-center", targets: 4, render: function(data){
                return `<a href="/webadmin/locutores/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye"></i></a>
                        <a href="/webadmin/locutores/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times"></i></a>
                        `
            }},
        ],
    });
}