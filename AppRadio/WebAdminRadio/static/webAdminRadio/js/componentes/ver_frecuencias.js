function getFrecuencias(publicidad) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/publicidad/"+ publicidad +"/frecuencias",
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
            { data: "tipo"},
            { data: "dia_semana"},
            { data: "hora_inicio"},            
            { data: "hora_fin"}
        ],
        columnDefs: [
            { width: 150, targets: 0},
            { width: 150, targets: 1},
            { width: 250, targets: 2},
            { width: 100, targets: 3},
            { width: 200, targets: 4},            
        ],
    });
}
