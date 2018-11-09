//id del comboboxxxx
$("#segmentoSelect").change(function () {
    var id_segmento = $("#segmentoSelect option:selected").val();
    getPublicidad(id_segmento);
});

function getPublicidad(segmento) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/segmento/"+ segmento +"/publicidad",
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
            { data: "titulo"},
            { data: "cliente"},            
            { data: "emisora"},
            { data: "frecuencia"},            
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { width: 150, targets: 1, render: function(data) {
                return '<img src="' + data + '" width="100%" >';
            }},
            { width: 250, targets: 2},
            { width: 100, targets: 3},
            { width: 200, targets: 4},            
            { width: 80, className: "text-center", targets:5 , render: function(data){
                return `<a href="api/publicidad" + publicidad + "/frecuencias/"` + data + `" class="btn btn-primary btn-md ml-auto action" role="button">Ver frecuencias</i></a>
                        `
            }},                    
            { width: 150, className: "text-center", targets: 6, render: function(data){
                return `<a href="/webadmin/publicidad/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye"></i></a>
                        <a href="/webadmin/publicidad/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times"></i></a>
                        `
            }},
        ],
    });
}