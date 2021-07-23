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
    $('#Jpsi_bt').click(function () {
        var counter = $('#id_Jpsi').val();
        if (counter == "0") {
            $("#Jpsi").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Jpsi').val("1");
            formsubmit();
        }
        else {
            $("#Jpsi").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Jpsi').val("0");
            formsubmit();
        }
        return false;
    });
    $('#psi2S_bt').click(function () {
        var counter = $('#id_psi2S').val();
        if (counter == "0") {
            $("#psi2S").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_psi2S').val("1");
            formsubmit();
        }
        else {
            $("#psi2S").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_psi2S').val("0");
            formsubmit();
        }
        return false;
    });
    $('#etac_bt').click(function () {
        var counter = $('#id_etac').val();
        if (counter == "0") {
            $("#etac").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_etac').val("1");
            formsubmit();
        }
        else {
            $("#etac").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_etac').val("0");
            formsubmit();
        }
        return false;
    });
    $('#chic_bt').click(function () {
        var counter = $('#id_chic').val();
        if (counter == "0") {
            $("#chic").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_chic').val("1");
            formsubmit();
        }
        else {
            $("#chic").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_chic').val("0");
            formsubmit();
        }
        return false;
    });
    $('#ccbar_bt').click(function () {
        var counter = $('#id_ccbar').val();
        if (counter == "0") {
            $("#ccbar").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_ccbar').val("1");
            formsubmit();
        }
        else {
            $("#ccbar").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_ccbar').val("0");
            formsubmit();
        }
        return false;
    });
    $('#X3872_bt').click(function () {
        var counter = $('#id_X3872').val();
        if (counter == "0") {
            $("#X3872").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_X3872').val("1");
            formsubmit();
        }
        else {
            $("#X3872").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_X3872').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Pc_bt').click(function () {
        var counter = $('#id_Pc').val();
        if (counter == "0") {
            $("#Pc").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Pc').val("1");
            formsubmit();
        }
        else {
            $("#Pc").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Pc').val("0");
            formsubmit();
        }
        return false;
    });
    $('#XYZ_bt').click(function () {
        var counter = $('#id_XYZ').val();
        if (counter == "0") {
            $("#XYZ").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_XYZ').val("1");
            formsubmit();
        }
        else {
            $("#XYZ").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_XYZ').val("0");
            formsubmit();
        }
        return false;
    });
    $('#p_bt').click(function () {
        var counter = $('#id_p').val();
        if (counter == "0") {
            $("#p").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_p').val("1");
            formsubmit();
        }
        else {
            $("#p").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_p').val("0");
            formsubmit();
        }
        return false;
    });
    $('#n_bt').click(function () {
        var counter = $('#id_n').val();
        if (counter == "0") {
            $("#n").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_n').val("1");
            formsubmit();
        }
        else {
            $("#n").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_n').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Lambda_bt').click(function () {
        var counter = $('#id_Lambda').val();
        if (counter == "0") {
            $("#Lambda").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Lambda').val("1");
            formsubmit();
        }
        else {
            $("#Lambda").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Lambda').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Sigma_bt').click(function () {
        var counter = $('#id_Sigma').val();
        if (counter == "0") {
            $("#Sigma").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Sigma').val("1");
            formsubmit();
        }
        else {
            $("#Sigma").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Sigma').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Xi_bt').click(function () {
        var counter = $('#id_Xi').val();
        if (counter == "0") {
            $("#Xi").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Xi').val("1");
            formsubmit();
        }
        else {
            $("#Xi").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Xi').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Omega_bt').click(function () {
        var counter = $('#id_Omega').val();
        if (counter == "0") {
            $("#Omega").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Omega').val("1");
            formsubmit();
        }
        else {
            $("#Omega").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Omega').val("0");
            formsubmit();
        }
        return false;
    });
    $('#baryon_bt').click(function () {
        var counter = $('#id_baryon').val();
        if (counter == "0") {
            $("#baryon").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_baryon').val("1");
            formsubmit();
        }
        else {
            $("#baryon").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_baryon').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Lambdac_bt').click(function () {
        var counter = $('#id_Lambdac').val();
        if (counter == "0") {
            $("#Lambdac").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Lambdac').val("1");
            formsubmit();
        }
        else {
            $("#Lambdac").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Lambdac').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Sigmac_bt').click(function () {
        var counter = $('#id_Sigmac').val();
        if (counter == "0") {
            $("#Sigmac").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Sigmac').val("1");
            formsubmit();
        }
        else {
            $("#Sigmac").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Sigmac').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Xic_bt').click(function () {
        var counter = $('#id_Xic').val();
        if (counter == "0") {
            $("#Xic").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Xic').val("1");
            formsubmit();
        }
        else {
            $("#Xic").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Xic').val("0");
            formsubmit();
        }
        return false;
    });
    $('#cbaryon_bt').click(function () {
        var counter = $('#id_cbaryon').val();
        if (counter == "0") {
            $("#cbaryon").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_cbaryon').val("1");
            formsubmit();
        }
        else {
            $("#cbaryon").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_cbaryon').val("0");
            formsubmit();
        }
        return false;
    });
    $('#K_bt').click(function () {
        var counter = $('#id_K').val();
        if (counter == "0") {
            $("#K").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#K').val("1");
            formsubmit();
        }
        else {
            $("#K").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_K').val("0");
            formsubmit();
        }
        return false;
    });
    $('#K0_bt').click(function () {
        var counter = $('#id_K0').val();
        if (counter == "0") {
            $("#K0").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_K0').val("1");
            formsubmit();
        }
        else {
            $("#K0").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_K0').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Ksplus_bt').click(function () {
        var counter = $('#id_Ksplus').val();
        if (counter == "0") {
            $("#Ksplus").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Ksplus').val("1");
            formsubmit();
        }
        else {
            $("#Ksplus").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Ksplus').val("0");
            formsubmit();
        }
        return false;
    });
    $('#Ks0_bt').click(function () {
        var counter = $('#id_Ks0').val();
        if (counter == "0") {
            $("#Ks0").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_Ks0').val("1");
            formsubmit();
        }
        else {
            $("#Ks0").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_Ks0').val("0");
            formsubmit();
        }
        return false;
    });
    $('#phi_bt').click(function () {
        var counter = $('#id_phi').val();
        if (counter == "0") {
            $("#phi").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_phi').val("1");
            formsubmit();
        }
        else {
            $("#phi").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_phi').val("0");
            formsubmit();
        }
        return false;
    });
    $('#kaon_bt').click(function () {
        var counter = $('#id_kaon').val();
        if (counter == "0") {
            $("#kaon").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_kaon').val("1");
            formsubmit();
        }
        else {
            $("#kaon").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_kaon').val("0");
            formsubmit();
        }
        return false;
    });
    $('#pi_bt').click(function () {
        var counter = $('#id_pi').val();
        if (counter == "0") {
            $("#pi").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_pi').val("1");
            formsubmit();
        }
        else {
            $("#pi").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_pi').val("0");
            formsubmit();
        }
        return false;
    });
    $('#pi0_bt').click(function () {
        var counter = $('#id_pi0').val();
        if (counter == "0") {
            $("#pi0").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_pi0').val("1");
            formsubmit();
        }
        else {
            $("#pi0").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_pi0').val("0");
            formsubmit();
        }
        return false;
    });
    $('#rhoplus_bt').click(function () {
        var counter = $('#id_rhoplus').val();
        if (counter == "0") {
            $("#rhoplus").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_rhoplus').val("1");
            formsubmit();
        }
        else {
            $("#rhoplus").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_rhoplus').val("0");
            formsubmit();
        }
        return false;
    });
    $('#rho0_bt').click(function () {
        var counter = $('#id_rho0').val();
        if (counter == "0") {
            $("#rho0").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_rho0').val("1");
            formsubmit();
        }
        else {
            $("#rho0").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_rho0').val("0");
            formsubmit();
        }
        return false;
    });
    $('#eta_bt').click(function () {
        var counter = $('#id_eta').val();
        if (counter == "0") {
            $("#eta").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_eta').val("1");
            formsubmit();
        }
        else {
            $("#eta").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_eta').val("0");
            formsubmit();
        }
        return false;
    });
    $('#omega_bt').click(function () {
        var counter = $('#id_omega').val();
        if (counter == "0") {
            $("#omega").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_omega').val("1");
            formsubmit();
        }
        else {
            $("#omega").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_omega').val("0");
            formsubmit();
        }
        return false;
    });
    $('#light_bt').click(function () {
        var counter = $('#id_light').val();
        if (counter == "0") {
            $("#light").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_light').val("1");
            formsubmit();
        }
        else {
            $("#light").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_light').val("0");
            formsubmit();
        }
        return false;
    });
    $('#lepton_bt').click(function () {
        var counter = $('#id_lepton').val();
        if (counter == "0") {
            $("#lepton").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_lepton').val("1");
            formsubmit();
        }
        else {
            $("#lepton").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_lepton').val("0");
            formsubmit();
        }
        return false;
    });
    $('#photon_bt').click(function () {
        var counter = $('#id_photon').val();
        if (counter == "0") {
            $("#photon").css({ "display": "block" });
            $(this).css({ "background-color": "#bfb" });
            $('#id_photon').val("1");
            formsubmit();
        }
        else {
            $("#photon").css({ "display": "none" });
            $(this).css({ "background-color": "#ddd" });
            $('#id_photon').val("0");
            formsubmit();
        }
        return false;
    });
    
});