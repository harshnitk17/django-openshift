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
                    searching: false,
                    "ordering": false,
                    "pageLength": 25,
                    "sDom": '<"top"flp>rt<"bottom"i><"clear">',
                    drawCallback: function () {
                        $('.paginate_button', this.api().table().container())
                            .on('click', function () {
                                MathJax.typeset();
                            });
                        $('select[name=table1_length]', this.api().table().container()).on('change', function (e) {
                            MathJax.typeset();
                        });
                    },
                    columns: [
                        { data: 'id' },
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
    formsubmit();
    $('.formbtn').on('click', function (event) {
        formsubmit();

    });

    $('#clear').on('click',function(e){
        $('input[name=initial]').prop('checked', false);
        $('input[name=observable]').prop('checked', false);
        $('.box_particle button').each(function (index,element) {
            var btn_id = $(element).attr('id');
            var input_id = "#id_" + btn_id.slice(0, -3);
            var btn_selector = "#" + btn_id.slice(0, -3);
            var counter = $(input_id).val();
            if (counter != "0") {
                $(btn_selector).css({ "display": "none" });
                $(element).css({ "background-color": "#ddd", "border": "2px solid #444" });
                $(element).hover(function(){
                    $(element).css({ "background-color": "#dfd"});
                }, function(){
                    $(element).css({ "background-color": "#ddd"});
                });
                $(input_id).val("0");
            }
            
        });
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
    $('.box_particle button').click(function (e) {
        e.preventDefault();
        var btn_id = $(this).attr('id');
        var input_id = "#id_" + btn_id.slice(0, -3);
        var btn_selector = "#" + btn_id.slice(0, -3);
        var counter = $(input_id).val();
        if (counter == "0") {
            $(btn_selector).css({ "display": "block" });
            $(this).css({ "background-color": "#bfb", "border-color": "#4c4" });
            $(this).hover(function(){
                $(this).css({ "background-color": "#bfb"});
            }, function(){
                $(this).css({ "background-color": "#bfb"});
            });
            $(input_id).val("1");
            formsubmit();
        }
        else {
            $(btn_selector).css({ "display": "none" });
            $(this).css({ "background-color": "#ddd", "border": "2px solid #444" });
            $(this).hover(function(){
                $(this).css({ "background-color": "#dfd"});
            }, function(){
                $(this).css({ "background-color": "#ddd"});
            });
            $(input_id).val("0");
            formsubmit();
        }
        return false;
    });

    $(window).scroll(function () {
        if ($(this).scrollTop()) {
            $('#toTop').fadeIn();
        } else {
            $('#toTop').fadeOut();
        }
    });
    $("#toTop").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 500);
    });




});