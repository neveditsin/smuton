function lala(){
	var k = document.getElementById("noofcriteria");
	var l = k.options[k.selectedIndex].value;

	if(l=='1'){
		document.getElementById("items1").style.display = "block";
		document.getElementById("items2").style.display = "none";
		document.getElementById("items3").style.display = "none";
		document.getElementById("items4").style.display = "none";
		document.getElementById("items5").style.display = "none";
	}
	if(l=='2'){
		document.getElementById("items1").style.display = "block";
		document.getElementById("items2").style.display = "block";
		document.getElementById("items3").style.display = "none";
		document.getElementById("items4").style.display = "none";
		document.getElementById("items5").style.display = "none";
	}
	if(l=='3'){
		document.getElementById("items1").style.display = "block";
		document.getElementById("items2").style.display = "block";
		document.getElementById("items3").style.display = "block";
		document.getElementById("items4").style.display = "none";
		document.getElementById("items5").style.display = "none";
	}
	if(l=='4'){
		document.getElementById("items1").style.display = "block";
		document.getElementById("items2").style.display = "block";
		document.getElementById("items3").style.display = "block";
		document.getElementById("items4").style.display = "block";
		document.getElementById("items5").style.display = "none";
	}
	if(l=='5'){
		document.getElementById("items1").style.display = "block";
		document.getElementById("items2").style.display = "block";
		document.getElementById("items3").style.display = "block";
		document.getElementById("items4").style.display = "block";
		document.getElementById("items5").style.display = "block";
	}
	
	
}