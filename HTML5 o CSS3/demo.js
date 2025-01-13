widthi = document.querySelector(".width");
heighti = document.querySelector(".height");
paddingi = document.querySelector(".padding");
margeni = document.querySelector(".margen");
bordei = document.querySelector(".borde");
borde_raduisi = document.querySelector(".borde_raduis");
selecti = document.querySelector(".select");
caja = document.querySelector(".caja");

widthi.onchange = function(){
    valor1 = widthi.value;
    caja.style.width = `${valor1}px`;
    const text1 = document.createElement("p");
    text1.textContent = `${valor}px`;
    widthi.appendChild(text1);}

heighti.onchange = function(){
    valor2 = heighti.value;
    caja.style.height = `${valor2}px`;
    const text2 = document.createElement("p");
    text2.textContent = `${valor2}px`;
    heighti.appendChild(text2);}

paddingi.onchange = function(){
    valor3 = paddingi.value;
    caja.style.padding = `${valor3}px`;
    const text3 = document.createElement("p");
    text3.textContent = `${valor3}px`;
    paddingi.appendChild(text3);}

margeni.onchange = function(){
    valor4 = margeni.value;
    caja.style.margin = `${valor4}px`;
    const text4 = document.createElement("p");
    text4.textContent = `${valor4}px`;
    margeni.appendChild(text4);}

bordei.onchange = function(){
    valor5 = bordei.value;
    caja.style.border = `${valor5}px solid black`;
    const text5 = document.createElement("p");
    text5.textContent = `${valor5}px`;
    bordei.appendChild(text5);}

    borde_raduisi.onchange = function(){
    valor6 = borde_raduisi.value;
    caja.style.borderRadius = `${valor6}px`;
    const text6 = document.createElement("p");
    text6.textContent = `${valor6}px`;
    borde_raduisi.appendChild(text6);}

selecti.onchange = function(){
    valor7 = selecti.value;
    caja.style.boxSizing = `${valor7}`;}