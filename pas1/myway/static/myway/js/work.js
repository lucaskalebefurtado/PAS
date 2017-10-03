$(function(){
	$('#poo').on('mouseover',(function(){
    	$('#ip').addClass("dependente");
		}));


});
var clicou = false;

// disciplinas do primeiro período que tem dependências
function mostraDependenciasIp(){
	document.getElementById("ip").className = "fonte";
	document.getElementById("lp").className = "dependente";

}


function tiraDependenciasIp(){
	document.getElementById("ip").className = "profissional";
	document.getElementById("lp").className = "profissional";

}


function mostraDependenciasADM1(){
	document.getElementById("adm1").className = "fonte";
	document.getElementById("adm2").className = "dependente";
}	

function tiraDependenciasADM1(){
	document.getElementById("adm1").className = "profissional"
	document.getElementById("adm2").className = "profissional";
}



function mostraDependenciasIc(){
	document.getElementById("ic").className = "fonte";
	document.getElementById("arquitetura").className = "dependente";
}	

function tiraDependenciasIc(){
	document.getElementById("ic").className = "profissional";
	document.getElementById("arquitetura").className = "profissional";
		
}



function mostraDependenciasMetodologia(){
	if (clicou == false) {
		document.getElementById("pesquisaAplicada").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("pesquisaAplicada").className = "complementar";
		clicou = false;
		
	}
}

function mostraDependenciasElementar(){
	if (clicou == false) {
		document.getElementById("logica").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("logica").className = "complementar";
		clicou = false;
		
	}
}

//segundo período
function mostraDependenciasLp(){
	if (clicou == false) {
		document.getElementById("estrutura1").className = "dependente";
		document.getElementById("poo").className = "dependente";
		document.getElementById("engenharia").className = "dependente";
		document.getElementById("plp").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("estrutura1").className = "profissional";
		document.getElementById("poo").className = "profissional";
		document.getElementById("engenharia").className = "profissional";
		document.getElementById("plp").className = "profissional";
		clicou = false;
		
	}
}


function mostraDependenciasCalculo(){
	if (clicou == false) {
		document.getElementById("estatistica").className = "dependente";
		document.getElementById("algebra").className = "dependente"
		clicou = true;	}	
	else{
		document.getElementById("estatistica").className = "profissional";
		document.getElementById("algebra").className = "profissional";

		clicou = false;
		
	}
}

function mostraDependenciasArquitetura(){
	if (clicou == false) {
		document.getElementById("SO").className = "dependente";
		document.getElementById("redes").className = "dependente"
		clicou = true;	}	
	else{
		document.getElementById("SO").className = "profissional";
		document.getElementById("redes").className = "profissional";

		clicou = false;
		
	}
}


function mostraDependenciasADM2(){
	if (clicou == false) {
		document.getElementById("GI").className = "dependente";
		document.getElementById("SAG").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("GI").className = "complementar";
		document.getElementById("SAG").className = "complementar";
		clicou = false;
		
	}
}

function mostraDependenciasLogica(){
	if (clicou == false) {
		document.getElementById("IA").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("IA").className = "complementar";
		clicou = false;
		
	}
}


//terceiroPeriodo

function mostraDependenciasEstrutura(){
	if (clicou == false) {
		document.getElementById("estrutura2").className = "dependente";
		document.getElementById("banco1").className = "dependente"
		clicou = true;	}	
	else{
		document.getElementById("estrutura2").className = "profissional";
		document.getElementById("banco1").className = "profissional";

		clicou = false;
		
	}
}

function mostraDependenciasEstatistica(){
	if (clicou == false) {
		document.getElementById("ADS").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("ADS").className = "complementar";
		clicou = false;
		
	}
}

//QUARTO PERÍODO

function mostraDependenciasEngenharia(){
	if (clicou == false) {
		document.getElementById("esa").className = "dependente";
		document.getElementById("gerenciaDeProjeto").className = "dependente";
		document.getElementById("gqs").className = "dependente";
		document.getElementById("estagio").className = "dependente";
		document.getElementById("ihm").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("esa").className = "complementar";
		document.getElementById("gerenciaDeProjeto").className = "complementar";
		document.getElementById("gqs").className = "complementar";
		document.getElementById("estagio").className = "estagio";
		document.getElementById("ihm").className = "complementar";
		clicou = false;
		
	}
}

//QUINTO PERÍODO

function mostraDependenciasBanco(){
	if (clicou == false) {
		document.getElementById("banco2").className = "dependente";
		document.getElementById("corporativos").className = "dependente"
		clicou = true;	}	
	else{
		document.getElementById("banco2").className = "profissional";
		document.getElementById("corporativos").className = "profissional";

		clicou = false;
		
	}
}

function mostraDependenciasEsa(){
	if (clicou == false) {
		document.getElementById("pas").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("pas").className = "profissional";
		clicou = false;
		
	}
}

function mostraDependenciasSO(){
	if (clicou == false) {
		document.getElementById("SD").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("SD").className = "complementar";
		clicou = false;
		
	}
}


function mostraDependenciasRedes(){
	if (clicou == false) {
		document.getElementById("SD").className = "dependente";
		document.getElementById("gerenciaDeRedes").className = "dependente"
		document.getElementById("auditoria").className = "dependente"
		clicou = true;	}	
	else{
		document.getElementById("SD").className = "complementar";
		document.getElementById("gerenciaDeRedes").className = "profissional";
		document.getElementById("auditoria").className = "complementar"

		clicou = false;
		
	}

}

//ultima cadeira

function mostraDependenciasGP(){
	if (clicou == false) {
		document.getElementById("tcc").className = "dependente";
		clicou = true;	}	
	else{
		document.getElementById("tcc").className = "complementar";
		clicou = false;
		
	}
}