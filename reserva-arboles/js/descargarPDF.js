document.getElementById('descargarPDFUsusarios').addEventListener('click', () => {
  // Ruta al archivo PDF
  var rutaPDF = '../pdf/usuarios.pdf';
  
  // Nombre del archivo
  var nombreArchivo = 'usuarios.pdf';
  
  // Crear un enlace temporal
  var link = document.createElement('a');
  link.href = rutaPDF;
  link.download = nombreArchivo;
  
  // Simular clic en el enlace para descargar el archivo
  document.body.appendChild(link);
  link.click();
  
  // Limpiar el enlace temporal
  document.body.removeChild(link);
});

document.getElementById('descargarPDFRefrigerios').addEventListener('click', () => {
  // Ruta al archivo PDF
  var rutaPDF = '../pdf/refrigerios.pdf';
  
  // Nombre del archivo
  var nombreArchivo = 'refrigerios.pdf';
  
  // Crear un enlace temporal
  var link = document.createElement('a');
  link.href = rutaPDF;
  link.download = nombreArchivo;
  
  // Simular clic en el enlace para descargar el archivo
  document.body.appendChild(link);
  link.click();
  
  // Limpiar el enlace temporal
  document.body.removeChild(link);
});

document.getElementById('descargarPDFSiembras').addEventListener('click', () => {
  // Ruta al archivo PDF
  var rutaPDF = '../pdf/siembras.pdf';
  
  // Nombre del archivo
  var nombreArchivo = 'siembras.pdf';
  
  // Crear un enlace temporal
  var link = document.createElement('a');
  link.href = rutaPDF;
  link.download = nombreArchivo;
  
  // Simular clic en el enlace para descargar el archivo
  document.body.appendChild(link);
  link.click();
  
  // Limpiar el enlace temporal
  document.body.removeChild(link);
});