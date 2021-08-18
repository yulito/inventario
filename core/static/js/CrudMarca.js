//PERMITE MANTENER ATENTA LA PAGINA PARA LA SOLICITUD DE LA FUNCION agregarMarca()
$(document).ready(function(){
    agregarMarca();
    
});

//LIMPIAMOS LOS BOTONES CADA VEZ QUE LE DAMOS AL BOTON Cancelar
$("#Cancelar").click(function(jqXHR){
    alert('Estoy en Cancelar')
    $("#guardarCambios").remove();
})

//FORMATEAMOS EL MODAL LIMPIANDOLO CADA VEZ QUE LO INVOCAMOS CON EL BOTON btAgregar
function agregarMarca(){
    $("#btAgregar").click(function(e){
        $("#modalMarca").modal('show');
        $('#tituloModelMarca').html('Ingresar Marca')
        $('#idmarca').val('');
        $('#marca').val(''); 
        $('#Guardar').show();
        //NOS LIBRAMOS PRINCIPALMENTE DE ESTOS BOTONES QUE CARGAMOS EN LAS FUNCIONES DE EDITAR MARCA
        $("#guardarCambios").remove();     
    })
}

//GUARDAMOS NUEVA MARCA
$("#Guardar").click(function(jqXHR){
    $("#modalMarca").modal('toggle'); //CERRAMOS EL MODAL
    var stDatos = $('#marca').val();  //creamos una variable con el valor del id de marca que contiene el nombre. RECUERDA que la id de esta tabla es autoincremental     
    console.log(stDatos)
    $.ajax({
        type:'POST',
        url: 'crearMarca',
        data: {'marca':stDatos},
        dataType: 'json',
        success: function (data){
            console.log(data.marcaa.idmarca)                 
            $('tbody').append(
            '<tr>'
            +   '<th scope="row">'+ data.marcaa.idmarca +'</th>'
            +   '<td>'+ data.marcaa.marca +'</td>'
            +   '<td><button type="button" name="btEditar" id="btEditar" class="btn  btn-success" onclick="editarMarca('+ "'" + data.marcaa.idmarca + "'" +')"> Editar </button></td>'
            +
            '</tr>') 
        },
        error: function(data) {
            alert('error');
            
            }
    })
})

//BUSCAMOS EL ID DE LA MARCA LA CUAL QUEREMOS MOSTRAR PARA LUEGO SER EDITADA O ACTUALIZADA (NOS TRAEMOS UN PARAMETRO DE LA FUNCION ONCLICK EN EL BOTON DE AJAX DE btEditar Y EN EL HTML EN EL BOTON btEditar)
function editarMarca(data){
    $.ajax({
        type:'POST',
        url: 'buscarMarca',
        data: {'idmarca': data},
        dataType: 'json',
        success: function (data) {
            console.log('funcion editarMarca!!')
            $("#modalMarca").modal('show');
            $('#tituloModelMarca').html('Editar marca')
            $("#guardarCambios").remove();
            $('#idmarca').val(data.marcaa.idmarca);
            $('#marca').val(data.marcaa.marca);           
            $('#Guardar').hide();  
            $('.modal-footer').append(
                '<button type="button" id="guardarCambios" class="btn btn-primary" onclick="actualizarMarca()">Guardar Cambios</button>' //'+ "'"+ data +"'"+'
                
            )
        }
    });
}

//ESTA FUNCION NOS PERMITE EDITAR O ACTUALIZAR LOS DATOS Y MOSTRARLOS EN EL HTML
function actualizarMarca(){
    console.log("ESTOY A PUNTO DE ENVIAR LOS DATOS PARA EDITAR")
    $("#modalMarca").modal('toggle');
    var idmarca_ = $('#idmarca').val();
    var marca_ = $('#marca').val();
    $('tbody').empty()//************************ ojo    
        $.ajax({
            type:'POST',
            url: 'marcaActualizar',
            data: {'idmarca': idmarca_ ,
                    'marca':marca_},
            dataType: 'json',
            success: function (dato) {                  
                console.log(dato)
                $.each(dato, function(index, value ){                    
                    $('tbody').append(
                        '<tr>'
                        +   '<th scope="row">'+ value[0] +'</th>' 
                        +   '<td>'+ value[1] +'</td>' 
                        +   '<td><button type="button" name="btEditar" id="btEditar" class="btn  btn-success" onclick="editarMarca('+ "'" + value[0] + "'" +')"> Editar </button></td>'
                        +
                        '</tr>'              
                        );                                    
                });  
            }

        })
}

