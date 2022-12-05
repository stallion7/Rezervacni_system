const options = {
  bottom: '23px', // default: '32px'
  right: '32px', // default: '32px'
  left: 'unset', // default: 'unset'
  time: '0.3s', // default: '0.3s'
  mixColor: '#fff', // default: '#fff'
  backgroundColor: '#fff',  // default: '#fff'
  buttonColorDark: '#000',  // default: '#100f2c'
  buttonColorLight: '#fff', // default: '#fff'
  saveInCookies: true, // default: true,
  label: '🌓', // default: ''
  autoMatchOsTheme: true // default: true
}

const darkmode = new Darkmode(options);
darkmode.showWidget();

function myFunction() {
  let dots = document.getElementById("dots");
  let moreText = document.getElementById("more");
  let btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}
function myFunction2() {
  let dots2 = document.getElementById("dots2");
  let moreText2 = document.getElementById("more2");
  let btnText2 = document.getElementById("myBtn2");

  if (dots2.style.display === "none") {
    dots2.style.display = "inline";
    btnText2.innerHTML = "Read more";
    moreText2.style.display = "none";
  } else {
    dots2.style.display = "none";
    btnText2.innerHTML = "Read less";
    moreText2.style.display = "inline";
  }
}
function myFunction3() {
  let dots3 = document.getElementById("dots3");
  let moreText3 = document.getElementById("more3");
  let btnText3 = document.getElementById("myBtn3");

  if (dots3.style.display === "none") {
    dots3.style.display = "inline";
    btnText3.innerHTML = "Read more";
    moreText3.style.display = "none";
  } else {
    dots3.style.display = "none";
    btnText3.innerHTML = "Read less";
    moreText3.style.display = "inline";
  }
}
function myFunction4() {
  let dots4 = document.getElementById("dots4");
  let moreText4 = document.getElementById("more4");
  let btnText4 = document.getElementById("myBtn4");

  if (dots4.style.display === "none") {
    dots4.style.display = "inline";
    btnText4.innerHTML = "Read more";
    moreText4.style.display = "none";
  } else {
    dots4.style.display = "none";
    btnText4.innerHTML = "Read less";
    moreText4.style.display = "inline";
  }
}

/*
let pomucky_img = document.getElementById('pomucky_img');
let images = ['img/expander.jpg','img/blaze_pods.jpg', 'img/svihadla.jpg'];
setInterval(function(){
  let random = Math.floor(Math.random() *5);
  pomucky_img.src = images[random];
}, 9000);

let kruhovy_img = document.getElementById('kruhovy_img');
let images2 = ['img/uvod2.jpg','img/uvod3.jpg','img/trenink2.jpg'];
setInterval(function(){
  let random = Math.floor(Math.random() *5);
  kruhovy_img.src = images2[random];
}, 12000);

let zavody_img = document.getElementById('zavody_img');
let images3 = ['img/zavod1.jpg','img/zavod2.jpg','img/zavod3.jpg','img/zavod4.jpg','img/zavod5.jpg'];
setInterval(function(){
  let random = Math.floor(Math.random() *5);
 zavody_img.src = images3[random];
}, 9000);

let party_img = document.getElementById('party_img');
let images4 = ['img/uvod.jpg','img/party2.jpg'];
setInterval(function(){
  let random = Math.floor(Math.random() *5);
  party_img.src = images4[random];
}, 9000);

 */