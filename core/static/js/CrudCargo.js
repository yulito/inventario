//PERMITE MANTENER ATENTA LA PAGINA PARA LA SOLICITUD DE LA FUNCION agregarMarca()
$(document).ready(function(){
    agregarCargo();
    
});

//LIMPIAMOS LOS BOTONES CADA VEZ QUE LE DAMOS AL BOTON Cancelar
$("#CancelarCargo").click(function(jqXHR){
    alert('Estoy en Cancelar')
    $("#guardarCambios").remove();
})

//FORMATEAMOS EL MODAL LIMPIANDOLO CADA VEZ QUE LO INVOCAMOS CON EL BOTON btAgregar
function agregarCargo(){
    $("#btAgregarCargo").click(function(e){
        $("#modalCargo").modal('show');
        $('#tituloModelCargo').html('Ingresar Cargo')
        $('#idCargo').val('');
        $('#cargo').val(''); 
        $('#GuardarCargo').show();
        //NOS LIBRAMOS PRINCIPALMENTE DE ESTOS BOTONES QUE CARGAMOS EN LAS FUNCIONES DE EDITAR MARCA
        $("#guardarCambios").remove();     
    })
}

//GUARDAMOS NUEVA MARCA
$("#GuardarCargo").click(function(jqXHR){
    $("#modalCargo").modal('toggle'); //CERRAMOS EL MODAL
    var stDatos = $('#cargo').val();  //creamos una variable con el valor del id de marca que contiene el nombre. RECUERDA que la id de esta tabla es autoincremental     
    console.log(stDatos)
    $.ajax({
        type:'POST',
        url: 'crearCargo',
        data: {'cargo':stDatos},
        dataType: 'json',
        success: function (data){
            console.log(data.cargoo.idCargo)                 
            $('tbody').append(
            '<tr>'
            +   '<th scope="row">'+ data.cargoo.idCargo +'</th>'
            +   '<td>'+ data.cargoo.cargo +'</td>'
            +   '<td><button type="button" name="btEditarCargo" id="btEditarCargo" class="btn  btn-success" onclick="editarCargo('+ "'" + data.cargoo.idCargo + "'" +')"> Editar </button></td>'
            +
            '</tr>') 
        },
        error: function(data) {
            alert('error');
            
            }
    })
})


//BUSCAMOS EL ID DE LA MARCA LA CUAL QUEREMOS MOSTRAR PARA LUEGO SER EDITADA O ACTUALIZADA (NOS TRAEMOS UN PARAMETRO DE LA FUNCION ONCLICK EN EL BOTON DE AJAX DE btEditar Y EN EL HTML EN EL BOTON btEditar)
function editarCargo(data){
    $.ajax({
        type:'POST',
        url: 'buscarCargo',
        data: {'idCargo': data},
        dataType: 'json',
        success: function (data) {
            console.log('funcion editarCargo!!')
            $("#modalCargo").modal('show');
            $('#tituloModelCargo').html('Editar Cargo js ')
            $("#guardarCambios").remove();
            $('#idCargo').val(data.cargoo.idCargo);
            $('#cargo').val(data.cargoo.cargo);           
            $('#GuardarCargo').hide();  
            $('.modal-footer').append(
                '<button type="button" id="guardarCambios" class="btn btn-primary" onclick="actualizarCargo()">Guardar Cambios</button>' 
                
            )
        }
    });
}

//ESTA FUNCION NOS PERMITE EDITAR O ACTUALIZAR LOS DATOS Y MOSTRARLOS EN EL HTML
function actualizarCargo(){
    console.log("ESTOY A PUNTO DE ENVIAR LOS DATOS PARA EDITAR") 
    $("#modalCargo").modal('toggle');
    var idCargo_ = $('#idCargo').val();
    var cargo_ = $('#cargo').val();
    $('tbody').empty()   
        $.ajax({
            type:'POST',
            url: 'cargoActualizar',
            data: {'idCargo': idCargo_  ,
                    'cargo':cargo_ },
            dataType: 'json',
            success: function (dato) {                  
                console.log(dato)
                $.each(dato, function(index, value ){                    
                    $('tbody').append(
                        '<tr>'
                        +   '<th scope="row">'+ value[0] +'</th>' 
                        +   '<td>'+ value[1] +'</td>' 
                        +   '<td><button type="button" name="btEditarCargo" id="btEditarCargo" class="btn  btn-success" onclick="editarCargo('+ "'" + value[0] + "'" +')"> Editar </button></td>'
                        +
                        '</tr>'              
                        );                                    
                });  
            }

        })
}

