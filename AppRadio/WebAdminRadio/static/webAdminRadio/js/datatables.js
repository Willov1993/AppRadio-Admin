$(document).ready( function () {
    $('#data_table').DataTable({
        columnDefs: [
            { width: 10, targets: 0},
            { width: 150, targets: 1 },
            { width: 150, targets: 5},
        ],
    });
} );