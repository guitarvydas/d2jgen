function genskip (skip) {
    if (skip == "true") {
	return "parse_ignore ()";
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
	
    
