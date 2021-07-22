$(document).ready(function () {
    function formsubmit() {
        $("#filter_form").submit(function (e) {
            return false;
        });
        var serializedData = $('#filter_form').serialize();
        $.ajax({
            url: "/index/post/ajax/filter",
            type: "POST",
            data: serializedData,
            success: function (json_response) {
                globalThis.table = $('#table1').DataTable({
                    data: JSON.parse(json_response),
                    responsive: true,
                    bDestroy: true,
                    "sDom": '<"top"flp>rt<"bottom"i><"clear">',
                    drawCallback: function () {
                        $('.paginate_button', this.api().table().container())
                            .on('click', function () {
                                MathJax.typeset();
                            });
                    },
                    columns: [
                        { data: 'id'},
                        { data: 'latex' },
                        { data: 'value' },
                        {
                            "data": "id", "name": "id",
                            fnCreatedCell: function (nTd, sData, oData, iRow, iCol) {
                                if (oData.id) {
                                    $(nTd).html("<a target='_blank' href='detail/" + oData.id + "'>" + "Detail" + "</a>");
                                }
                            }
                        }

                    ],
                    'columnDefs': [
                        {
                           'targets': 0,
                           'checkboxes': {
                              'selectRow': true
                           }
                        }
                     ],
                     'select': {
                        'style': 'multi'
                     },
                     'order': [[2, 'asc']]

                });
                MathJax.typeset();
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });


    }
    $('.formbtn').on('click', function (event) {
        formsubmit();

    });

    $('#btnini').on('click', function (event) {
        $('input[name=initial]').prop('checked', false);
        formsubmit();
    });

    $('#btnobs').on('click', function (event) {
        $('input[name=observable]').prop('checked', false);
        formsubmit();
    });
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        formsubmit();

    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        formsubmit();

    });
    $('#D0_bt').click(function () {
        var counter = $('#id_D0').val();
        if (counter == "0") {
            $("#D0").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_D0').val("1");
            formsubmit();
        }
        else {
            $("#D0").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_D0').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Dplus_bt').click(function () {
        var counter = $('#id_Dplus').val();
        if (counter == "0") {
            $("#Dplus").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Dplus').val("1");
            formsubmit();
        }
        else {
            $("#Dplus").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Dplus').val("0");
            formsubmit();
        }
        return false;
    }); $('#Ds_bt').click(function () {
        var counter = $('#id_Ds').val();
        if (counter == "0") {
            $("#Ds").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Ds').val("1");
            formsubmit();
        }
        else {
            $("#Ds").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Ds').val("0");
            formsubmit();
        }
        return false;
    }); $('#Ds0_bt').click(function () {
        var counter = $('#id_Ds0').val();
        if (counter == "0") {
            $("#Ds0").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Ds0').val("1");
            formsubmit();
        }
        else {
            $("#Ds0").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Ds0').val("0");
            formsubmit();
        }
        return false;
    }); $('#Dsplus_bt').click(function () {
        var counter = $('#id_Dsplus').val();
        if (counter == "0") {
            $("#Dsplus").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Dsplus').val("1");
            formsubmit();
        }
        else {
            $("#Dsplus").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Dsplus').val("0");
            formsubmit();
        }
        return false;
    }); $('#Dss_bt').click(function () {
        var counter = $('#id_Dss').val();
        if (counter == "0") {
            $("#Dss").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Dss').val("1");
            formsubmit();
        }
        else {
            $("#Dss").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Dss').val("0");
            formsubmit();
        }
        return false;
    }); $('#Dsss_bt').click(function () {
        var counter = $('#id_Dsss').val();
        if (counter == "0") {
            $("#Dsss").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Dsss').val("1");
            formsubmit();
        }
        else {
            $("#Dsss").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Dsss').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Dssss_bt').click(function () {
        var counter = $('#id_Dssss').val();
        if (counter == "0") {
            $("#Dssss").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Dssss').val("1");
            formsubmit();
        }
        else {
            $("#Dssss").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Dssss').val("0");
            formsubmit();
        }
        return false;
    });
    
});