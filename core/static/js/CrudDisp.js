$(document).ready(function(){
    mostrarDisp();
});

function mostrarDisp(){
    $("#btIngresar").click(function(e){
        e.preventDefault();
        $("#modalDispositivo").modal('show');
        let dispo = $("#idNom").val();
        let marc = $("#idMar").val();
        let mod = $("#idMod").val();
        let nro = $("#idNro").val();
        let texto = $("#Textarea1").val();
        let sucu = $("#idSuc").val();
        let usu = $("#idUsu").val();
        //instanciar ajax, luego añadir funcion de boton agregar onclick y en sus parentesis añadir nombre funcion url y los datos.
        

    });
}

 