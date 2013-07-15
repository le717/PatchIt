function GetSiteSearchResults(newWindow,frameObject,frameObjectName,fontFace,fontSize,fontColour,linkFace,linkSize,linkColour,resultsText)
{
var sTerms="";
var iDepth = 0;
var sURL = new String(document.location);
if (sURL.indexOf("?") > 0)
{
var arrParams = sURL.split("?");
var arrURLParams = arrParams[1].split("&");
for (var i=0;i<arrURLParams.length;i++)
{
var sParam = arrURLParams[i].split("=");
var sValue = unescape(sParam[1]);
if( sParam[0] == frameObjectName)
	sTerms = sValue;
if( sParam[0] == "depth")
	iDepth = parseInt(sValue);
}
}
var d=frameObject.document;
if (sTerms=="") {d.open(); d.write("<html><head></head><body style=\"background: transparent;\"></body></html>"); d.close();return;}
var sBack=""; for (i=0; i<iDepth; i++) sBack+='..\\\\';
d.open();
d.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">");
d.write("<html lang=\"en\">");
d.write("<head>");
d.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">");
d.write("</head>");
d.write("<body style=\"margin: 0px 0px 0px 0px; font-family: "+fontFace+"; font-size: "+fontSize+"; color: "+fontColour+"; background: transparent;\">");
d.write("<div id=\"wpSearchResults\"></div>");
d.write("<script type=\"text/javascript\">");
d.write("var wordMap = new Array(\" patchit standard simple package install lego® racers mods welcome readme here will find information support help about created triangle717 continually being updated ability modifications 1999 video game also 1998 loco \",\" \",\" installing patch install patchit compatible patch simply load press select file after reading information confirm installation will automatically into your lego® racers game need resources page download unsure about everything successfully check section tutorial \",\" creating patch create patchit compatible load press type your mod's mods name version author description point modded files will compress them into archive file write details stable later automatically filter stops illegal from being compressed complete this process found github both items filename located same folder uncompressed check format documentation complete have made lego® loco need enter screen resolution used this important played different some elements destroying hard work making \",\" support request feature submit code patch download release patchit please http github le717 report issues state attach your file located program files logs attaching this will ensure found easier released much faster \",\" \",\" resources following sites programs helpful your patchit documentation extras patches started lego® racers extractor extracts builds lego setting installing tutorial jimbobjeffers rock raiders united only place learn everything need know about modding python programming language written rioforce designer creator graphics readme \",\" about patchit python application written triangle717 standard simple packaging installing mods lego® racers plan although modding still it's early stages many already being developed there needs install them heavily influenced based patchman installer 1999 data design interactive game rock raiders aims lego works three main goals follows installation ensure exists that location store plain text file same folder used directory create completely portable which means flash-drive create patch entering name version author description point modded files automatically compress into normal archive write details using filenames install selecting confirm automatically decompress directly racers® \");");
d.write("var pageMap = new Array(\"Home\",\"Search Results\",\"Installing a Patch\",\"Creating a Patch\",\"Support\",\"Change Log\",\"Resources\",\"About\");");
d.write("var linkMap = new Array(\"index.html\",\"search.html\",\"install.html\",\"create.html\",\"support.html\",\"changes.html\",\"resources.html\",\"about.html\");");
d.write("var preMap = new Array(\"“ ” PatchIt! The standard and simple way to package and install LEGO® Racers mods. Welcome to the PatchIt! readme. Here, you will find information, support, and help about PatchIt! PatchIt! was create\",\"\",\"Installing a Patch To install a PatchIt! compatible patch, simply load PatchIt!, press the i key, select the PiP file, and after reading the patch information, confirm the installation. PatchIt! wil\",\"Creating a Patch To create a PatchIt! compatible mod, load PatchIt! and press the c key. Type your mods name, version, author, and description. Point it to your modded files, and PatchIt! will comp\",\"Support To request a feature, submit a code patch, or download a new release of PatchIt!, please go to http://github.com/le717/PatchIt. To submit a bug report, please go to http://github.com/le717/Pat\",\"\",\"Resources The following sites and programs may be helpful to you and in your use of PatchIt!  • PatchIt! Documentation • PatchIt! Extras: Patches to get you started! • LEGO® Racers JAM Extractor: Extr\",\"About PatchIt! Is a Python 3 application written by Triangle717 to be the standard and simple way to packaging and installing mods for LEGO® Racers. The Plan  Although LEGO® Racers modding is still in\");");
d.write("function doNav(ind)");
d.write("{");
if (newWindow)
d.write("		 window.open(\""+sBack+"\"+linkMap[ind],\"_blank\");");
else
d.write("		 parent.window.location.href=linkMap[ind];");
d.write("}");
d.write("function wpDoSearch(searchTerms){");
d.write("var terms = searchTerms.split(\" \");");
d.write("if (terms==\"\") return;");
d.write("var results = \"\";");
d.write("var resultscount = 0;");
d.write("for (var i=0; i<wordMap.length; i++)");
d.write("{");
d.write("			var found=true;");
d.write("			for (var j=0; j<terms.length; j++)");
d.write("					if (wordMap[i].indexOf(terms[j].toLowerCase())==-1) found=false;");
d.write("			if (found)");
d.write("			{");
d.write("				 results+=\"<a style=\\\"cursor: pointer; font-family: "+linkFace+"; font-size: "+linkSize+"; color: "+linkColour+"; \\\" onclick=\\\"doNav(\"+i+\");\\\"><u>\"+pageMap[i]+\"</u></a><br>\"+preMap[i]+\"...<br><br>\";");
d.write("				 resultscount++;");
d.write("			}");
d.write("}");
d.write("document.getElementById(\"wpSearchResults\").innerHTML=resultscount+\" "+resultsText+" \"+searchTerms+\"<br><br>\"+results;");
d.write("}");
while(sTerms.indexOf("\"") != -1 ) {
sTerms = sTerms.replace("\"","");
};
d.write("wpDoSearch(\""+sTerms+"\");");
d.write("</script>");
d.write("</body></html>");
d.close();
}