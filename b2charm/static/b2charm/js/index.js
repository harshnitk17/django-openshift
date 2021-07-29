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
    $('.box_particle button').click(function () {
        var btn_id = $(this).attr('id');
        var input_id = "#id_"+btn_id.slice(0,-3);
        var btn_selector = "#"+btn_id.slice(0,-3);
        var counter = $(input_id).val();
        if (counter == "0") {
            $(btn_selector).css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $(input_id).val("1");
            formsubmit();
        }
        else {
            $(btn_selector).css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $(input_id).val("0");
            formsubmit();
        }
        return false;
    });
    
});