var supported = !/Gecko/.test(navigator.userAgent) && !/Opera/.test(navigator.userAgent) && /MSIE (5\.5|6)/.test(navigator.userAgent) &&  navigator.platform == "Win32";
function OnLoadPngFix() {
	if(!supported) return;
	if(!event.srcElement) return;
	var src=event.srcElement.src;
	if(!src) return;
	if(!new RegExp(blankSrc).test(src)) {
		// test for png
		if(/\.png$/.test(src.toLowerCase())) {
			src = src.replace(/\(/g, "%28" );
			src = src.replace(/\)/g, "%29" );
			// set blank image
			event.srcElement.src = blankSrc;
			// set filter
			event.srcElement.runtimeStyle.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + src + "',sizingMethod='scale')";
		} 
		else { event.srcElement.runtimeStyle.filter = "";}
	}
}
