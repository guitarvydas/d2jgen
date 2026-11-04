function genskip (skip) {
    if (skip === "true") {
	return "\nparse_ignore ()";
    } else {
	return "";
    }
}

function genslprefix (name) {
    let firstc = name [0];
    if ((name[0] >= 'A' && name[0] <= 'Z') || (name[0] == '_')) {
	return `s_${name}`;
    } else {
	return `l_${name}`;
    }
}
	
function finalexit (retvar, funcname) {
    return `if ${retvar}:⤷\nreturn accept ("${funcname}")⤶\nelse:⤷\nreturn fail ("${funcname}")⤶`
}


let varcounter = 0;
function genvar () {
    varcounter = varcounter + 1;
    return `${varcounter}`;
}

