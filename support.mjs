function genskipmaybe (skip, item) {
    if (skip === "true") {
	return `parse_ignoring (lambda : ${item})`;
    } else {
	return item;
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
function genvar (s) {
    varcounter = varcounter + 1;
    return `${s}${varcounter}`;
}
function resetgenvar () {
    varcounter = 0
    return "";
}



function pbplog (s) {
    console.error (s);
}

