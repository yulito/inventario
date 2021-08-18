//PERMITE MANTENER ATENTA LA PAGINA PARA LA SOLICITUD DE LA FUNCION agregarMarca()
$(document).ready(function(){
    agregarTipo();
    
});

//LIMPIAMOS LOS BOTONES CADA VEZ QUE LE DAMOS AL BOTON Cancelar
$("#CancelarTipo").click(function(jqXHR){
    alert('Estoy en Cancelar')
    $("#guardarCambios").remove();
})

//FORMATEAMOS EL MODAL LIMPIANDOLO CADA VEZ QUE LO INVOCAMOS CON EL BOTON btAgregar
function agregarTipo(){
    $("#btAgregarTipo").click(function(e){
        $("#modalTipo").modal('show');
        $('#tituloModelTipo').html('Ingresar Dispositivo')
        $('#idTipo').val('');
        $('#tipo').val(''); 
        $('#GuardarTipo').show();
        //NOS LIBRAMOS PRINCIPALMENTE DE ESTOS BOTONES QUE CARGAMOS EN LAS FUNCIONES DE EDITAR MARCA
        $("#guardarCambios").remove();     
    })
}

//GUARDAMOS NUEVA MARCA
$("#GuardarTipo").click(function(jqXHR){
    $("#modalTipo").modal('toggle'); //CERRAMOS EL MODAL
    var stDatos = $('#tipo').val();  //creamos una variable con el valor del id de marca que contiene el nombre. RECUERDA que la id de esta tabla es autoincremental     
    console.log(stDatos)
    $.ajax({
        type:'POST',
        url: 'crearTipo',
        data: {'tipo':stDatos},
        dataType: 'json',
        success: function (data){
            console.log(data.tipoo.idTipo)                 
            $('tbody').append(
            '<tr>'
            +   '<th scope="row">'+ data.tipoo.idTipo +'</th>'
            +   '<td>'+ data.tipoo.tipo +'</td>'
            +   '<td><button type="button" name="btEditarTipo" id="btEditarTipo" class="btn  btn-success" onclick="editarTipo('+ "'" + data.tipoo.idTipo + "'" +')"> Editar </button></td>'
            +
            '</tr>') 
        },
        error: function(data) {
            alert('error');
            
            }
    })
})


//BUSCAMOS EL ID DE LA MARCA LA CUAL QUEREMOS MOSTRAR PARA LUEGO SER EDITADA O ACTUALIZADA (NOS TRAEMOS UN PARAMETRO DE LA FUNCION ONCLICK EN EL BOTON DE AJAX DE btEditar Y EN EL HTML EN EL BOTON btEditar)
function editarTipo(data){
    $.ajax({
        type:'POST',
        url: 'buscarTipo',
        data: {'idTipo': data},
        dataType: 'json',
        success: function (data) {
            console.log('funcion editarTipo!!')
            $("#modalTipo").modal('show');
            $('#tituloModelTipo').html('Editar Dispositivo')
            $("#guardarCambios").remove();
            $('#idTipo').val(data.tipoo.idTipo);
            $('#tipo').val(data.tipoo.tipo);           
            $('#GuardarTipo').hide();  
            $('.modal-footer').append(
                '<button type="button" id="guardarCambios" class="btn btn-primary" onclick="actualizarTipo()">Guardar Cambios</button>' 
                
            )
        }
    });
}

//ESTA FUNCION NOS PERMITE EDITAR O ACTUALIZAR LOS DATOS Y MOSTRARLOS EN EL HTML
function actualizarTipo(){
    console.log("ESTOY A PUNTO DE ENVIAR LOS DATOS PARA EDITAR") 
    $("#modalTipo").modal('toggle');
    var idTipo_ = $('#idTipo').val();
    var tipo_ = $('#tipo').val();
    $('tbody').empty()   
        $.ajax({
            type:'POST',
            url: 'tipoActualizar',
            data: {'idTipo': idTipo_  ,
                    'tipo':tipo_ },
            dataType: 'json',
            success: function (dato) {                  
                console.log(dato)
                $.each(dato, function(index, value ){                    
                    $('tbody').append(
                        '<tr>'
                        +   '<th scope="row">'+ value[0] +'</th>' 
                        +   '<td>'+ value[1] +'</td>' 
                        +   '<td><button type="button" name="btEditarTipo" id="btEditarTipo" class="btn  btn-success" onclick="editarTipo('+ "'" + value[0] + "'" +')"> Editar </button></td>'
                        +
                        '</tr>'              
                        );                                    
                });  
            }

        })
}

