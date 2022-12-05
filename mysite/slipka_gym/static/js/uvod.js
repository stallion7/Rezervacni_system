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

let pomucky_img = document.getElementById('pomucky_img');
let images = ['img/expander.jpg','img/blaze_pods.jpg'];
setInterval(function(){
  let random = Math.floor(Math.random() *5);
  pomucky_img.src = images[random];
}, 9000);