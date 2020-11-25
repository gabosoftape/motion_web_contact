
function isPostPossible(){
    var status = false;
    var data = $('#contact_form').serializeArray();
    var nombre = false;
    var token = false;
    var telefono = false;
    var asunto = false;
    var solicitud = false;
    var email = false;
    var empresa = false;
    var medio = false;
    var state = 'nuevo';
    // revisamos si viene algun dato nulo y aprovechamos para clasificar la info
    $.each( data, function( name, value ) {
      switch(value.name){
        case 'csrf_token':
            token = value.value;
            break;
        case 'nombre':
            nombre = value.value;
            break;
        case 'telefono':
            telefono = value.value;
            break;
        case 'asunto':
            asunto  = value.value;
            break;
        case 'solicitud':
            solicitud = value.value;
            break;
        case 'email':
            email = value.value;
            break;
        case 'empresa':
            empresa = value.value;
            break;
        case 'medio':
            medio = value.value;
            break;
        default:
            console.log('is otro dato');
            break;
      }
    });
    // si almenos contiene nombre, telefono, asunto , solicitud y email posteamos, si no deshabilitamos el boton, hasta que sea posible.
    if(nombre && telefono && asunto && solicitud && email){
         // se puede postear en esta accion
        $('#btn_enviar').prop('disabled', false); //TO DISABLED
        $('#btn_enviar').removeClass('button-active2').addClass('button-active1');
        $('#btn_enviar').trigger("change");
        console.log('algun dato vacio');
        status = true;
    }else{
        // ya no se puede postear mas
        $('#btn_enviar').prop('disabled', true); //TO DISABLED
        $('#btn_enviar').removeClass('button-active1').addClass('button-active2');
        $('#btn_enviar').trigger("change");
        console.log('algun dato vacio');
        // deshabilitamos boton.
        // cada que cambie un input verificamos que se pueda postear
    }
}

function postNewContact(){
    var data = $('#contact_form').serializeArray();
    var nombre = $('#nombreIn').val();
    var token = $('#tokenIn').val();
    var telefono = $('#telefonoIn').val();
    var asunto = $('#asuntoIn').val();
    var solicitud = $('#solicitudIn').val();
    var email = $('#emailIn').val();
    var empresa = $('#empresaIn').val();
    var medio = 'sw';
    var state = 'nuevo';

    var dataContact = {
        'nombre': nombre,
        'telefono': telefono,
        'asunto': asunto,
        'solicitud': solicitud,
        'email': email,
        'empresa': empresa,
        'medio': medio,
        'state': state,
        'token': token,
    }
    // si almenos contiene nombre, telefono, asunto , solicitud y email posteamos, si no deshabilitamos el boton, hasta que sea posible.
    if(nombre && telefono && asunto && solicitud && email){
         // se puede postear en esta accion
        $.ajax({
            type: "POST",
            url: "/contacto/new",
            data: dataContact,
            success: function(blob, status, xhr) {
                // check for a filename
                console.log('este es el size del blob');
                console.log(blob);
            }
        });

    }else{
        // ya no se puede postear mas
        $('#btn_enviar').prop('disabled', true); //TO DISABLED
        $('#btn_enviar').trigger("change");
        console.log('algun dato vacio');
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'No puedes generar el informe, dejaste algun campo importante vacio!. Verifica la informacion e intenta de nuevo.',
        });
        // deshabilitamos boton.
        // cada que cambie un input verificamos que se pueda postear
    }
}

$( document ).ready(function() {
    isPostPossible();
    $('#btn_enviar').click(function(){
        console.log('Se hizo click en el boton mdfkr');
        postNewContact();
    });
    $('#nombreIn').on('change', function() {
       isPostPossible();
    });
    $('#tokenIn').on('change', function() {
       isPostPossible();
    });
    $('#telefonoIn').on('change', function() {
       isPostPossible();
    });
    $('#asuntoIn').on('change', function() {
       isPostPossible();
    });
    $('#solicitudIn').on('change', function() {
       isPostPossible();
    });
    $('#emailIn').on('change', function() {
       isPostPossible();
    });
    $('#empresaIn').on('change', function() {
       isPostPossible();
    });
});