const whatsapp = new WhatsApp({
    phone: "+5355089270",
    message: "Hola, vengo desde Vilanova'Shop y  deseo comprar este producto: {productName}. El precio es {productPrice}",
  });
  
  const button = document.getElementById("buyButton");
  button.addEventListener("click", () => {
    whatsapp.send();
  });