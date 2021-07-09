$(document).ready(function(){
    mostrarDisp();
});

/*
function mostrarDisp(){
    $("#btIngresar").click(function(e){
        e.preventDefault();
        $("#modalDispositivo").modal('show');

            $("#btGuardar").click(function(e){
                let dispo = $("#idNom").val();
                let marc = $("#idMar").val();
                let mod = $("#idMod").val();
                let nro = $("#idNro").val();
                let texto = $("#Textarea1").val();
                let estado = $("idEstado").val();
                let sucu = $("#idSuc").val();
                let usu = $("#idUsu").val();
                $.post('http://localhost/inventario/core/views.py', //(urls.py en vez de views.py al parecer), lo de abajo simula un serializerarray al parecer 
                    {"accion":"agregarDispositivo", "idNom":dispo, "idMar":marc, "idMod":mod, "idNro":nro, "Textarea1":texto, "idEstado":estado, "idSuc":sucu, "idUsu":usu},
                        function(data){
                            console.log(data);        
                        }
                    )
        });
    });
}
*/

function mostrarDisp(){
    $("#btIngresar").click(function(e){
        e.preventDefault();
        $("#modalDispositivo").modal('show');
        $("#btGuardar").click(function(jqXHR){
            var stDatos = $('form').serializeArray(); 
            console.log(jqXHR);
            console.log(stDatos)
            $.ajax({
                type:'POST',
                url:'agregarDispositivo',
                data:stDatos,
                success:function(data){
                    console.log('holas 2')
                    swal('Ingresado con exito!',{
                        icon: "success",
                    });
                }
            });
        });
    });
}

    
 