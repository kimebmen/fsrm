$('#myTable').DataTable({
    pageLength: 10,
    ajax: "/data",
    columns: [
        { data: 0 },
        { data: 1 },
        { data: 2 },
    ]
});
