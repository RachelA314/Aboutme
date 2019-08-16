window.onscroll = function() {scrollButton()};

function scrollButton(){
   if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10){
     document.getElementById("button").style.display = "block";
  } else {
      document.getElementById("button").style.display = "none";
  }
}

function topPage() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
