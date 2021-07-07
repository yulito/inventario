$(document).ready(function(){
    mostrarDisp();
});

function mostrarDisp(){
    $("#btVer").click(function(e){
        e.preventDefault();
        $("#modalDispositivo").modal('show');
    })
}