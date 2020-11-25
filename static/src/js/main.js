function createContactMsg(){
    var data = $('#excelOptions').serializeArray();
    var units = false;
    var drivers = false;
    var status = '';
    var fecha_ini = false;
    var fecha_end = false;
    var token = '';
    var void_flag = false;
    // revisamos si viene algun dato nulo y aprovechamos para clasificar la info
    $.each( data, function( name, value ) {
      switch(value.name){
        case 'csrf_token':
            token = value.value;
            break;
        case 'estado':
            status = value.value;
            break;
        case 'date_ini':
            fecha_ini = value.value;
            if(fecha_ini){
                console.log('la fecha inicial viene con info');
                void_flag = false;
            }else{
                console.log('la fecha inicial viene sin info');
                void_flag = true;
            }
            break;
        case 'date_end':
            fecha_end  = value.value;
            if(fecha_end){
                console.log('la fecha final viene con info');
                void_flag = false;
            }else{
                console.log('la fecha final viene sin info');
                void_flag = true;
            }
            break;
        case 'unidadesarray[]':
            var a = value.value;
            if(a){
                console.log('las unidades vienen con informacion');
            }else{
                console.log('las unidades vienen sin info');
                void_flag = true;
                break;
            }
            var b = a.split(',').map(function(item) {
                return parseInt(item, 10);
            });
            units = b;
            break;
        case 'conductoresarray[]':
            var a = value.value;
            if(a){
                console.log('los conductores vienen con informacion');
                // pregunto si el flag esta arriba .. si el flag esta arriba y las fechas tienen informacion igual lo dejamos pasar
                if (date_ini && date_end && void_flag){
                    //dejalo pasar porque aunque las unidades estan vacias pero los conductores traen informacion
                    void_flag = false; //solo decimos que no esta vacio ningun item. aunque las unidades lo esten.. solo por verificar el siguiente item.
                }
            }else{
                console.log('los conductores vienen sin info');
                // si las unidades tienen informacion pasamos, si no .. paila.
                if (date_ini && date_end && !void_flag){
                    //dejalo pasar porque aunque los conductores estan vacios pero la unidades traen informacion
                    void_flag = false;
                    break;
                }else{
                    void_flag = true;
                    break;
                }

            }
            var b = a.split(',').map(function(item) {
                return parseInt(item, 10);
            });
            drivers = b;
            break;
        default:
            console.log('is otro dato');
            break;
      }
    });
    var options = {
            'model': 'wizard.enlist.history',
            'unidades': units,
            'conductores': drivers,
            'fecha_ini': fecha_ini,
            'fecha_end': fecha_end,
            'status': status,
        }
    var posting_data = {
            'model': 'wizard.enlist.history',
            'options': JSON.stringify(options),
            'output_format': 'xlsx',
            'report_name': 'Historial de alistamientos',
            'token': token,
             }
    var jsonstr = posting_data;
    if(fecha_ini && fecha_end && units){
        console.log('Se encontraron valores para fecha inicial, fecha final y unidades..');
        getReport(jsonstr);
    }else if(fecha_ini && fecha_end && drivers){
        console.log('Se encontraron valores para fecha inicial, fecha final y conductores..');
        getReport(jsonstr);
    }else {
        console.log("algun dato esta vacio porque el flag es true");
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'No puedes generar el informe, dejaste algun campo importante vacio!. Verifica la informacion e intenta de nuevo.',
        });

    }
    console.log(jsonstr);
}

function getReport(data){
    $.ajax({
            type: "POST",
            url: "/xlsx_reports",
            data: data,
            xhrFields: {
                responseType: 'blob' // to avoid binary data being mangled on charset conversion
            },
            success: function(blob, status, xhr) {
                // check for a filename
                console.log('este es el size del blob');
                console.log(blob);
                var filename = "Historial de alistamientos";
                var disposition = xhr.getResponseHeader('Content-Disposition');
                if (disposition && disposition.indexOf('attachment') !== -1) {
                    var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                    var matches = filenameRegex.exec(disposition);
                    if (matches != null && matches[1]) filename = matches[1].replace(/['"]/g, '');
                }

                if (typeof window.navigator.msSaveBlob !== 'undefined') {
                    // IE workaround for "HTML7007: One or more blob URLs were revoked by closing the blob for which they were created. These URLs will no longer resolve as the data backing the URL has been freed."
                    window.navigator.msSaveBlob(blob, filename);
                } else {
                    var URL = window.URL || window.webkitURL;
                    //var downloadUrl = URL.createObjectURL(blob);
                    var downloadUrl = URL.createObjectURL(blob);
                    console.log(downloadUrl);
                    if (filename) {
                        // use HTML5 a[download] attribute to specify filename
                        var a = document.createElement("a");
                        // safari doesn't support this yet
                        if (typeof a.download === 'undefined') {
                            window.location.href = downloadUrl;
                        } else {
                            a.href = downloadUrl;
                            a.download = filename;
                            document.body.appendChild(a);
                            a.click();
                        }
                    } else {
                        window.location.href = downloadUrl;
                    }

                    setTimeout(function () { URL.revokeObjectURL(downloadUrl); }, 100); // cleanup
                }
            }
        });
}

function canipost(){
    //obtengo los elementos del formulario
    if($("#unidadesinput").val() || $("#conductoresinput").val()){
        if($("#date_ini").val() && $("#date_end").val()){
            $('#createxcelbtn').prop('disabled', false); //TO ENABLE
            $('#createxcelbtn').trigger("change");
            createExcel();
        }else{
            $('#createxcelbtn').prop('disabled', true); //TO DISABLED
            $('#createxcelbtn').trigger("change");
            console.log('algun dato vacio');
        }

    }

}

$( document ).ready(function() {

    $('.js-example-basic-multiple').select2();
    // funcion para obtener los conductores del select multiple y colocarlos en un input hidden.
    //console.log(valores);
    // funcion para obtener los responsables del select multiple y colocarlos en un input hidden.
    $('#date_ini').on('change', function() {

    });
    $('#date_end').on('change', function() {

    });
    var unitsSelect = [];
    $('#selectpickerUnidades').on('change', function() {
        //alert( $(this).val() );

        $("#unidadesinput").val('');
        unitsSelect = [];
        unitsSelect.push($(this).val());
        $("#unidadesinput").val(unitsSelect);
    });
    var driversSelect = [];
    $('#selectpickerConductores').on('change', function() {
        //alert( $(this).val() );

        $("#conductoresinput").val('');
        driversSelect = [];
        driversSelect.push($(this).val());
        $("#conductoresinput").val(driversSelect);
    });
    $('#select_all_units').click(function() {
        $('#selectpickerUnidades option').prop('selected', true);
        $("#unidadesinput").val('');
        unitsSelect = [];
        unitsSelect.push($('#selectpickerUnidades').val());
        $("#unidadesinput").val(unitsSelect);
        $("#selectpickerUnidades").trigger("change");
    });
    $('#select_all_drivers').click(function() {
        $('#selectpickerConductores option').prop('selected', true);
        $("#conductoresinput").val('');
        driversSelect = [];
        driversSelect.push($('#selectpickerConductores').val());
        $("#conductoresinput").val(driversSelect);
        $("#selectpickerConductores").trigger("change");
    });
    $('#deselect_all_units').click(function() {
        $('#selectpickerUnidades option').prop('selected', false);
        $("#unidadesinput").val('');
        unitsSelect = [];
        unitsSelect.push($('#selectpickerUnidades').val());
        $("#unidadesinput").val(unitsSelect);
        $("#selectpickerUnidades").trigger("change");
    });
    $('#deselect_all_drivers').click(function() {
        $('#selectpickerConductores option').prop('selected', false);
        $("#conductoresinput").val('');
        driversSelect = [];
        driversSelect.push($('#selectpickerConductores').val());
        $("#conductoresinput").val(driversSelect);
        $("#selectpickerConductores").trigger("change");
    });
    $('#btn_enviar').click(function(){
        console.log('Se hizo click en el boton mdfkr');
        createContactMsg();
    });
});