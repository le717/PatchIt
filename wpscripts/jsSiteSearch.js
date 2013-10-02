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
d.write("var wordMap = new Array(\" patchit standard simple package install lego® racers mods welcome here will find information support help topics about created triangle717 continually does best update with latest greatest features ability modifications 1999 video game completely open-source application released under that means that read source code made involved development free software annoy offers trial-ware applications charge fears some random piece junk being loaded your system what download truly what \",\" \",\" installing patch install patchit simply load press select patch after reading information confirm installation will automatically into your lego® racers loco depending game created need unsure about everything successfully resources page \",\" creating patch create patchit load press select video game creaed enter your patch's patchs name version author description point files will compress them into archive file write details stable later automatically filters stops illegal from being compressed complete this process found github both items name version filename located same folder uncompressed check format documentation complete have made lego® loco need screen resolution used this important played different some elements destroying hard work making \",\" support request feature submit code download release patchit please http github le717 report issues state attach your file located program files logs attaching will ensure bugs found quicker easier released sooner installing there ways install onto computer installer standard this location with start menu desktop shortcut although both optional also portable meaning that used flash drive setup installation folder above directory hold shift right-click press open command window here type name append portable=1 \",\" \",\" resources following sites programs helpful your patchit documentation extras patches started lego® racers extractor extracts builds lego setting installing tutorial jimbobjeffers rock raiders united only place learn everything need know about modding python programming language written rioforce designer creator graphics website \",\" about patchit python application written triangle717 standard simple package install lego® racers mods plan although still it's earlier stages modding many have already being developed there needs them which heavily influenced based patchman installer 1999 data design interactive game rock raiders fills that void credits creator logo graphics website designer rioforce alan cirevam cyrem hobino jimbobjeffers olivus prime robexplorien xiron awesome people united sharing their gameplay tips supporting development special thanks jrmastermodelbuilder thedoctor programming help suggestions without would exist makes uses extractor copyright 2012 released under runasadmin 2013 quantumcd license \",\" patchit compatible banner click larger image small media html source bbcode this page copy source either size icons your patch's patchs website informational display respective image \");");
d.write("var pageMap = new Array(\"Home\",\"Search Results\",\"Installing a Patch\",\"Creating a Patch\",\"Support\",\"Change Log\",\"Resources\",\"About\",\"Media\");");
d.write("var linkMap = new Array(\"index.html\",\"search.html\",\"install.html\",\"create.html\",\"support.html\",\"changes.html\",\"resources.html\",\"about.html\",\"media.html\");");
d.write("var preMap = new Array(\"“ ” PatchIt! The standard and simple way to package and install LEGO® Racers mods. Welcome to PatchIt! Here, you will find information, support, and help topics about PatchIt! PatchIt! is created by T\",\"\",\"Installing a Patch To install a PatchIt! Patch, simply load PatchIt!, press the i key, select the PiP patch, and after reading the Patch information, confirm the installation. PatchIt! will automati\",\"Creating a Patch To create a PatchIt! Patch, load PatchIt! and press the c key. Select the video game it is creaed for, and enter your Patchs Name, Version, Author, and Description. Point it to you\",\"Support To request a feature, submit a code fix, or download a new release of PatchIt!, please go to http://github.com/le717/PatchIt. To submit a bug report, please go to http://github.com/le717/Patch\",\"\",\"Resources The following sites and programs may be helpful to you and in your use of PatchIt! • PatchIt! Documentation • PatchIt! Extras: Patches to get you started! • LEGO® Racers JAM Extractor: Extra\",\"About PatchIt! is a Python 3 application written by Triangle717  as the standard and simple way to package and install LEGO® Racers mods. The Plan Although LEGO® Racers is still in it’s earlier stages\",\"PatchIt! Compatible Banner (Click for Larger Image)  PatchIt! Compatible Banner (Small)  (Click for Larger Image) Media HTML Source BBCode Source HTML Source BBCode Source On this page, you can copy H\");");
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