function getFrecuencias(publicidad) {
    console.log("/api/publicidad/"+ publicidad + "/frecuencias");
    console.log($('#table_frecuencias').length);
    $('#table_frecuencias').DataTable({
        "destroy": true,
        "bPaginate": false,
        "bLengthChange": false,
        "bFilter": true,
        "bInfo": false,
        "bAutoWidth": false,
        "searching": false,
        "ajax": {
            "method": "GET",
            "url": "/api/publicidad/"+ publicidad + "/frecuencias",
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
            { data: "tipo"},
            { data: "dia_semana"},
            { data: "hora_inicio"},            
            { data: "hora_fin"}
        ],
        columnDefs: [
            { width: 150, targets: 0},
            { width: 250, targets: 1},
            { width: 100, targets: 2},
            { width: 200, targets: 3},
        ],
    });
}
