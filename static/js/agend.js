function validarFormulario() {
    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var servico = document.getElementById('servico').value;
    var data = document.getElementById('data').value;
    var hora = document.getElementById('hora').value;
  
    if (nome === '') {
      alert('Por favor, insira seu nome.');
      return false;
    }
  
    if (email === '') {
      alert('Por favor, insira seu email.');
      return false;
    }
  
    if (servico === '') {
      alert('Por favor, selecione um serviço.');
      return false;
    }
  
    if (data === '') {
      alert('Por favor, selecione uma data.');
      return false;
    }
  
    if (hora === '') {
      alert('Por favor, selecione uma hora.');
      return false;
    }
  
    alert('Seu agendamento foi enviado com sucesso!');
    document.getElementById('formulario').submit();
  }
  
  function inicializar() {
    document.getElementById('enviar').addEventListener('click', validarFormulario);
  }
  
  window.onload = inicializar;