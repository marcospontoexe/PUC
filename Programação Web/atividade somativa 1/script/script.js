function openModal(cupcake) {
  var txt1 = document.getElementById("txt1");
  var txt2 = document.getElementById("txt2");
  var txt3 = document.getElementById("txt3");
  switch (cupcake) {
    case "CupFlavor1":
      txt1.innerHTML  = "Cookies And Cream";
      txt2.innerHTML  = "Creme de Negresco no bolo de chocolate.";
      txt3.innerHTML  = "R$15,00";
      break;
    case "CupFlavor2":
      txt1.innerHTML  = "Cookies And Cream";
      txt2.innerHTML  = "Creme de Negresco no bolo de chocolate.";
      txt3.innerHTML  = "R$15,00";
      break;
    case "CupFlavor3":
      txt1.innerHTML  = "Cookies And Cream";
      txt2.innerHTML  = "Creme de Negresco no bolo de chocolate.";
      txt3.innerHTML  = "R$15,00";
      break;
    case "CupFlavor4":
      txt1.innerHTML  = "Cookies And Cream";
      txt2.innerHTML  = "Creme de Negresco no bolo de chocolate.";
      txt3.innerHTML  = "R$15,00";
      break;
    case "CupFlavor5":
      txt1.innerHTML  = "Cookies And Cream";
      txt2.innerHTML  = "Creme de Negresco no bolo de chocolate.";
      txt3.innerHTML  = "R$15,00";
      break;
    case "CupFlavor6":
      txt1.innerHTML  = "Cookies And Cream";
      txt2.innerHTML  = "Creme de Negresco no bolo de chocolate.";
      txt3.innerHTML  = "R$15,00";
      break;
        
    default:
      txt1.innerHTML  = "Cookies And Cream";    
      txt2.innerHTML  = "Cookies And Cream";txt1.innerHTML  = "Delicioso cupkake.";
      txt3.innerHTML  = "R$15,00";
  }
  document.getElementById("knowMore").style.display = "block";
}

function closeModal() {
  document.getElementById("knowMore").style.display = 'none';
}


function mascaraTelefone(event) {
    let tecla = event.key;
    // Regex:
    // g = não termina verificação enquanto não houver combinação para todos os elementos
    // \D+ = troca qualquer caractere que não seja um dígito por caracter vazio
    let telefone = event.target.value.replace(/\D+/g, "");
    // Regex: i = case insensitive
    // Se Tecla é número, concatena com telefone
    if(/^[0-9]$/i.test(tecla)) {
        telefone = telefone + tecla;
        let tamanho = telefone.length;
        if(tamanho >= 12) { // Se telefone com 12 ou mais caracteres, não faz mais nada
            return false;
        }
        if(tamanho > 10) {
            telefone = telefone.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
        } else if(tamanho > 5) {
            telefone = telefone.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
        } else if(tamanho > 2) {
            telefone = telefone.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
        } else {
            telefone = telefone.replace(/^(\d*)/, "($1");
        }
        event.target.value = telefone;
    }
    if(!["Backspace", "Delete", "Tab"].includes(tecla)) {
        return false;
    }
}

// Espera até que o DOM esteja totalmente carregado
document.addEventListener('DOMContentLoaded', function () {

    // Adiciona event listener ao campo de telefone para aplicar a máscara
    document.getElementById('celular').addEventListener('keydown', mascaraTelefone);
    
});






