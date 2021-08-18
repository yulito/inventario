$(document).ready(function(){
    agregarUsuario();
    
});

$("#CancelarUsuario").click(function(jqXHR){
    alert('Estoy en Cancelar')
    
})

function agregarUsuario(){
    $("#btAgregarUsuario").click(function(e){
        $(".frmUsuario").trigger('reset');    //RECUERDA QUE LA FUNCION TRIGGER FUNCIONA CUANDO ES UN SERIALIZERARRAY
        $("#modalUsuario").modal('show');
        $("#guardarCambios").remove();
    })
}

$("#GuardarUsuario").click(function(jqXHR){
    $("#modalUsuario").modal('toggle'); 
    var stDatos = $('.frmUsuario').serializeArray();
    console.log(stDatos)
    $.ajax({
        type:'POST',
        url: 'crearUsuario',
        data: stDatos,
        success: function (data){
            console.log(data)                
            $('tbody').append(
            '<tr>'
            +   '<th scope="row">'+ data.user.rut +'</th>'
            +   '<td>'+ data.user.nombre +'</td>'
            +   '<td>'+ data.user.apePa +'</td>'
            +   '<td>'+ data.user.apeMa +'</td>'
            +   '<td>'+ data.user.cargo +'</td>'
            +   '<td><button type="button" name="btEditarUsuario" id="btEditarUsuario" class="btn  btn-success" onclick="editarUsuario('+ "'" + data.user.rut + "'" +')"> Editar </button></td>'
            +
            '</tr>') 
        },
        error: function(data) {
            alert('error');
            
            }
    }) 
})

function editarUsuario(data){
    
    $.ajax({
        type:'POST',
        url: 'buscarUsuario',
        data: {'rut': data},
        dataType: 'json',
        success: function (data) {
            console.log('funcion editarUsuario!!')
            console.log(data.cargoo.dato[0].idCargo)
            
                    console.log(data.cargoo.dato[0].nomCargo)
        
            $('.frmUsuarioEd').empty();
            $('#footerEd').empty()
            $("#modalUsuarioEd").modal('show');    
            
           $('.frmUsuarioEd').append(
            '<div class="form-group">'+
            '<label for="correlativo">ID</label>'+
            '<input type="text" class="form-control md-2" name="rut" id="idRutt" value="'+ data.usuarioo.rut +'"  required>'+
          '</div>'+
          '<div class="form-group">'+
            '<label for="">Nombre Usuario</label>'+
            '<input type="text" class="form-control md-2" name="nombre" id="idNombree" value="'+ data.usuarioo.nombre +'"  required>'+
          '</div>'+
          '<div class="form-group">'+
             '<label for="correlativo">Apellido Paterno</label>'+
             '<input type="text" class="form-control md-2" name="apePa" id="idApePaa" value="'+ data.usuarioo.apePa +'" required>'+
           '</div>'+
           '<div class="form-group">'+
             '<label for="">Apellido Materno</label>'+
             '<input type="text" class="form-control md-2" name="apeMa" id="idApeMaa" value="'+ data.usuarioo.apeMa +'" required>'+
           '</div>'+
           '<div class="form-group">'+
                  '<label for="">Cargo</label>'+
                  '<select class="form-control md-2" name="cargo" id="idCargooEd" required>'+
                    '<option value="'+ data.usuarioo.cargo +'" selected  >'+ data.usuarioo.cargo +'</option>'+                  
                  '</select>'+
                '</div>'
           ); 
                var i = 0;
                for(i; i < data.cargoo.dato.length; i++){ 
                    $('#idCargooEd').append( '<option value="'+ data.cargoo.dato[i].nomCargo +'">'+ data.cargoo.dato[i].nomCargo +'</option>')
                }
            $('#footerEd').append(               
                '<button type="button" id="guardarCambios" class="btn btn-primary" onclick="actualizarUsuario()">Guardar Cambios</button>'+               
                '<button type="button" id="CancelarUsuario" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>'
                             
            ) 
                
        }
    });
}

function actualizarUsuario(){
    console.log("ESTOY A PUNTO DE ENVIAR LOS DATOS PARA EDITAR")
    
    $("#modalUsuarioEd").modal('toggle');    
    var stData = $('.frmUsuarioEd').serializeArray(); 
    console.log(stData, 'Enviando')
    $('tbody').empty()
        $.ajax({
            type:'POST',
            url: 'usuarioActualizar',
            data: stData,
            dataType: 'json',
            success: function (data) {                  
                console.log('QUE HA PASADOO AQUII')
                console.log(data[0].rut);
                var i = 0;
                for(i; i < data.length; i++){
                $('tbody').append(
                    '<tr>'
                    +   '<th scope="row">'+ data[i].rut +'</th>'
                    +   '<td>'+ data[i].nombre +'</td>'
                    +   '<td>'+ data[i].apePa +'</td>'
                    +   '<td>'+ data[i].apeMa +'</td>'
                    +   '<td>'+ data[i].cargo +'</td>'
                    +   '<td><button type="button" name="btEditarUsuario" id="btEditarUsuario" class="btn  btn-success" onclick="editarUsuario('+ "'" + data[i].rut + "'" +')"> Editar </button></td>'
                    +
                    '</tr>'
                    
                    ) }
                    
            }

        })
}

