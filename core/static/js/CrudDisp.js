$(document).ready(function(){
    agregarDisp();
});

$("#cancelarDisp").click(function(jqXHR){
    alert('Estoy en Cancelar')  
})

function agregarDisp(){
    $("#btIngresarDispositivo").click(function(e){
        $("#modalDispositivo").modal('show');
        $(".frmDispositivo").trigger('reset');

    })
}

$("#GuardarDispositivo").click(function(jqXHR){
    $("#modalDispositivo").modal('toggle'); 
    var stDatos = $('.frmDispositivo').serializeArray();
    console.log(stDatos)
    $.ajax({
        type:'POST',
        url: 'crearDispositivo',
        data: stDatos,
        success: function (data){
            console.log(data)                
            $('tbody').append(
            '<tr>'
            +   '<th scope="row">'+ data.dispp.id +'</th>'
            +   '<td>'+ data.dispp.tipo +'</td>'
            +   '<td>'+ data.dispp.marca +'</td>'
            +   '<td>'+ data.dispp.nro +'</td>'
            +   '<td>'+ data.dispp.modelo +'</td>'
            +   '<td>'+ data.dispp.estado +'</td>'
            +   '<td>'+ data.dispp.usuario +'</td>'
            +   '<td><button type="button" name="btEditarDispositivo" id="btEditarDispositivo" class="btn  btn-success" onclick="editarDispositivo('+ "'" + data.dispp.id + "'" +')"> Editar </button></td>'
            +
            '</tr>') 
        },
        error: function(data) {
            alert('error');
            
            }
    })

})

function editarDispositivo(data){
    
    $.ajax({
        type:'POST',
        url: 'buscarDispositivo',
        data: {'id': data},
        dataType: 'json',
        success: function (data) {
            console.log('funcion buscarDispositivo!!')
            console.log(data)
            $('.frmDispositivoEd').empty();
            $('#footerDispEd').empty()
            $("#modalDispositivoEd").modal('show'); 
           $('.frmDispositivoEd').append(
            '<div class="form-group">'+
                '<label for="correlativo">ID: '+ data.dispoo.id +'</label>'+
                '<input type="number" class="form-control md-2" name="idcorred" id="idcorred" value="'+ data.dispoo.id +'" hidden>'+
            '</div>'+
          '<div class="form-group">'+
                '<label for="">Modelo</label>'+
                    '<select class="form-control md-2" name="Moded" id="idModed" required>'+
                        '<option value="'+ data.dispoo.modelo +'" selected  >'+ data.dispoo.modelo +'</option>'+ 
                    '</select>'+
            '</div>'+
            '<div class="form-group">'+
                '<label for="">Nro de Serie</label>'+
                  '<input type="text" class="form-control md-2" name="Nroed" id="idNro" value="'+ data.dispoo.serie +'"  required>'+
                    '</div>'+
                    '<div class="form-group">'+
                      '<label for="">Comentario</label>'+
                      '<textarea class="form-control md-2" id="Textarea1" name="Textoed" rows="3" value="'+ data.dispoo.texto +'" >'+ data.dispoo.texto +'</textarea>'+
                    '</div>'+
                    '<div class="form-check" >'+
                      '<input class="form-check-input" type="radio"  name="Estadoed" id="idEstadoed" value=1 >'+
                      '<label class="form-check-label" for="exampleRadios1">'+
                        'Habilitado'+
                      '</label>'+
                    '</div>'+
                    '<div class="form-check">'+
                      '<input class="form-check-input" type="radio"  name="Estadoed" id="idEstadoed" value=2>'+
                      '<label class="form-check-label" for="exampleRadios2">'+
                        'En Uso'+
                      '</label>'+
                    '</div>'+
                    '<div class="form-check disabled">'+
                      '<input class="form-check-input" type="radio"  name="Estadoed" id="idEstadoed" value=3 >'+
                      '<label class="form-check-label" for="exampleRadios3">'+
                        'Deshabilitado'+
                      '</label>'+
                    '</div>'+
                    '<div class="form-group">'+
                      '<label for="">Sucursal</label>'+
                      '<select class="form-control md-2" name="Suced" id="idSuced" required>'+
                      '<option value="'+ data.dispoo.sucursal +'" selected  >'+ data.dispoo.sucursal +'</option>'+                       
                      '</select>'+
                    '</div>'+
                    '<div class="form-group">'+
                      '<label for="">Usuario</label>'+
                      '<input type="text" class="form-control md-2" name="Usued" id="idUsued" value="'+ data.dispoo.rut +'">'+
                    '</div>'
            )
            var i = 0;
                for(i; i < data.mode.datoI.length; i++){ 
                    $('#idModed').append( '<option value="'+ data.mode.datoI[i].nomMod +'">'+ data.mode.datoI[i].nomMod +'</option>')
                }
                var i = 0;
                for(i; i < data.sucur.datoII.length; i++){ 
                    $('#idSuced').append( '<option value="'+ data.sucur.datoII[i].nombreSuc +'">'+ data.sucur.datoII[i].nombreSuc  +'</option>')
                }
                $('#footerDispEd').append(               
                    '<button type="button" id="guardarCambios" class="btn btn-primary" onclick="actualizarDispositivo()">Guardar Cambios</button>'+               
                    '<button type="button" id="CancelarDisp" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>'
                                 
                ) 
        }
    });
}

function actualizarDispositivo(){
    console.log("ESTOY A PUNTO DE ENVIAR LOS DATOS PARA EDITAR")
    
    $("#modalDispositivoEd").modal('toggle');    
    var stData = $('.frmDispositivoEd').serializeArray(); 
    console.log(stData, 'Enviando')
    $('tbody').empty()
        $.ajax({
            type:'POST',
            url: 'dispositivoActualizar',
            data: stData,
            dataType: 'json',
            success: function (data) {                  
                console.log('QUE HA PASADOO AQUII')
                console.log(data);
                
                var i = 0;
                for(i; i < data.length; i++){
                $('tbody').append(
                    '<tr>'
                    +   '<th scope="row">'+ data[i].corre +'</th>' 
                    +   '<td>'+ data[i].tipo +'</td>'
                    +   '<td>'+ data[i].marca +'</td>'
                    +   '<td>'+ data[i].serie +'</td>'
                    +   '<td>'+ data[i].modelo +'</td>'
                    +   '<td>'+ data[i].estado +'</td>'
                    +   '<td>'+ data[i].rut +'</td>'
                    +   '<td><button type="button" name="btEditarDispositivo" id="btEditarDispositivo" class="btn  btn-success" onclick="editarDispositivo('+ "'" + data[i].corre + "'" +')"> Editar </button></td>'
                    +
                    '</tr>'
                    
                    ) }
            }

        })
}