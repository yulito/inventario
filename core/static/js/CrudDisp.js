$(document).ready(function(){
    mostrarDisp();
});

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
                //instanciar ajax, luego añadir funcion de boton agregar onclick y en sus parentesis añadir nombre funcion url y los datos.
                $.post('http://localhost/inventario/core/views.py',
                    {"accion":"agregarDispositivo", "idNom":dispo, "idMar":marc, "idMod":mod, "idNro":nro, "Textarea1":texto, "idEstado":estado, "idSuc":sucu, "idUsu":usu},
                        
                    )
        });
    });
}

 