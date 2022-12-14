function toggleMobileMenu(menu){
	menu.classList.toggle('open');
	var x = document.getElementById("d1");
	
if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
// best();
// function best(){
// 	console.log("cange");
// var w=screen.width;
// if(w>600)
// {
// 	var a = document.getElementById("hamburger-icon");
//  a.style.visibility = "hidden";

// }
// else{
//  a.style.display = "visible";

// }
// }
// window.addEventListener('resize', best);
