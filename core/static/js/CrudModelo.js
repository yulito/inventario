$(document).ready(function(){
    agregarModelo();
});

$("#CancelarModelo").click(function(jqXHR){
    alert('Estoy en Cancelar')   
})

function agregarModelo(){
    $("#btAgregarModelo").click(function(e){
        $(".frmModelo").trigger('reset');    //RECUERDA QUE LA FUNCION TRIGGER FUNCIONA CUANDO ES UN SERIALIZERARRAY
        $("#modalModelo").modal('show');
        $("#guardarCambiosed").remove();
    })
}

$("#GuardarModelo").click(function(jqXHR){
    $("#modalModelo").modal('toggle'); 
    var stDatos = $('.frmModelo').serializeArray();
    console.log(stDatos)
    
    $.ajax({
        type:'POST',
        url: 'crearModelo',
        data: stDatos,
        success: function (data){
            console.log(data) 
                          
            $('tbody').append(
            '<tr>'
            +   '<th scope="row">'+ data.modelo.idModelo +'</th>'
            +   '<td>'+ data.modelo.nombre +'</td>'
            +   '<td>'+ data.modelo.marca +'</td>'
            +   '<td>'+ data.modelo.tipo +'</td>'
            +   '<td><button type="button" name="btEditarModelo" id="btEditarModelo" class="btn  btn-success" onclick="editarModelo('+ "'" + data.modelo.idModelo + "'" +')"> Editar </button></td>'
            +
            '</tr>') 
        },
        error: function(data) {
            alert('error');
            
            } 
    }) 
}) 

function editarModelo(data){
    
    $.ajax({
        type:'POST',
        url: 'buscarModelo',
        data: {'idModelo': data},
        dataType: 'json',
        success: function (data) {
            console.log('funcion editarModelo!!')
            console.log(data.marcaa.datom[0].nomMarca)
                  
            $('.frmModeloEd').empty();
            $('#footermodEd').empty()
            $("#modalModeloEd").modal('show');    
            
           $('.frmModeloEd').append(

            '<div class="form-group">'+
                '<label for="correlativo">Id Modelo: '+ data.modeloo.idModelo +'</label>'+
                '<input type="text" class="form-control md-2" name="modeloed" id="idModeloed" value="'+ data.modeloo.idModelo +'" hidden >'+
                    '</div>'+
                    '<div class="form-group">'+
                      '<label for="">Modelo</label>'+
                      '<input type="text" class="form-control md-2" name="nombreModed" id="idNombreModed"  value="'+ data.modeloo.nombre +'" required>'+
                    '</div>'+
                    '<div class="form-group">'+
                     '<label for="">Marca</label>'+
                        '<select class="form-control md-2" name="marcaModed" id="idMarcaModed"  required>'+                          
                          '<option value="'+ data.modeloo.marca +'"> '+ data.modeloo.marca +' </option>'+                         
                        '</select>'+
                      '</div> '+
                    '<div class="form-group">'+
                      '<label for="">Tipo Dispositivo</label>'+
                      '<select class="form-control md-2" name="modeloTipoed" id="idModeloTipoed" required>'+                        
                        '<option value="'+ data.modeloo.tipo +'">'+ data.modeloo.tipo +'</option>'+                        
                      '</select>'+
                    '</div> '
          
           ); 
                
                var i = 0;
                for(i; i < data.marcaa.datom.length; i++){ 
                    $('#idMarcaModed').append( '<option value="'+ data.marcaa.datom[i].nomMarca +'">'+ data.marcaa.datom[i].nomMarca +'</option>')
                }
                var j = 0;
                for(j; j < data.tipoo.tipod.length; j++){ 
                    $('#idModeloTipoed').append( '<option value="'+ data.tipoo.tipod[j].nomTipo +'">'+ data.tipoo.tipod[j].nomTipo +'</option>')
                }

            $('#footermodEd').append(               
                '<button type="button" id="guardarCambiosed" class="btn btn-primary" onclick="actualizarModelo()">Guardar Cambios</button>'+               
                '<button type="button" id="CancelarModelo" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>'
                             
            ) 
              
        } 
    });
}


function actualizarModelo(){
    console.log("ESTOY A PUNTO DE ENVIAR LOS DATOS PARA EDITAR")
    
    $("#modalModeloEd").modal('toggle');    
    var stData = $('.frmModeloEd').serializeArray(); 
    console.log(stData, 'Enviando')
    
    $('tbody').empty()
        $.ajax({
            type:'POST',
            url: 'modeloActualizar',
            data: stData,
            dataType: 'json',
            success: function (data) {                  
                console.log('QUE HA PASADOO AQUII')
                console.log(data); //console.log(data[0].rut);
                var i = 0;
                for(i; i < data.length; i++){
                $('tbody').append(
                    '<tr>'
                    +   '<th scope="row">'+ data[i].idMod +'</th>'
                    +   '<td>'+ data[i].nombremod +'</td>'
                    +   '<td>'+ data[i].marcamod +'</td>'
                    +   '<td>'+ data[i].tipomod +'</td>'
                    +   '<td><button type="button" name="btEditarModelo" id="btEditarModelo" class="btn  btn-success" onclick="editarModelo('+ "'" + data[i].idMod + "'" +')"> Editar </button></td>'
                    +
                    '</tr>'
                    
                    ) } 
                    
                }

        }) 
}
