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
	
function finalexit (cond, retvar, funcname) {
    if (cond === "⊤⊥") {
	return `if ${retvar}: return accept ("${funcname}"); else: return fail ("${funcname}")`;
    } else {
	return `if ${revar}: return fail ("${funcname}"); else: return accept ("${funcname}")`;
    }
}

function negatecond (cond) {
    if (cond === "⊤⊥") {
	return "⊥⊤";
    } else {
	return "⊤⊥";
    }
}
function conjoin (cond) {
    if (cond === "⊤⊥") {
	return "and";
    } else {
	return "or";
    }
}
    
function maybenot (cond, s) {
    if (cond === "⊤⊥") {
	return s;
    } else {
	return `(not ${s})`;
    }
}
    

let varcounter = 0;
function genvar () {
    varcounter = varcounter + 1;
    return `${varcounter}`;
}

