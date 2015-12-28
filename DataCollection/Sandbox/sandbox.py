# -*- coding: UTF-8 -*-
import csv
from datetime import datetime
import time
import re
import multiprocessing

from bs4 import BeautifulSoup
import requests
# from DataCollection import PagesCreated

__author__ = "lizzybradley"


def collect_pages_created():
	html = "https://tools.wmflabs.org/xtools/pages/?user="
	end_html = "&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=100000"

	username = "%28aeropagitica%29"
	url = html + username + end_html
	# r = requests.get(url)

	# data = r.text

	data = """<!DOCTYPE html> /
			<html>
			<head>
				<title>X!"s tools</title>

				<link rel="stylesheet" type="text/css" href="//tools.wmflabs.org/static/res/bootstrap/3.1.1/css/bootstrap.min.css">
				<link rel="stylesheet" type="text/css" href="//tools.wmflabs.org/xtools/static/css/stylenew.css" />
				<script type="text/javascript" src="//tools.wmflabs.org/xtools/static/sortable.js"></script>

				<!--
					<link rel="stylesheet" type="text/css" href="//tools.wmflabs.org/xtools/static/css/bootstrap.min.css" />
					<link rel="stylesheet" type="text/css" href="//tools.wmflabs.org/xtools/static/css/bootstrap-theme.min.css" />
				-->

				<meta charset="utf-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<meta name="viewport" content="width=device-width, initial-scale=1">

				<script type="text/javascript">
					function switchShow( id, elmnt ) {
						var ff = document.getElementById(id);
						if( ff.style.display == "none" || ff.style.display == undefined ) {
							ff.style.display = "block";
							if(elmnt && id != "xt-notifications") elmnt.innerHTML = "[hide]";
						}
						else{
							ff.style.display = "none";
							if(elmnt && id != "xt-notifications") elmnt.innerHTML = "[show]";
						}
					}
				</script>

				</head>

			<body>

				<div class="navbar navbar-default navbar-top" role="navigation" style="min-height:40px;">
					<div class="container-fluid">
						<div class="navbar-collapse collapse" style="padding-top:5px;">

						<ul class="list-inline">
						<li><a href="//tools.wmflabs.org/xtools" >X!"s Tools</a></li>
						<li><span class="login" ><a href="https://tools.wmflabs.org/xtools/oauthredirector.php?action=login&callto=https://en.wikipedia.org/w/api.php&returnto=http://tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000" >Log in</a></span></li>
						<li><a title="XAgent configuration" href="//tools.wmflabs.org/xtools/agent/config.php"><img style="vertical-align:baseline" src="//tools.wmflabs.org/xtools/static/images/Blue_Fedora_hat_12.png" /> XAgent</a>&nbsp;&nbsp;</li>
						<li></li>
						<li><a title="Your echo notifications from 800+ wikis" href="//tools.wmflabs.org/xtools/echo/"><img style="vertical-align:bottom;padding-right:4px;" src="//tools.wmflabs.org/xtools/static/images/Echo_Icon_18.png" />XEcho</a>&nbsp;&nbsp;</li>
						</ul>
								</div>
						<div class="navbar-collapse collapse">
							<ul class="nav navbar-nav navbar-left">
								<li class="" >			<a href="//tools.wmflabs.org/xtools-ec/" title="Edit Counter">Edit Counter</a></li>
								<li class="" >	<a href="//tools.wmflabs.org/xtools-articleinfo/" title="Page history" >Page history</a></li>
								<li class="active" >			<a href="//tools.wmflabs.org/xtools/pages/" title="Pages created" >Pages created</a></li>
								<li class="" >		<a href="//tools.wmflabs.org/xtools/topedits/" title="Top edits" >Top edits</a></li>
								<li class="" >	<a href="//tools.wmflabs.org/xtools/rangecontribs/" title="Range contribs">Range Contributions</a></li>
								<li class="" >			<a href="//tools.wmflabs.org/xtools/blame/" title="Article blamer" >Article blamer</a></li>

							<!-- <li class="" >		<a href="//tools.wmflabs.org/xtools/autoedits/" title="Automated edits" >Automated edits</a></li>  -->
								<li class="" >		<a href="//tools.wmflabs.org/xtools/autoblock/" title="Autoblock" >Autoblock</a></li>
								<li class="" >	<a href="//tools.wmflabs.org/xtools/adminstats/" title="AdminStats" >AdminStats</a></li>
								<li class="" >			<a href="//tools.wmflabs.org/xtools/rfa/" title="RfX" >RfX Analysis</a></li>
								<li class="" >			<a href="//tools.wmflabs.org/xtools/rfap/" title="RfX Vote">RfX Vote Calculator</a></li>
							<!-- <li class="" >			<a href="//tools.wmflabs.org/xtools/bash/">RQ</a></li>  -->
								<li class="" >			<a href="//tools.wmflabs.org/xtools/sc" title="SC" >Quick, Dirty, Simple Edit Counter</a></li>

							</ul>
						</div>
					</div>
				</div>
				<div class="container-fluid text-center" style="margin-top: -10px;margin-bottom:10px;">

						<span  style="margin-right:5px" >(<a class="alert-link" href="//translatewiki.net/w/i.php?title=Special:MessageGroupStats&language=en&group=tsint-xtools&setlang=en" >Translate</a>)</span>
						<span>Select language: </span><a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=af" title="Afrikaans" >af</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ak" title="Akan" >ak</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=am" title="አማርኛ" >am</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ar" title="العربية" >ar</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=arc" title="ܐܪܡܝܐ" >arc</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=as" title="অসমীয়া" >as</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ast" title="asturianu" >ast</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=az" title="azərbaycanca" >az</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=azb" title="تۆرکجه" >azb</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ba" title="башҡортса" >ba</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=bbc-latn" title="Batak Toba" >bbc-latn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=be" title="беларуская" >be</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=be-tarask" title="беларуская (тарашкевіца)‎" >be-tarask</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=bg" title="български" >bg</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=bgn" title="بلوچی رخشانی" >bgn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=bjn" title="Bahasa Banjar" >bjn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=bn" title="বাংলা" >bn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=br" title="brezhoneg" >br</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=bs" title="bosanski" >bs</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=bxr" title="буряад" >bxr</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ca" title="català" >ca</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ce" title="нохчийн" >ce</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ckb" title="کوردیی ناوەندی" >ckb</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=cs" title="čeština" >cs</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=cv" title="Чӑвашла" >cv</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=cy" title="Cymraeg" >cy</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=da" title="dansk" >da</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=de" title="Deutsch" >de</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=de-formal" title="Deutsch (Sie-Form)‎" >de-formal</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=diq" title="Zazaki" >diq</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=dsb" title="dolnoserbski" >dsb</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=egl" title="Emiliàn" >egl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=el" title="Ελληνικά" >el</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=eml" title="emiliàn e rumagnòl" >eml</a> &middot;&nbsp;<span title="English" >en</span> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=en-ca" title="Canadian English" >en-ca</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=en-gb" title="British English" >en-gb</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=eo" title="Esperanto" >eo</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=es" title="español" >es</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=et" title="eesti" >et</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=eu" title="euskara" >eu</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=fa" title="فارسی" >fa</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=fi" title="suomi" >fi</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=fo" title="føroyskt" >fo</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=fr" title="français" >fr</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=frp" title="arpetan" >frp</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=frr" title="Nordfriisk" >frr</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=fy" title="Frysk" >fy</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ga" title="Gaeilge" >ga</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=gl" title="galego" >gl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=gor" title="" >gor</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=grc" title="Ἀρχαία ἑλληνικὴ" >grc</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=gu" title="ગુજરાતી" >gu</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=he" title="עברית" >he</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=hi" title="हिन्दी" >hi</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=hr" title="hrvatski" >hr</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=hsb" title="hornjoserbsce" >hsb</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ht" title="Kreyòl ayisyen" >ht</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=hu" title="magyar" >hu</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=hy" title="Հայերեն" >hy</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ia" title="interlingua" >ia</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=id" title="Bahasa Indonesia" >id</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ig" title="Igbo" >ig</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ilo" title="Ilokano" >ilo</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=inh" title="ГӀалгӀай" >inh</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=is" title="íslenska" >is</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=it" title="italiano" >it</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ja" title="日本語" >ja</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=jv" title="Basa Jawa" >jv</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ka" title="ქართული" >ka</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=kk-cyrl" title="қазақша (кирил)‎" >kk-cyrl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=km" title="ភាសាខ្មែរ" >km</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=kn" title="ಕನ್ನಡ" >kn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ko" title="한국어" >ko</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ksh" title="Ripoarisch" >ksh</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ku-latn" title="Kurdî (latînî)‎" >ku-latn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ky" title="Кыргызча" >ky</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=la" title="Latina" >la</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=lb" title="Lëtzebuergesch" >lb</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=lez" title="лезги" >lez</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=lrc" title="لوری مینجایی" >lrc</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=lt" title="lietuvių" >lt</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=lv" title="latviešu" >lv</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=lzh" title="文言" >lzh</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=lzz" title="Lazuri" >lzz</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=map-bms" title="Basa Banyumasan" >map-bms</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=mg" title="Malagasy" >mg</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=min" title="Baso Minangkabau" >min</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=mk" title="македонски" >mk</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ml" title="മലയാളം" >ml</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=mn" title="монгол" >mn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=mr" title="मराठी" >mr</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ms" title="Bahasa Melayu" >ms</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=mt" title="Malti" >mt</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=my" title="မြန်မာဘာသာ" >my</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=mzn" title="مازِرونی" >mzn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nah" title="Nāhuatl" >nah</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nap" title="Napulitano" >nap</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nb" title="norsk bokmål" >nb</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nds" title="Plattdüütsch" >nds</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nds-nl" title="Nedersaksies" >nds-nl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ne" title="नेपाली" >ne</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=new" title="नेपाल भाषा" >new</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nl" title="Nederlands" >nl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nl-informal" title="Nederlands (informeel)‎" >nl-informal</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=nn" title="norsk nynorsk" >nn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=no" title="norsk bokmål" >no</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=oc" title="occitan" >oc</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=olo" title="" >olo</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=or" title="ଓଡ଼ିଆ" >or</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=os" title="Ирон" >os</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pa" title="ਪੰਜਾਬੀ" >pa</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pdc" title="Deitsch" >pdc</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pfl" title="Pälzisch" >pfl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pi" title="पालि" >pi</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pl" title="polski" >pl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pms" title="Piemontèis" >pms</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ps" title="پښتو" >ps</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pt" title="português" >pt</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=pt-br" title="português do Brasil" >pt-br</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=qqq" title="English" >qqq</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=qu" title="Runa Simi" >qu</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ro" title="română" >ro</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=roa-tara" title="tarandíne" >roa-tara</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ru" title="русский" >ru</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=rue" title="русиньскый" >rue</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sa" title="संस्कृतम्" >sa</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sah" title="саха тыла" >sah</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sco" title="Scots" >sco</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sh" title="srpskohrvatski / српскохрватски" >sh</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=shy-latn" title="" >shy-latn</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=si" title="සිංහල" >si</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sk" title="slovenčina" >sk</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sl" title="slovenščina" >sl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=so" title="Soomaaliga" >so</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sq" title="shqip" >sq</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sr-ec" title="српски (ћирилица)‎" >sr-ec</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sr-el" title="srpski (latinica)‎" >sr-el</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sv" title="svenska" >sv</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=sw" title="Kiswahili" >sw</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ta" title="தமிழ்" >ta</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=te" title="తెలుగు" >te</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tet" title="tetun" >tet</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=th" title="ไทย" >th</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ti" title="ትግርኛ" >ti</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tl" title="Tagalog" >tl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tly" title="толышә зывон" >tly</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tr" title="Türkçe" >tr</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tt" title="татарча/tatarça" >tt</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tt-cyrl" title="татарча" >tt-cyrl</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ttt" title="" >ttt</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tyv" title="тыва дыл" >tyv</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=tzm" title="ⵜⴰⵎⴰⵣⵉⵖⵜ" >tzm</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ug-arab" title="ئۇيغۇرچە" >ug-arab</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=uk" title="українська" >uk</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=ur" title="اردو" >ur</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=uz" title="oʻzbekcha/ўзбекча" >uz</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=vi" title="Tiếng Việt" >vi</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=wuu" title="吴语" >wuu</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=yi" title="ייִדיש" >yi</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=zea" title="Zeêuws" >zea</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=zh-hans" title="中文（简体）‎" >zh-hans</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=zh-hant" title="中文（繁體）‎" >zh-hant</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=zh-hk" title="中文（香港）‎" >zh-hk</a> &middot;&nbsp;<a style="display:inline-block;padding: 0px; text-align:center" href="//tools.wmflabs.org/xtools/pages/?user=%28aeropagitica%29&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=1000&uselang=zh-tw" title="中文（台灣）‎" >zh-tw</a> 	</div>

				<div class="container-fluid" style="margin-top: -10px;margin-bottom:10px;">
					<p class="alert alert-info xt-alert">
						&#9733;&nbsp; Try: <a class="alert-link" href="//meta.wikimedia.org/wiki/User:Hedonil/XTools" >XTools gadget</a>. It"s fast. Enjoy!&nbsp;&bull;&nbsp;
						&nbsp;&bull;&nbsp;#Featured: <a class="alert-link" href="http://tools.wmflabs.org/directory/?view=web" >Directory NG</a>  &#9733;
					  </p>									</div>

				<div class="container-fluid" id="content">


				<div class="panel panel-primary" style="text-align:center">
					<div class="panel-heading">
						<p class="xt-heading-top" >
							<a href="http://en.wikipedia.org/wiki/User:%28aeropagitica%29">(aeropagitica)</a>
							<small><span style="padding-left:10px;" > &bull;&nbsp; en.wikipedia.org </span></small>
						</p>
					</div>
					<div class="panel-body xt-panel-body-top" >
						<p>
							<a href="//en.wikipedia.org/w/index.php?title=Special%3ALog&type=block&user=&page=User%3A%28aeropagitica%29&year=&month=-1&tagfilter=" >block log</a> &middot;
							<a href="//tools.wmflabs.org/xtools/ec/?user=%28aeropagitica%29&lang=en&wiki=wikipedia" >Edit Counter</a> &middot;
							<a href="//tools.wmflabs.org/guc/?user=%28aeropagitica%29" >Global user contributions</a> &middot;
							<a href="//tools.wmflabs.org/wikiviewstats/?lang=en&wiki=wikipedia&page=User:%28aeropagitica%29*" >Pageviews in userspace</a> &middot;
						</p>

						<div class="panel panel-default">
							<div class="panel-heading">
								<h4>Namespace Totals <span class="showhide" onclick="javascript:switchShow( "nstotals", this )">[hide]</span></h4>
							</div>
							<div class="panel-body" id="nstotals">
								<p style="margin-top: 0px;" >
								<table class="table-condensed xt-table">
									<tr><td>Namespace:</td><td>일반 문서 (0)</td></tr>
									<tr><td>Redirects:</td><td>Include redirects and non-redirects</td></tr>
								</table>
								</p>
								<table>
									<tr>
									<td>
									<table class="leantable table-condensed xt-table"  >
										<tr>
										<th>Namespace</th>
										<th>Pages</th>
										<th style="padding_left:5px">Redirects</th>
										<th style="padding_left:5px">Deleted</th>
										</tr>

						<tr>
						<td style="padding-right:10px">
							<span class=legendicon style="background-color:#Cc0000"> </span>
							<a href="#0" >일반 문서</a>
						</td>
						<td class=tdnum >77</td>
						<td class=tdnum >55</td>
						<td class=tdnum >0</td>
						</tr>

						<tr>
						<td style="border-top:3px double silver;" ></td>
						<td class=tdnum style="border-top:3px double silver" ><strong>77</strong></td>
						<td class=tdnum style="border-top:3px double silver" >55</td>
						<td class=tdnum style="border-top:3px double silver" ></td>
						</tr>

									</table>
									</td>
									<td style="padding-left:50px;">
										<img height="140px" src="data:image/png;base64,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" alt="some graph" />
									</td>
									</tr>
								</table>
								<br />
							</div>
						</div>

						<div class="panel panel-default">
							<div class="panel-heading">
								<h4>Pages created <span class="showhide" onclick="javascript:switchShow( "pagescreated", this )">[hide]</span></h4>
							</div>
							<div class="panel-body" id="pagescreated">
								<table class="table-condensed xt-table" >
									<tr ><td colspan=22 ><h3 id=0 >일반 문서</h3></td></tr>
								<tr>
								<td>1.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Idiomotor_effect?redirect=no" >Idiomotor effect</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2008-08-20</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Idiomotor_effect" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Idiomotor_effect" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Idiomotor_effect" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>2.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Infected?redirect=no" >Infected</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2007-05-13</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Infected" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Infected" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Infected" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>3.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Before_the_Devil_knows_your_dead?redirect=no" >Before the Devil knows your dead</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2007-02-04</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Before_the_Devil_knows_your_dead" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Before_the_Devil_knows_your_dead" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Before_the_Devil_knows_your_dead" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>4.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Khull%28Noor-abad%29?redirect=no" >Khull(Noor-abad)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-12-10</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Khull%28Noor-abad%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Khull%28Noor-abad%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Khull%28Noor-abad%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>5.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Doctor_Who_The_Veiled_Lepord?redirect=no" >Doctor Who The Veiled Lepord</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Doctor_Who_The_Veiled_Lepord" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Doctor_Who_The_Veiled_Lepord" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Doctor_Who_The_Veiled_Lepord" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>6.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Sheffield_Tigers_%28Speedway%29?redirect=no" >Sheffield Tigers (Speedway)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-11-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Sheffield_Tigers_%28Speedway%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Sheffield_Tigers_%28Speedway%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Sheffield_Tigers_%28Speedway%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>7.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Battle_of_Vyazma%22?redirect=no" >Battle of Vyazma"</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-10-23</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Battle_of_Vyazma%22" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Battle_of_Vyazma%22" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Battle_of_Vyazma%22" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>8.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Torn%28Battlestar_Galactica%29?redirect=no" >Torn(Battlestar Galactica)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-10-17</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Torn%28Battlestar_Galactica%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Torn%28Battlestar_Galactica%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Torn%28Battlestar_Galactica%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>9.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Accounting_reference_date?redirect=no" >Accounting reference date</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-10-07</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Accounting_reference_date" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Accounting_reference_date" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Accounting_reference_date" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>10.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/The_Royal_High_School?redirect=no" >The Royal High School</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-10-06</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=The_Royal_High_School" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=The_Royal_High_School" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=The_Royal_High_School" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>11.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Sugar%28album%29?redirect=no" >Sugar(album)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-10-01</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Sugar%28album%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Sugar%28album%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Sugar%28album%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>12.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Broads?redirect=no" >Broads</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-09-12</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Broads" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Broads" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Broads" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>13.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Moon_Hoax_Theory?redirect=no" >Moon Hoax Theory</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-09-12</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Moon_Hoax_Theory" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Moon_Hoax_Theory" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Moon_Hoax_Theory" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>14.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Oakes_Park?redirect=no" >Oakes Park</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-09-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Oakes_Park" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Oakes_Park" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Oakes_Park" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>15.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Matrimonial_sites?redirect=no" >Matrimonial sites</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-09-02</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Matrimonial_sites" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Matrimonial_sites" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Matrimonial_sites" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>16.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Gobos?redirect=no" >Gobos</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-09-01</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Gobos" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Gobos" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Gobos" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>17.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Bubblehash?redirect=no" >Bubblehash</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-08-31</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Bubblehash" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Bubblehash" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Bubblehash" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>18.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Friend_Bear?redirect=no" >Friend Bear</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-08-31</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Friend_Bear" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Friend_Bear" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Friend_Bear" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>19.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/X-Fighters?redirect=no" >X-Fighters</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-08-31</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=X-Fighters" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=X-Fighters" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=X-Fighters" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>20.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Centralia_mine_blast?redirect=no" >Centralia mine blast</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-08-31</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Centralia_mine_blast" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Centralia_mine_blast" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Centralia_mine_blast" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>21.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Etagni%C3%A9res?redirect=no" >Etagniéres</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-08-30</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Etagni%C3%A9res" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Etagni%C3%A9res" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Etagni%C3%A9res" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>22.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Ultramodern?redirect=no" >Ultramodern</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-08-28</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Ultramodern" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Ultramodern" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Ultramodern" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>23.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Anna_Hingley?redirect=no" >Anna Hingley</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-08-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Anna_Hingley" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Anna_Hingley" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Anna_Hingley" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>24.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Gnat_line?redirect=no" >Gnat line</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-07-20</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Gnat_line" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Gnat_line" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Gnat_line" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>25.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Scott_Brown%28footballer%29?redirect=no" >Scott Brown(footballer)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-07-16</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Scott_Brown%28footballer%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Scott_Brown%28footballer%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Scott_Brown%28footballer%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>26.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/MUSAC?redirect=no" >MUSAC</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-07-14</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=MUSAC" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=MUSAC" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=MUSAC" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>27.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Jedi_religon?redirect=no" >Jedi religon</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-06-18</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Jedi_religon" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Jedi_religon" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Jedi_religon" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>28.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Harriet_fier?redirect=no" >Harriet fier</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-06-16</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Harriet_fier" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Harriet_fier" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Harriet_fier" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>29.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/DIRECT_MANIPULATION_ANIMATION?redirect=no" >DIRECT MANIPULATION ANIMATION</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-05-30</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=DIRECT_MANIPULATION_ANIMATION" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=DIRECT_MANIPULATION_ANIMATION" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=DIRECT_MANIPULATION_ANIMATION" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>30.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/OBJECT_ANIMATION?redirect=no" >OBJECT ANIMATION</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-05-30</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=OBJECT_ANIMATION" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=OBJECT_ANIMATION" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=OBJECT_ANIMATION" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>31.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Neil_cutler?redirect=no" >Neil cutler</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-04-23</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Neil_cutler" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Neil_cutler" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Neil_cutler" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>32.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Bulotu?redirect=no" >Bulotu</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-04-08</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Bulotu" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Bulotu" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Bulotu" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>33.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Auahi-Turoa?redirect=no" >Auahi-Turoa</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-04-08</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Auahi-Turoa" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Auahi-Turoa" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Auahi-Turoa" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>34.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Hahau-Whenua?redirect=no" >Hahau-Whenua</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-04-08</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Hahau-Whenua" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Hahau-Whenua" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Hahau-Whenua" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>35.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/I%27i?redirect=no" >I"i</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-04-08</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=I%27i" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=I%27i" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=I%27i" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>36.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Kuala_Lumpur_City_Centre?redirect=no" >Kuala Lumpur City Centre</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-04-07</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Kuala_Lumpur_City_Centre" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Kuala_Lumpur_City_Centre" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Kuala_Lumpur_City_Centre" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>37.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Miranda_hart?redirect=no" >Miranda hart</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-04-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Miranda_hart" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Miranda_hart" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Miranda_hart" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>38.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Electra_%28pleiade%29?redirect=no" >Electra (pleiade)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-03-27</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Electra_%28pleiade%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Electra_%28pleiade%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Electra_%28pleiade%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>39.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Star-Fury?redirect=no" >Star-Fury</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-03-19</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Star-Fury" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Star-Fury" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Star-Fury" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>40.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Roman_pucinski?redirect=no" >Roman pucinski</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-03-19</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Roman_pucinski" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Roman_pucinski" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Roman_pucinski" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>41.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Lobster_neuberg?redirect=no" >Lobster neuberg</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-03-12</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Lobster_neuberg" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Lobster_neuberg" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Lobster_neuberg" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>42.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Fort_baker?redirect=no" >Fort baker</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-03-09</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Fort_baker" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Fort_baker" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Fort_baker" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>43.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Heidi_postlewait?redirect=no" >Heidi postlewait</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-03-08</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Heidi_postlewait" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Heidi_postlewait" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Heidi_postlewait" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>44.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Ray_french?redirect=no" >Ray french</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-03-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Ray_french" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Ray_french" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Ray_french" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>45.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Poelaert?redirect=no" >Poelaert</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-02-08</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Poelaert" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Poelaert" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Poelaert" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>46.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Coen_river?redirect=no" >Coen river</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-02-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Coen_river" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Coen_river" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Coen_river" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>47.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Alma_baldwin?redirect=no" >Alma baldwin</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-02-01</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Alma_baldwin" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Alma_baldwin" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Alma_baldwin" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>48.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Tom_nugent?redirect=no" >Tom nugent</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-01-25</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Tom_nugent" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Tom_nugent" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Tom_nugent" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>49.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Pascal_smet?redirect=no" >Pascal smet</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-01-24</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Pascal_smet" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Pascal_smet" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Pascal_smet" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>50.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Scott_mayer?redirect=no" >Scott mayer</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-01-24</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Scott_mayer" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Scott_mayer" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Scott_mayer" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>51.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Lichner%2C_Heinrich?redirect=no" >Lichner, Heinrich</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-01-20</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Lichner%2C_Heinrich" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Lichner%2C_Heinrich" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Lichner%2C_Heinrich" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>52.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Malaysian_Center_for_Remote_Sensing?redirect=no" >Malaysian Center for Remote Sensing</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-01-04</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Malaysian_Center_for_Remote_Sensing" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Malaysian_Center_for_Remote_Sensing" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Malaysian_Center_for_Remote_Sensing" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>53.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Nuri_demirag?redirect=no" >Nuri demirag</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2006-01-01</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Nuri_demirag" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Nuri_demirag" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Nuri_demirag" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>54.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Precious_Cargo_%28Enterprise_Episode%29?redirect=no" >Precious Cargo (Enterprise Episode)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-06</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Precious_Cargo_%28Enterprise_Episode%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Precious_Cargo_%28Enterprise_Episode%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Precious_Cargo_%28Enterprise_Episode%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>55.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/The_Catwalk_%28Enterprise_Episode%29?redirect=no" >The Catwalk (Enterprise Episode)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-06</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=The_Catwalk_%28Enterprise_Episode%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=The_Catwalk_%28Enterprise_Episode%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=The_Catwalk_%28Enterprise_Episode%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>56.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/The_Catwalk?redirect=no" >The Catwalk</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=The_Catwalk" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=The_Catwalk" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=The_Catwalk" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>57.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Precious_Cargo?redirect=no" >Precious Cargo</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Precious_Cargo" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Precious_Cargo" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Precious_Cargo" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>58.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Vanishing_Point_%28Star_Trek%3A_Enterprise%29?redirect=no" >Vanishing Point (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Vanishing_Point_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Vanishing_Point_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Vanishing_Point_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>59.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Singularity_%28Star_Trek%3A_Enterprise%29?redirect=no" >Singularity (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Singularity_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Singularity_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Singularity_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>60.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/The_Communicator_%28Star_Trek%3A_Enterprise%29?redirect=no" >The Communicator (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=The_Communicator_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=The_Communicator_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=The_Communicator_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>61.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/The_Seventh?redirect=no" >The Seventh</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=The_Seventh" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=The_Seventh" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=The_Seventh" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>62.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Shockwave_Part_II_%28Enterprise_episode%29?redirect=no" >Shockwave Part II (Enterprise episode)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-05</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Shockwave_Part_II_%28Enterprise_episode%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Shockwave_Part_II_%28Enterprise_episode%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Shockwave_Part_II_%28Enterprise_episode%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>63.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Shockwave_%28Star_Trek%3A_Enterprise%29?redirect=no" >Shockwave (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-04</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Shockwave_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Shockwave_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Shockwave_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>64.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Two_Days_and_Two_Nights?redirect=no" >Two Days and Two Nights</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-04</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Two_Days_and_Two_Nights" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Two_Days_and_Two_Nights" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Two_Days_and_Two_Nights" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>65.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Desert_Crossing?redirect=no" >Desert Crossing</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-04</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Desert_Crossing" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Desert_Crossing" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Desert_Crossing" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>66.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Fallen_Hero_%28Star_Trek%3A_Enterprise%29?redirect=no" >Fallen Hero (Star Trek: Enterprise)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-04</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Fallen_Hero_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Fallen_Hero_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Fallen_Hero_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>67.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Vox_Sola?redirect=no" >Vox Sola</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-04</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Vox_Sola" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Vox_Sola" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Vox_Sola" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>68.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Detained_%28Star_Trek%3A_Enterprise%29?redirect=no" >Detained (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Detained_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Detained_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Detained_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>69.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Oasis_%28Star_Trek%3A_Enterprise%29?redirect=no" >Oasis (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Oasis_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Oasis_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Oasis_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>70.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Acquisition_%28Star_Trek%3A_Enterprise%29?redirect=no" >Acquisition (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Acquisition_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Acquisition_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Acquisition_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>71.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Rogue_Planet_%28Star_Trek%3A_Enterprise%29?redirect=no" >Rogue Planet (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Rogue_Planet_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Rogue_Planet_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Rogue_Planet_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>72.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Fusion_%28Star_Trek%3A_Enterprise%29?redirect=no" >Fusion (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Fusion_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Fusion_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Fusion_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>73.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Shuttlepod_One?redirect=no" >Shuttlepod One</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Shuttlepod_One" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Shuttlepod_One" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Shuttlepod_One" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>74.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Sleeping_Dogs_%28Star_Trek%3A_Enterprise%29?redirect=no" >Sleeping Dogs (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Sleeping_Dogs_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Sleeping_Dogs_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Sleeping_Dogs_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>75.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Dear_Doctor?redirect=no" >Dear Doctor</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-03</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Dear_Doctor" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Dear_Doctor" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Dear_Doctor" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>76.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/Silent_Enemy_%28Star_Trek%3A_Enterprise%29?redirect=no" >Silent Enemy (Star Trek: Enterprise)</a>  </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-12-02</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=Silent_Enemy_%28Star_Trek%3A_Enterprise%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=Silent_Enemy_%28Star_Trek%3A_Enterprise%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=Silent_Enemy_%28Star_Trek%3A_Enterprise%29" ><small>topedits</small></a></td>

								</tr>

								<tr>
								<td>77.</td>
								<td style="max-width:50%; white-space:wrap; word-wrap:break-word" ><a href="//en.wikipedia.org/wiki/We%27ll_Always_Have_Paris_%28TNG_Episode%29?redirect=no" >We"ll Always Have Paris (TNG Episode)</a> <small> &middot; (redirect)</small> </td>
								<td style="white-space: nowrap; font-size:95%; padding-right:10px;" >2005-09-01</td>
								<td style="white-space: nowrap" ><a href="//en.wikipedia.org/w/index.php?title=Special:Log&type=&page=We%27ll_Always_Have_Paris_%28TNG_Episode%29" ><small>log</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/articleinfo/?lang=en&wiki=wikipedia&page=We%27ll_Always_Have_Paris_%28TNG_Episode%29" ><small>page history</small></a> &middot; </td>
								<td style="white-space: nowrap" ><a href="//tools.wmflabs.org/xtools/topedits/?lang=en&wiki=wikipedia&user=%28aeropagitica%29&page=We%27ll_Always_Have_Paris_%28TNG_Episode%29" ><small>topedits</small></a></td>

								</tr>

								</table>
							</div>
						</div>
					</div>
				</div>

					<div class="container-fluid">
						<span><small><span>Executed in 0.37 second(s).</span> &middot; <span>Taken 13 megabytes of memory to execute. (Peak: 14.75)</span></small></span>
						<hr style="margin:5px 10px;" />
						<div class="row">
							<div class="col">
								<span>&copy; 2008-2015 &middot; </span>
								<a href="//en.wikipedia.org/wiki/User:Cyberpower678"><b>Cyberpower678</b></a> &middot;
								<a href="//de.wikipedia.org/wiki/User:Hedonil">Hedonil</a> &middot;
								<a href="//en.wikipedia.org/wiki/User:MusikAnimal"><b>MusikAnimal</b></a> &middot;
								<a href="//en.wikipedia.org/wiki/User:Technical 13"><b>Technical 13</b></a> &middot;
								<a href="//en.wikipedia.org/wiki/User:TParis">TParis</a> &middot;
								<a href="//en.wikipedia.org/wiki/User:X!">X!</a> &bull;
								<a href="//github.com/x-Tools/xtools/" >View Source</a> &bull; 					<a href="//github.com/x-Tools/xtools/issues" >Bugs</a> &bull; 					<a href="irc://irc.freenode.net/#wikimedia-labs" >#wikimedia-labs</a>
								<span><sup><a  style="color:green" href="https://webchat.freenode.net/?channels=#wikimedia-labs">WebChat</a></sup></span><br />
								<span>Translations are powered by <a href="//translatewiki.net/" >translatewiki.net</a> and <a href="//tools.wmflabs.org/intuition/#tab-about" >Intuition</a>.</span>
							</div>
							<div class="col pull-right">
								<a style="margin-right:5px;" href="//translatewiki.net/?setlang=en "><img height="36px" src="//upload.wikimedia.org/wikipedia/commons/5/51/Translatewiki.net_logo.svg" alt="translatewiki.net logo"/></a>
								<a href="//tools.wmflabs.org"><img height="40px" src="//tools.wmflabs.org/xtools/static/images/labs.png" alt="Powered by WMF Labs" /></a>
							</div>
						</div>
					</div>
				</div>
				<br />
				<br />

			<script>
				if (window.sortables_init) sortables_init();
			</script>
			<script>
				</script>

			</body>
			</html>"""

	soup = BeautifulSoup(data)

	trs = soup.find_all("tr")

	last_num = trs[-1].td.string[:-1]
	first_num = 0

	pattern = re.compile("[0-9]+.")
	for tr in reversed(trs):
		if tr.td is not None:
			if tr.td.string is not None and pattern.match(tr.td.string):
				date = tr.contents[5].text

				date = datetime.strptime(date, "%Y-%m-%d")
				if date < datetime.strptime("2006", "%Y"):
					first_num = tr.td.string[:-1]
				else:
					break

	num_pages_created = int(last_num) - int(first_num) + 1
	print num_pages_created


def append_pages_created():
	v = open('short.csv')
	r = csv.reader(v)
	row0 = r.next()
	row0.append('content_pages_created')

	items = []

	for item in r:
		username = item[0]
		election_date = datetime.strptime(item[1], "%Y-%m-%d %H:%M:%S")
		pages_created = get_pages_created(username, election_date)
		item.append(pages_created)
		items.append(item)
		print(item)

	with open('short2.csv', 'w') as toWrite:
		writer = csv.writer(toWrite, delimiter=',')
		writer.writerow(row0)
		for item in items:
			writer.writerow(item)


def get_pages_created(username, election_date):
	html = "https://tools.wmflabs.org/xtools/pages/?user="
	end_html = "&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=100000"

	url = html + username + end_html
	r = requests.get(url)

	data = r.text

	soup = BeautifulSoup(data)

	trs = soup.find_all("tr")

	last_num = trs[-1].td.string[:-1]
	first_num = 0

	pattern = re.compile("[0-9]+.")
	for tr in reversed(trs):
		if tr.td is not None:
			if tr.td.string is not None and pattern.match(tr.td.string):
				date = tr.contents[5].text

				date = datetime.strptime(date, "%Y-%m-%d")
				if date < election_date:
					first_num = tr.td.string[:-1]
				else:
					break

	num_pages_created = int(last_num) - int(first_num) + 1
	return num_pages_created

#pc = PagesCreated()
#pc.append_pages_created("short.csv", "test.csv")

def foo(n):
	time.sleep(n)
	print "successfully waited"

def run():
	p = multiprocessing.Process(target=foo, name='Foo', args=(5,))

	p.start()

	p.join(4)

	# Terminate
	if p.is_alive():
		print "Timed out!"
		p.terminate()
		p.join()

run()