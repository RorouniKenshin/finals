const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");
var swiper = new Swiper(".mySwiper", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  },
  on: {
    autoplayTimeLeft(s, time, progress) {
      progressCircle.style.setProperty("--progress", 1 - progress);
      progressContent.textContent = `${Math.ceil(time / 1000)}s`;
    }
  }
});



new VenoBox({
    selector: '.venobox',
});


AOS.init({
    duration : 1500
});


// Wrap every letter in a span
var textWrapper = document.querySelector('.ml16');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml16 .letter',
    translateY: [-100,0],
    easing: "easeOutExpo",
    duration: 1400,
    delay: (el, i) => 30 * i
  }).add({
    targets: '.ml16',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });