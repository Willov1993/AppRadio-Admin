$('#data_table').DataTable({
    "destroy": true,
    "ajax": {
        "method": "GET",
        "url": "/api/usuarios",
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
        { data: "fecha_nac"},
        { data: "email"},
        { data: "rol"},
        { data: "is_active"},
        { data: "id"}
    ],
    columnDefs: [
        { width: 10, className: "text-center", targets: 0},
        { width: 200, targets: 1, render: function(data) {
            var image = '';
            if (data == null){
                image = `<img src="/static/webAdminRadio/images/generic_avatar.png" width="100%">`;
            } else {
                image = '<img src="' + data + '" width="100%">';
            }
            return image;
        }},
        { width: 250, targets: 2},
        { width: 100, targets: 3},
        { width: 250, targets: 4},
        { width: 50, targets: 5},
        { width: 100, targets: 6},
        { width: 150, className: "text-center", targets: 7, render: function(data){
            return `<a href="/webadmin/usuarios/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye"></i></a>
                    <a href="/webadmin/usuarios/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen"></i></a>
                    <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times"></i></a>
                    `
        }},
    ],
});