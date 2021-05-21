%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-i
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1240:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonts-tlwg.tar.xz
Source1241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonts-tlwg.doc.tar.xz
Source1389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyhdr.tar.xz
Source1390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyhdr.doc.tar.xz
Source1391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fix2col.tar.xz
Source1392:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fix2col.doc.tar.xz
Source1449:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fbs.tar.xz
Source1450:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figbib.tar.xz
Source1451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figbib.doc.tar.xz
Source1452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footbib.tar.xz
Source1453:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footbib.doc.tar.xz
Source1455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/francais-bst.tar.xz
Source1456:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/francais-bst.doc.tar.xz
Source1831:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fbb.tar.xz
Source1832:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fbb.doc.tar.xz
Source1833:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fdsymbol.tar.xz
Source1834:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fdsymbol.doc.tar.xz
Source1836:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fetamont.tar.xz
Source1837:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fetamont.doc.tar.xz
Source1839:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feyn.tar.xz
Source1840:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feyn.doc.tar.xz
Source1842:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fge.tar.xz
Source1843:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fge.doc.tar.xz
Source1845:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fira.tar.xz
Source1846:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fira.doc.tar.xz
Source1847:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/foekfont.tar.xz
Source1848:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/foekfont.doc.tar.xz
Source1849:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonetika.tar.xz
Source1850:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonetika.doc.tar.xz
Source1851:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontawesome.tar.xz
Source1852:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontawesome.doc.tar.xz
Source1853:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontmfizz.tar.xz
Source1854:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontmfizz.doc.tar.xz
Source1857:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fourier.tar.xz
Source1858:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fourier.doc.tar.xz
Source1860:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fouriernc.tar.xz
Source1861:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fouriernc.doc.tar.xz
Source1862:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frcursive.tar.xz
Source1863:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frcursive.doc.tar.xz
Source2128:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fpl.tar.xz
Source2129:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fpl.doc.tar.xz
Source2280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fenixpar.tar.xz
Source2281:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fenixpar.doc.tar.xz
Source2282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fltpoint.tar.xz
Source2283:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fltpoint.doc.tar.xz
Source2285:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fntproof.tar.xz
Source2286:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fntproof.doc.tar.xz
Source2346:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontname.tar.xz
Source2347:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontname.doc.tar.xz
Source2490:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fc.tar.xz
Source2491:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fc.doc.tar.xz
Source2518:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fandol.tar.xz
Source2519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fandol.doc.tar.xz
Source2608:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/FAQ-en.doc.tar.xz
Source2615:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/first-latex-doc.doc.tar.xz
Source2666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/finbib.tar.xz
Source2713:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/facture.tar.xz
Source2714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/facture.doc.tar.xz
Source2716:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frletter.tar.xz
Source2717:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frletter.doc.tar.xz
Source2750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fifinddo-info.doc.tar.xz
Source2853:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyhdr-it.doc.tar.xz
Source2854:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixltxhyph.tar.xz
Source2855:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixltxhyph.doc.tar.xz
Source2857:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frontespizio.tar.xz
Source2858:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frontespizio.doc.tar.xz
Source2976:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feupphdteses.tar.xz
Source2977:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feupphdteses.doc.tar.xz
Source3013:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancybox.tar.xz
Source3014:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancybox.doc.tar.xz
Source3015:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyref.tar.xz
Source3016:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyref.doc.tar.xz
Source3018:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyvrb.tar.xz
Source3019:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyvrb.doc.tar.xz
Source3021:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/float.tar.xz
Source3022:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/float.doc.tar.xz
Source3024:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontspec.tar.xz
Source3025:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontspec.doc.tar.xz
Source3033:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fp.tar.xz
Source3034:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fp.doc.tar.xz
Source3145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fast-diagram.tar.xz
Source3146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fast-diagram.doc.tar.xz
Source3149:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fitbox.tar.xz
Source3150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fitbox.doc.tar.xz
Source3152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flowchart.tar.xz
Source3153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flowchart.doc.tar.xz
Source3155:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forest.tar.xz
Source3156:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forest.doc.tar.xz
Source3949:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/facsimile.tar.xz
Source3950:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/facsimile.doc.tar.xz
Source3952:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/factura.tar.xz
Source3953:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/factura.doc.tar.xz
Source3955:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancylabel.tar.xz
Source3956:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancylabel.doc.tar.xz
Source3958:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancynum.tar.xz
Source3959:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancynum.doc.tar.xz
Source3961:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancypar.tar.xz
Source3962:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancypar.doc.tar.xz
Source3964:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyslides.tar.xz
Source3965:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancyslides.doc.tar.xz
Source3966:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancytabs.tar.xz
Source3967:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancytabs.doc.tar.xz
Source3969:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancytooltips.tar.xz
Source3970:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fancytooltips.doc.tar.xz
Source3972:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fcolumn.tar.xz
Source3973:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fcolumn.doc.tar.xz
Source3975:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fifo-stack.tar.xz
Source3976:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fifo-stack.doc.tar.xz
Source3978:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figsize.tar.xz
Source3979:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figsize.doc.tar.xz
Source3980:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filecontents.tar.xz
Source3981:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filecontents.doc.tar.xz
Source3983:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filedate.tar.xz
Source3984:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filedate.doc.tar.xz
Source3986:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filehook.tar.xz
Source3987:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filehook.doc.tar.xz
Source3989:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fileinfo.tar.xz
Source3990:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fileinfo.doc.tar.xz
Source3992:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filemod.tar.xz
Source3993:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filemod.doc.tar.xz
Source3994:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fink.tar.xz
Source3995:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fink.doc.tar.xz
Source3997:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/finstrut.tar.xz
Source3998:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/finstrut.doc.tar.xz
Source4000:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fithesis.tar.xz
Source4001:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fithesis.doc.tar.xz
Source4003:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixfoot.tar.xz
Source4004:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixfoot.doc.tar.xz
Source4005:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixme.tar.xz
Source4006:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixme.doc.tar.xz
Source4008:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixmetodonotes.tar.xz
Source4009:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixmetodonotes.doc.tar.xz
Source4011:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fjodor.tar.xz
Source4012:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fjodor.doc.tar.xz
Source4013:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flabels.tar.xz
Source4014:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flabels.doc.tar.xz
Source4016:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flacards.tar.xz
Source4017:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flacards.doc.tar.xz
Source4018:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flagderiv.tar.xz
Source4019:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flagderiv.doc.tar.xz
Source4021:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flashcards.tar.xz
Source4022:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flashcards.doc.tar.xz
Source4024:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flashmovie.tar.xz
Source4025:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flashmovie.doc.tar.xz
Source4026:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flipbook.tar.xz
Source4027:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flipbook.doc.tar.xz
Source4028:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flippdf.tar.xz
Source4029:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flippdf.doc.tar.xz
Source4031:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/floatflt.tar.xz
Source4032:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/floatflt.doc.tar.xz
Source4034:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/floatrow.tar.xz
Source4035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/floatrow.doc.tar.xz
Source4037:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flowfram.tar.xz
Source4038:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/flowfram.doc.tar.xz
Source4040:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fmp.tar.xz
Source4041:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fmp.doc.tar.xz
Source4043:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fmtcount.tar.xz
Source4044:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fmtcount.doc.tar.xz
Source4046:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fn2end.tar.xz
Source4047:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fn2end.doc.tar.xz
Source4048:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnbreak.tar.xz
Source4049:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnbreak.doc.tar.xz
Source4051:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fncychap.tar.xz
Source4052:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fncychap.doc.tar.xz
Source4053:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fncylab.tar.xz
Source4054:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fncylab.doc.tar.xz
Source4055:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnpara.tar.xz
Source4056:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnpara.doc.tar.xz
Source4057:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnpct.tar.xz
Source4058:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnpct.doc.tar.xz
Source4059:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnumprint.tar.xz
Source4060:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnumprint.doc.tar.xz
Source4062:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/foilhtml.tar.xz
Source4063:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/foilhtml.doc.tar.xz
Source4065:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontaxes.tar.xz
Source4066:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontaxes.doc.tar.xz
Source4068:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonttable.tar.xz
Source4069:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonttable.doc.tar.xz
Source4071:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footmisc.tar.xz
Source4072:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footmisc.doc.tar.xz
Source4074:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnotebackref.tar.xz
Source4075:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnotebackref.doc.tar.xz
Source4076:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnoterange.tar.xz
Source4077:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnoterange.doc.tar.xz
Source4079:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnpag.tar.xz
Source4080:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnpag.doc.tar.xz
Source4082:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forarray.tar.xz
Source4083:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forarray.doc.tar.xz
Source4085:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/foreign.tar.xz
Source4086:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/foreign.doc.tar.xz
Source4088:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forloop.tar.xz
Source4089:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forloop.doc.tar.xz
Source4091:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/formlett.tar.xz
Source4092:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/formlett.doc.tar.xz
Source4093:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/formular.tar.xz
Source4094:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/formular.doc.tar.xz
Source4096:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fragments.tar.xz
Source4097:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fragments.doc.tar.xz
Source4098:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frame.tar.xz
Source4099:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frame.doc.tar.xz
Source4100:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/framed.tar.xz
Source4101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/framed.doc.tar.xz
Source4102:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frankenstein.tar.xz
Source4103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frankenstein.doc.tar.xz
Source4105:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frege.tar.xz
Source4106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frege.doc.tar.xz
Source4107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ftcap.tar.xz
Source4108:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ftcap.doc.tar.xz
Source4109:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ftnxtra.tar.xz
Source4110:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ftnxtra.doc.tar.xz
Source4112:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fullblck.tar.xz
Source4113:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fullblck.doc.tar.xz
Source4115:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fullminipage.tar.xz
Source4116:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fullminipage.doc.tar.xz
Source4118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fullwidth.tar.xz
Source4119:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fullwidth.doc.tar.xz
Source4120:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fundus-calligra.tar.xz
Source4121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fundus-calligra.doc.tar.xz
Source4123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fundus-cyr.tar.xz
Source4124:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fundus-sueterlin.tar.xz
Source4125:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fundus-sueterlin.doc.tar.xz
Source4127:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fwlw.tar.xz
Source4128:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fwlw.doc.tar.xz
Source5844:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/faktor.tar.xz
Source5845:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/faktor.doc.tar.xz
Source5960:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/featpost.tar.xz
Source5961:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/featpost.doc.tar.xz
Source5962:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feynmf.tar.xz
Source5963:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feynmf.doc.tar.xz
Source5965:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feynmp-auto.tar.xz
Source5966:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/feynmp-auto.doc.tar.xz
Source6024:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figbas.tar.xz
Source6025:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figbas.doc.tar.xz
Source6077:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figflow.tar.xz
Source6078:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/figflow.doc.tar.xz
Source6079:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixpdfmag.tar.xz
Source6080:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/font-change.tar.xz
Source6081:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/font-change.doc.tar.xz
Source6082:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontch.tar.xz
Source6083:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontch.doc.tar.xz
Source6376:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fbithesis.tar.xz
Source6377:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fbithesis.doc.tar.xz
Source6379:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fcavtex.tar.xz
Source6380:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fcavtex.doc.tar.xz
Source6381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fcltxdoc.tar.xz
Source6382:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fcltxdoc.doc.tar.xz
Source6384:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fei.tar.xz
Source6385:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fei.doc.tar.xz
Source6660:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fouridx.tar.xz
Source6661:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fouridx.doc.tar.xz
Source6663:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/functan.tar.xz
Source6664:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/functan.doc.tar.xz
Source6750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixlatvian.tar.xz
Source6751:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixlatvian.doc.tar.xz
Source6753:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontbook.tar.xz
Source6754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontbook.doc.tar.xz
Source6756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontwrap.tar.xz
Source6757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontwrap.doc.tar.xz
Source7332:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ffslides.tar.xz
Source7333:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ffslides.doc.tar.xz
Source7334:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fibeamer.tar.xz
Source7335:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fibeamer.doc.tar.xz
Source7337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixcmex.tar.xz
Source7338:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixcmex.doc.tar.xz
Source7340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/font-change-xetex.tar.xz
Source7341:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/font-change-xetex.doc.tar.xz
Source7342:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnotehyper.tar.xz
Source7343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footnotehyper.doc.tar.xz
Source7578:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonts-churchslavonic.tar.xz
Source7579:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fonts-churchslavonic.doc.tar.xz
Source7743:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fetchcls.tar.xz
Source7744:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fetchcls.doc.tar.xz
Source7745:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fgruler.tar.xz
Source7746:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fgruler.doc.tar.xz
Source7747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filecontentsdef.tar.xz
Source7748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/filecontentsdef.doc.tar.xz
Source7749:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixjfm.tar.xz
Source7750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fixjfm.doc.tar.xz
Source7751:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontloader-luaotfload.tar.xz
Source7752:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontloader-luaotfload.doc.tar.xz
Source7753:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footmisx.tar.xz
Source7754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/footmisx.doc.tar.xz
Source7756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forest-quickstart.doc.tar.xz
Source7757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forms16be.tar.xz
Source7758:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/forms16be.doc.tar.xz
Source7759:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frederika2016.tar.xz
Source7760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/frederika2016.doc.tar.xz
Source8030:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fvextra.tar.xz
Source8031:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fvextra.doc.tar.xz
Source8144:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fduthesis.tar.xz
Source8145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fduthesis.doc.tar.xz
Source8146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnspe.tar.xz
Source8147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fnspe.doc.tar.xz
Source8148:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontawesome5.tar.xz
Source8149:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontawesome5.doc.tar.xz
Source8150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/formation-latex-ul.tar.xz
Source8151:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/formation-latex-ul.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-fonts-tlwg
Provides:       tex-fonts-tlwg = %{tl_version}
License:        GPL+
Summary:        Thai fonts for LaTeX from TLWG
Version:        svn47499
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       texlive-tlwg = %{epoch}:%{tl_version}
Obsoletes:      texlive-tlwg < %{epoch}:%{tl_version}
Provides:       tex(lthtlwg.enc) = %{tl_version}, tex(nectec.map) = %{tl_version}
Provides:       tex(nf.map) = %{tl_version}, tex(sipa.map) = %{tl_version}
Provides:       tex(tlwg.map) = %{tl_version}, tex(garuda.tfm) = %{tl_version}
Provides:       tex(garuda_b.tfm) = %{tl_version}, tex(garuda_bo.tfm) = %{tl_version}
Provides:       tex(garuda_o.tfm) = %{tl_version}, tex(kinnari.tfm) = %{tl_version}
Provides:       tex(kinnari_b.tfm) = %{tl_version}, tex(kinnari_bi.tfm) = %{tl_version}
Provides:       tex(kinnari_bo.tfm) = %{tl_version}, tex(kinnari_i.tfm) = %{tl_version}
Provides:       tex(kinnari_o.tfm) = %{tl_version}, tex(laksaman.tfm) = %{tl_version}
Provides:       tex(laksaman_b.tfm) = %{tl_version}, tex(laksaman_bi.tfm) = %{tl_version}
Provides:       tex(laksaman_i.tfm) = %{tl_version}, tex(loma.tfm) = %{tl_version}
Provides:       tex(loma_b.tfm) = %{tl_version}, tex(loma_bo.tfm) = %{tl_version}
Provides:       tex(loma_o.tfm) = %{tl_version}, tex(norasi.tfm) = %{tl_version}
Provides:       tex(norasi_b.tfm) = %{tl_version}, tex(norasi_bi.tfm) = %{tl_version}
Provides:       tex(norasi_bo.tfm) = %{tl_version}, tex(norasi_i.tfm) = %{tl_version}
Provides:       tex(norasi_o.tfm) = %{tl_version}, tex(purisa.tfm) = %{tl_version}
Provides:       tex(purisa_b.tfm) = %{tl_version}, tex(purisa_bo.tfm) = %{tl_version}
Provides:       tex(purisa_o.tfm) = %{tl_version}, tex(rgaruda.tfm) = %{tl_version}
Provides:       tex(rgaruda_b.tfm) = %{tl_version}, tex(rgaruda_bo.tfm) = %{tl_version}
Provides:       tex(rgaruda_o.tfm) = %{tl_version}, tex(rkinnari.tfm) = %{tl_version}
Provides:       tex(rkinnari_b.tfm) = %{tl_version}, tex(rkinnari_bi.tfm) = %{tl_version}
Provides:       tex(rkinnari_bo.tfm) = %{tl_version}, tex(rkinnari_i.tfm) = %{tl_version}
Provides:       tex(rkinnari_o.tfm) = %{tl_version}, tex(rlaksaman.tfm) = %{tl_version}
Provides:       tex(rlaksaman_b.tfm) = %{tl_version}, tex(rlaksaman_bi.tfm) = %{tl_version}
Provides:       tex(rlaksaman_i.tfm) = %{tl_version}, tex(rloma.tfm) = %{tl_version}
Provides:       tex(rloma_b.tfm) = %{tl_version}, tex(rloma_bo.tfm) = %{tl_version}
Provides:       tex(rloma_o.tfm) = %{tl_version}, tex(rnorasi.tfm) = %{tl_version}
Provides:       tex(rnorasi_b.tfm) = %{tl_version}, tex(rnorasi_bi.tfm) = %{tl_version}
Provides:       tex(rnorasi_bo.tfm) = %{tl_version}, tex(rnorasi_i.tfm) = %{tl_version}
Provides:       tex(rnorasi_o.tfm) = %{tl_version}, tex(rpurisa.tfm) = %{tl_version}
Provides:       tex(rpurisa_b.tfm) = %{tl_version}, tex(rpurisa_bo.tfm) = %{tl_version}
Provides:       tex(rpurisa_o.tfm) = %{tl_version}, tex(rsawasdee.tfm) = %{tl_version}
Provides:       tex(rsawasdee_b.tfm) = %{tl_version}, tex(rsawasdee_bo.tfm) = %{tl_version}
Provides:       tex(rsawasdee_o.tfm) = %{tl_version}, tex(rttype.tfm) = %{tl_version}
Provides:       tex(rttype_b.tfm) = %{tl_version}, tex(rttype_bo.tfm) = %{tl_version}
Provides:       tex(rttype_o.tfm) = %{tl_version}, tex(rttypist.tfm) = %{tl_version}
Provides:       tex(rttypist_b.tfm) = %{tl_version}, tex(rttypist_bo.tfm) = %{tl_version}
Provides:       tex(rttypist_o.tfm) = %{tl_version}, tex(rumpush.tfm) = %{tl_version}
Provides:       tex(rumpush_b.tfm) = %{tl_version}, tex(rumpush_bo.tfm) = %{tl_version}
Provides:       tex(rumpush_l.tfm) = %{tl_version}, tex(rumpush_lo.tfm) = %{tl_version}
Provides:       tex(rumpush_o.tfm) = %{tl_version}, tex(rwaree.tfm) = %{tl_version}
Provides:       tex(rwaree_b.tfm) = %{tl_version}, tex(rwaree_bo.tfm) = %{tl_version}
Provides:       tex(rwaree_o.tfm) = %{tl_version}, tex(sawasdee.tfm) = %{tl_version}
Provides:       tex(sawasdee_b.tfm) = %{tl_version}, tex(sawasdee_bo.tfm) = %{tl_version}
Provides:       tex(sawasdee_o.tfm) = %{tl_version}, tex(ttype.tfm) = %{tl_version}
Provides:       tex(ttype_b.tfm) = %{tl_version}, tex(ttype_bo.tfm) = %{tl_version}
Provides:       tex(ttype_o.tfm) = %{tl_version}, tex(ttypist.tfm) = %{tl_version}
Provides:       tex(ttypist_b.tfm) = %{tl_version}, tex(ttypist_bo.tfm) = %{tl_version}
Provides:       tex(ttypist_o.tfm) = %{tl_version}, tex(umpush.tfm) = %{tl_version}
Provides:       tex(umpush_b.tfm) = %{tl_version}, tex(umpush_bo.tfm) = %{tl_version}
Provides:       tex(umpush_l.tfm) = %{tl_version}, tex(umpush_lo.tfm) = %{tl_version}
Provides:       tex(umpush_o.tfm) = %{tl_version}, tex(waree.tfm) = %{tl_version}
Provides:       tex(waree_b.tfm) = %{tl_version}, tex(waree_bo.tfm) = %{tl_version}
Provides:       tex(waree_o.tfm) = %{tl_version}, tex(garuda.pfb) = %{tl_version}
Provides:       tex(garuda_b.pfb) = %{tl_version}, tex(garuda_bo.pfb) = %{tl_version}
Provides:       tex(garuda_o.pfb) = %{tl_version}, tex(kinnari.pfb) = %{tl_version}
Provides:       tex(kinnari_b.pfb) = %{tl_version}, tex(kinnari_bi.pfb) = %{tl_version}
Provides:       tex(kinnari_bo.pfb) = %{tl_version}, tex(kinnari_i.pfb) = %{tl_version}
Provides:       tex(kinnari_o.pfb) = %{tl_version}, tex(laksaman.pfb) = %{tl_version}
Provides:       tex(laksaman_b.pfb) = %{tl_version}, tex(laksaman_bi.pfb) = %{tl_version}
Provides:       tex(laksaman_i.pfb) = %{tl_version}, tex(loma.pfb) = %{tl_version}
Provides:       tex(loma_b.pfb) = %{tl_version}, tex(loma_bo.pfb) = %{tl_version}
Provides:       tex(loma_o.pfb) = %{tl_version}, tex(norasi.pfb) = %{tl_version}
Provides:       tex(norasi_b.pfb) = %{tl_version}, tex(norasi_bi.pfb) = %{tl_version}
Provides:       tex(norasi_bo.pfb) = %{tl_version}, tex(norasi_i.pfb) = %{tl_version}
Provides:       tex(norasi_o.pfb) = %{tl_version}, tex(purisa.pfb) = %{tl_version}
Provides:       tex(purisa_b.pfb) = %{tl_version}, tex(purisa_bo.pfb) = %{tl_version}
Provides:       tex(purisa_o.pfb) = %{tl_version}, tex(sawasdee.pfb) = %{tl_version}
Provides:       tex(sawasdee_b.pfb) = %{tl_version}, tex(sawasdee_bo.pfb) = %{tl_version}
Provides:       tex(sawasdee_o.pfb) = %{tl_version}, tex(ttype.pfb) = %{tl_version}
Provides:       tex(ttype_b.pfb) = %{tl_version}, tex(ttype_bo.pfb) = %{tl_version}
Provides:       tex(ttype_o.pfb) = %{tl_version}, tex(ttypist.pfb) = %{tl_version}
Provides:       tex(ttypist_b.pfb) = %{tl_version}, tex(ttypist_bo.pfb) = %{tl_version}
Provides:       tex(ttypist_o.pfb) = %{tl_version}, tex(umpush.pfb) = %{tl_version}
Provides:       tex(umpush_b.pfb) = %{tl_version}, tex(umpush_bo.pfb) = %{tl_version}
Provides:       tex(umpush_l.pfb) = %{tl_version}, tex(umpush_lo.pfb) = %{tl_version}
Provides:       tex(umpush_o.pfb) = %{tl_version}, tex(waree.pfb) = %{tl_version}
Provides:       tex(waree_b.pfb) = %{tl_version}, tex(waree_bo.pfb) = %{tl_version}
Provides:       tex(waree_o.pfb) = %{tl_version}, tex(garuda.vf) = %{tl_version}
Provides:       tex(garuda_b.vf) = %{tl_version}, tex(garuda_bo.vf) = %{tl_version}
Provides:       tex(garuda_o.vf) = %{tl_version}, tex(kinnari.vf) = %{tl_version}
Provides:       tex(kinnari_b.vf) = %{tl_version}, tex(kinnari_bi.vf) = %{tl_version}
Provides:       tex(kinnari_bo.vf) = %{tl_version}, tex(kinnari_i.vf) = %{tl_version}
Provides:       tex(kinnari_o.vf) = %{tl_version}, tex(laksaman.vf) = %{tl_version}
Provides:       tex(laksaman_b.vf) = %{tl_version}, tex(laksaman_bi.vf) = %{tl_version}
Provides:       tex(laksaman_i.vf) = %{tl_version}, tex(loma.vf) = %{tl_version}
Provides:       tex(loma_b.vf) = %{tl_version}, tex(loma_bo.vf) = %{tl_version}
Provides:       tex(loma_o.vf) = %{tl_version}, tex(norasi.vf) = %{tl_version}
Provides:       tex(norasi_b.vf) = %{tl_version}, tex(norasi_bi.vf) = %{tl_version}
Provides:       tex(norasi_bo.vf) = %{tl_version}, tex(norasi_i.vf) = %{tl_version}
Provides:       tex(norasi_o.vf) = %{tl_version}, tex(purisa.vf) = %{tl_version}
Provides:       tex(purisa_b.vf) = %{tl_version}, tex(purisa_bo.vf) = %{tl_version}
Provides:       tex(purisa_o.vf) = %{tl_version}, tex(sawasdee.vf) = %{tl_version}
Provides:       tex(sawasdee_b.vf) = %{tl_version}, tex(sawasdee_bo.vf) = %{tl_version}
Provides:       tex(sawasdee_o.vf) = %{tl_version}, tex(ttype.vf) = %{tl_version}
Provides:       tex(ttype_b.vf) = %{tl_version}, tex(ttype_bo.vf) = %{tl_version}
Provides:       tex(ttype_o.vf) = %{tl_version}, tex(ttypist.vf) = %{tl_version}
Provides:       tex(ttypist_b.vf) = %{tl_version}, tex(ttypist_bo.vf) = %{tl_version}
Provides:       tex(ttypist_o.vf) = %{tl_version}, tex(umpush.vf) = %{tl_version}
Provides:       tex(umpush_b.vf) = %{tl_version}, tex(umpush_bo.vf) = %{tl_version}
Provides:       tex(umpush_l.vf) = %{tl_version}, tex(umpush_lo.vf) = %{tl_version}
Provides:       tex(umpush_o.vf) = %{tl_version}, tex(waree.vf) = %{tl_version}
Provides:       tex(waree_b.vf) = %{tl_version}, tex(waree_bo.vf) = %{tl_version}
Provides:       tex(waree_o.vf) = %{tl_version}, tex(fonts-tlwg.sty) = %{tl_version}
Provides:       tex(lthgaruda.fd) = %{tl_version}, tex(lthkinnari.fd) = %{tl_version}
Provides:       tex(lthlaksaman.fd) = %{tl_version}, tex(lthloma.fd) = %{tl_version}
Provides:       tex(lthnorasi.fd) = %{tl_version}, tex(lthpurisa.fd) = %{tl_version}
Provides:       tex(lthsawasdee.fd) = %{tl_version}, tex(lthttype.fd) = %{tl_version}
Provides:       tex(lthttypist.fd) = %{tl_version}, tex(lthumpush.fd) = %{tl_version}
Provides:       tex(lthwaree.fd) = %{tl_version}

%description -n texlive-fonts-tlwg
A collection of free Thai fonts, supplied as FontForge sources,
and with LaTeX .fd files. This package depends on the thailatex
package.

%package -n texlive-fonts-tlwg-doc
Summary:        Documentation for fonts-tlwg
Version:        svn47499
Provides:       tex-fonts-tlwg-doc
AutoReqProv:    No

%description -n texlive-fonts-tlwg-doc
Documentation for fonts-tlwg

%package -n texlive-fancyhdr
Provides:       tex-fancyhdr = %{tl_version}
License:        LPPL
Summary:        Extensive control of page headers and footers in LaTeX2e
Version:        svn44730
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(extramarks.sty) = %{tl_version}, tex(fancyhdr.sty) = %{tl_version}
Provides:       tex(fancyheadings.sty) = %{tl_version}

%description -n texlive-fancyhdr
The package provides extensive facilities, both for
constructing headers and footers, and for controlling their use
(for example, at times when LaTeX would automatically change
the heading style in use).

%package -n texlive-fancyhdr-doc
Summary:        Documentation for fancyhdr
Version:        svn44730
Provides:       tex-fancyhdr-doc
AutoReqProv:    No

%description -n texlive-fancyhdr-doc
Documentation for fancyhdr

%package -n texlive-fix2col
Provides:       tex-fix2col = %{tl_version}
License:        LPPL
Summary:        Fix miscellaneous two column mode features
Version:        svn38770

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fix2col.sty) = %{tl_version}

%description -n texlive-fix2col
Fix mark handling so that \firstmark is taken from the first
column if that column has any marks at all; keep two column
floats like figure* in sequence with single column floats like
figure.

%package -n texlive-fix2col-doc
Summary:        Documentation for fix2col
Version:        svn38770

Provides:       tex-fix2col-doc
AutoReqProv:    No

%description -n texlive-fix2col-doc
Documentation for fix2col

%package -n texlive-fbs
Provides:       tex-fbs = %{tl_version}
License:        LPPL
Summary:        BibTeX style for Frontiers in Bioscience
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-fbs
A BibTeX style file made with custom-bib to fit Frontiers in
Bioscience requirements: all authors, no et al, full author
names, initials abbreviated; only abbreviated journal name
italicised, no abbreviation dots; only year, no month, at end
of reference; and DOI excluded, ISSN excluded.

%package -n texlive-figbib
Provides:       tex-figbib = %{tl_version}
License:        LPPL
Summary:        Organize figure databases with BibTeX
Version:        svn19388.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(figbib.sty) = %{tl_version}

%description -n texlive-figbib
FigBib lets you organize your figures in BibTeX databases. Some
FigBib features are: Store and manage figures in a BibTeX
database; Include figures in your LaTeX document with one short
command; Generate a List of Figures containing more/other
information than the figure captions; Control with one switch
where to output the figures, either as usual float objects or
in a separate part at the end of your document.

%package -n texlive-figbib-doc
Summary:        Documentation for figbib
Version:        svn19388.0

Provides:       tex-figbib-doc
AutoReqProv:    No

%description -n texlive-figbib-doc
Documentation for figbib

%package -n texlive-footbib
Provides:       tex-footbib = %{tl_version}
License:        LPPL
Summary:        Bibliographic references as footnotes
Version:        svn17115.2.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(footbib.sty) = %{tl_version}

%description -n texlive-footbib
The package makes bibliographic references appear as footnotes.
It defines a command \footcite which is similar to the LaTeX
\cite command but the references cited in this way appear at
the bottom of the pages. This 'foot bibliography' does not
conflict with the standard one and both may exist
simultaneously in a document. The command \cite may still be
used to produce the standard bibliography. The foot
bibliography uses its own style and bibliographic database
which may be specified independently of the standard one. Any
standard bibliography style may be used.

%package -n texlive-footbib-doc
Summary:        Documentation for footbib
Version:        svn17115.2.0.7

Provides:       tex-footbib-doc
AutoReqProv:    No

%description -n texlive-footbib-doc
Documentation for footbib

%package -n texlive-francais-bst
Provides:       tex-francais-bst = %{tl_version}
License:        LPPL 1.3
Summary:        Bibliographies conforming to French typographic standards
Version:        svn38922

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-francais-bst
The package provides bibliographies (in French) conforming to
the rules in "Guide de la communication ecrite" (Malo, M.,
Quebec Amerique, 1996. ISBN 978-2-8903-7875-9) The BibTeX
styles were generated using custom-bib and they are compatible
with natbib

%package -n texlive-francais-bst-doc
Summary:        Documentation for francais-bst
Version:        svn38922

Provides:       tex-francais-bst-doc
AutoReqProv:    No

%description -n texlive-francais-bst-doc
Documentation for francais-bst

%package -n texlive-fbb
Provides:       tex-fbb = %{tl_version}
License:        OFL
Summary:        A free Bembo-like font
Version:        svn45277
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(ifetex.sty), tex(etoolbox.sty), tex(mweights.sty)
Requires:       tex(fontaxes.sty), tex(xkeyval.sty)
Provides:       tex(fbb_2xteu2.enc) = %{tl_version}, tex(fbb_3pafo2.enc) = %{tl_version}
Provides:       tex(fbb_3q7523.enc) = %{tl_version}, tex(fbb_3szmnl.enc) = %{tl_version}
Provides:       tex(fbb_3t72qi.enc) = %{tl_version}, tex(fbb_47nzug.enc) = %{tl_version}
Provides:       tex(fbb_4eykqf.enc) = %{tl_version}, tex(fbb_4fm2lh.enc) = %{tl_version}
Provides:       tex(fbb_4phrex.enc) = %{tl_version}, tex(fbb_5kfdlm.enc) = %{tl_version}
Provides:       tex(fbb_5yuftp.enc) = %{tl_version}, tex(fbb_646rxv.enc) = %{tl_version}
Provides:       tex(fbb_6wf2yd.enc) = %{tl_version}, tex(fbb_7ftbhc.enc) = %{tl_version}
Provides:       tex(fbb_bbqv4h.enc) = %{tl_version}, tex(fbb_bjcd27.enc) = %{tl_version}
Provides:       tex(fbb_cglacz.enc) = %{tl_version}, tex(fbb_ciz6qs.enc) = %{tl_version}
Provides:       tex(fbb_dfjaoq.enc) = %{tl_version}, tex(fbb_dli7xt.enc) = %{tl_version}
Provides:       tex(fbb_do4apa.enc) = %{tl_version}, tex(fbb_dppuce.enc) = %{tl_version}
Provides:       tex(fbb_eaddwb.enc) = %{tl_version}, tex(fbb_fefik6.enc) = %{tl_version}
Provides:       tex(fbb_fmiu37.enc) = %{tl_version}, tex(fbb_gia3f7.enc) = %{tl_version}
Provides:       tex(fbb_gti7xr.enc) = %{tl_version}, tex(fbb_h4gxkq.enc) = %{tl_version}
Provides:       tex(fbb_h4yzgv.enc) = %{tl_version}, tex(fbb_icb62t.enc) = %{tl_version}
Provides:       tex(fbb_iqrulf.enc) = %{tl_version}, tex(fbb_k4t5oa.enc) = %{tl_version}
Provides:       tex(fbb_k67ydz.enc) = %{tl_version}, tex(fbb_k6hjgp.enc) = %{tl_version}
Provides:       tex(fbb_lahflm.enc) = %{tl_version}, tex(fbb_lqd7qz.enc) = %{tl_version}
Provides:       tex(fbb_ms7h4m.enc) = %{tl_version}, tex(fbb_nakqlt.enc) = %{tl_version}
Provides:       tex(fbb_nyched.enc) = %{tl_version}, tex(fbb_p2khiw.enc) = %{tl_version}
Provides:       tex(fbb_p6sgcp.enc) = %{tl_version}, tex(fbb_pg3xpw.enc) = %{tl_version}
Provides:       tex(fbb_pjzzzk.enc) = %{tl_version}, tex(fbb_pkrngd.enc) = %{tl_version}
Provides:       tex(fbb_pqcug3.enc) = %{tl_version}, tex(fbb_q44qkc.enc) = %{tl_version}
Provides:       tex(fbb_qxzlqe.enc) = %{tl_version}, tex(fbb_r5yodg.enc) = %{tl_version}
Provides:       tex(fbb_tizue6.enc) = %{tl_version}, tex(fbb_tpadeo.enc) = %{tl_version}
Provides:       tex(fbb_u3ego5.enc) = %{tl_version}, tex(fbb_uqncc5.enc) = %{tl_version}
Provides:       tex(fbb_vokwwj.enc) = %{tl_version}, tex(fbb_vvs2t7.enc) = %{tl_version}
Provides:       tex(fbb_w6cgkc.enc) = %{tl_version}, tex(fbb_wmfgc4.enc) = %{tl_version}
Provides:       tex(fbb_wmijbz.enc) = %{tl_version}, tex(fbb_xcuijf.enc) = %{tl_version}
Provides:       tex(fbb_xmsf7g.enc) = %{tl_version}, tex(fbb_yr6epv.enc) = %{tl_version}
Provides:       tex(fbb_zac64m.enc) = %{tl_version}, tex(fbb_zxsywv.enc) = %{tl_version}
Provides:       tex(fbb.map) = %{tl_version}, tex(fbb-Bold.otf) = %{tl_version}
Provides:       tex(fbb-BoldItalic.otf) = %{tl_version}, tex(fbb-Italic.otf) = %{tl_version}
Provides:       tex(fbb-Regular.otf) = %{tl_version}, tex(fbb-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-t1.tfm) = %{tl_version}, tex(fbb-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(fbb-Bold.pfb) = %{tl_version}, tex(fbb-BoldItalic.pfb) = %{tl_version}
Provides:       tex(fbb-Italic.pfb) = %{tl_version}, tex(fbb-Regular.pfb) = %{tl_version}
Provides:       tex(fbb-Bold-lf-ly1.vf) = %{tl_version}, tex(fbb-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-lf-t1.vf) = %{tl_version}, tex(fbb-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-osf-t1.vf) = %{tl_version}, tex(fbb-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-sup-t1.vf) = %{tl_version}, tex(fbb-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tlf-t1.vf) = %{tl_version}, tex(fbb-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(fbb-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(fbb-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1fbb-LF.fd) = %{tl_version}, tex(LY1fbb-OsF.fd) = %{tl_version}
Provides:       tex(LY1fbb-Sup.fd) = %{tl_version}, tex(LY1fbb-TLF.fd) = %{tl_version}
Provides:       tex(LY1fbb-TOsF.fd) = %{tl_version}, tex(OT1fbb-LF.fd) = %{tl_version}
Provides:       tex(OT1fbb-OsF.fd) = %{tl_version}, tex(OT1fbb-Sup.fd) = %{tl_version}
Provides:       tex(OT1fbb-TLF.fd) = %{tl_version}, tex(OT1fbb-TOsF.fd) = %{tl_version}
Provides:       tex(T1fbb-LF.fd) = %{tl_version}, tex(T1fbb-OsF.fd) = %{tl_version}
Provides:       tex(T1fbb-Sup.fd) = %{tl_version}, tex(T1fbb-TLF.fd) = %{tl_version}
Provides:       tex(T1fbb-TOsF.fd) = %{tl_version}, tex(TS1fbb-LF.fd) = %{tl_version}
Provides:       tex(TS1fbb-OsF.fd) = %{tl_version}, tex(TS1fbb-TLF.fd) = %{tl_version}
Provides:       tex(TS1fbb-TOsF.fd) = %{tl_version}, tex(fbb.sty) = %{tl_version}

%description -n texlive-fbb
The package provides a Bembo-like font package based on Cardo
but with many modifications, adding Bold Italic, small caps in
all styles, six figure choices in all styles, updated kerning
tables, added figure tables and corrected f-ligatures. Both
OpenType and Adobe Type 1 versions are provided; all necessary
support files are provided. The font works well with
newtxmath's libertine option.

%package -n texlive-fbb-doc
Summary:        Documentation for fbb
Version:        svn45277
Provides:       tex-fbb-doc
AutoReqProv:    No

%description -n texlive-fbb-doc
Documentation for fbb

%package -n texlive-fdsymbol
Provides:       tex-fdsymbol = %{tl_version}
License:        OFL
Summary:        A maths symbol font
Version:        svn26722.0.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(amsmath.sty), tex(textcomp.sty)
Provides:       tex(fdsymbol-a.enc) = %{tl_version}, tex(fdsymbol-b.enc) = %{tl_version}
Provides:       tex(fdsymbol-c.enc) = %{tl_version}, tex(fdsymbol-d.enc) = %{tl_version}
Provides:       tex(fdsymbol-e.enc) = %{tl_version}, tex(fdsymbol-f.enc) = %{tl_version}
Provides:       tex(fdsymbol.map) = %{tl_version}, tex(FdSymbol-Bold.otf) = %{tl_version}
Provides:       tex(FdSymbol-Book.otf) = %{tl_version}, tex(FdSymbol-Medium.otf) = %{tl_version}
Provides:       tex(FdSymbol-Regular.otf) = %{tl_version}
Provides:       tex(FdSymbolA-Bold.tfm) = %{tl_version}, tex(FdSymbolA-Book.tfm) = %{tl_version}
Provides:       tex(FdSymbolA-Medium.tfm) = %{tl_version}
Provides:       tex(FdSymbolA-Regular.tfm) = %{tl_version}
Provides:       tex(FdSymbolB-Bold.tfm) = %{tl_version}, tex(FdSymbolB-Book.tfm) = %{tl_version}
Provides:       tex(FdSymbolB-Medium.tfm) = %{tl_version}
Provides:       tex(FdSymbolB-Regular.tfm) = %{tl_version}
Provides:       tex(FdSymbolC-Bold.tfm) = %{tl_version}, tex(FdSymbolC-Book.tfm) = %{tl_version}
Provides:       tex(FdSymbolC-Medium.tfm) = %{tl_version}
Provides:       tex(FdSymbolC-Regular.tfm) = %{tl_version}
Provides:       tex(FdSymbolD-Bold.tfm) = %{tl_version}, tex(FdSymbolD-Book.tfm) = %{tl_version}
Provides:       tex(FdSymbolD-Medium.tfm) = %{tl_version}
Provides:       tex(FdSymbolD-Regular.tfm) = %{tl_version}
Provides:       tex(FdSymbolE-Bold.tfm) = %{tl_version}, tex(FdSymbolE-Book.tfm) = %{tl_version}
Provides:       tex(FdSymbolE-Medium.tfm) = %{tl_version}
Provides:       tex(FdSymbolE-Regular.tfm) = %{tl_version}
Provides:       tex(FdSymbolF-Bold.tfm) = %{tl_version}, tex(FdSymbolF-Book.tfm) = %{tl_version}
Provides:       tex(FdSymbolF-Medium.tfm) = %{tl_version}
Provides:       tex(FdSymbolF-Regular.tfm) = %{tl_version}
Provides:       tex(FdSymbolA-Bold.pfb) = %{tl_version}, tex(FdSymbolA-Book.pfb) = %{tl_version}
Provides:       tex(FdSymbolA-Medium.pfb) = %{tl_version}
Provides:       tex(FdSymbolA-Regular.pfb) = %{tl_version}
Provides:       tex(FdSymbolB-Bold.pfb) = %{tl_version}, tex(FdSymbolB-Book.pfb) = %{tl_version}
Provides:       tex(FdSymbolB-Medium.pfb) = %{tl_version}
Provides:       tex(FdSymbolB-Regular.pfb) = %{tl_version}
Provides:       tex(FdSymbolC-Bold.pfb) = %{tl_version}, tex(FdSymbolC-Book.pfb) = %{tl_version}
Provides:       tex(FdSymbolC-Medium.pfb) = %{tl_version}
Provides:       tex(FdSymbolC-Regular.pfb) = %{tl_version}
Provides:       tex(FdSymbolD-Bold.pfb) = %{tl_version}, tex(FdSymbolD-Book.pfb) = %{tl_version}
Provides:       tex(FdSymbolD-Medium.pfb) = %{tl_version}
Provides:       tex(FdSymbolD-Regular.pfb) = %{tl_version}
Provides:       tex(FdSymbolE-Bold.pfb) = %{tl_version}, tex(FdSymbolE-Book.pfb) = %{tl_version}
Provides:       tex(FdSymbolE-Medium.pfb) = %{tl_version}
Provides:       tex(FdSymbolE-Regular.pfb) = %{tl_version}
Provides:       tex(FdSymbolF-Bold.pfb) = %{tl_version}, tex(FdSymbolF-Book.pfb) = %{tl_version}
Provides:       tex(FdSymbolF-Medium.pfb) = %{tl_version}
Provides:       tex(FdSymbolF-Regular.pfb) = %{tl_version}
Provides:       tex(fdsymbol.sty) = %{tl_version}

%description -n texlive-fdsymbol
FdSymbol is a maths symbol font, designed as a companion to the
Fedra family by Typotheque, but it might also fit other
contemporary typefaces.

%package -n texlive-fdsymbol-doc
Summary:        Documentation for fdsymbol
Version:        svn26722.0.8

Provides:       tex-fdsymbol-doc
AutoReqProv:    No

%description -n texlive-fdsymbol-doc
Documentation for fdsymbol

%package -n texlive-fetamont
Provides:       tex-fetamont = %{tl_version}
License:        LPPL 1.3
Summary:        Extended version of Knuth's logo typeface
Version:        svn43812
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(fetamont.map) = %{tl_version}, tex(ffmb10.otf) = %{tl_version}
Provides:       tex(ffmb8.otf) = %{tl_version}, tex(ffmb9.otf) = %{tl_version}
Provides:       tex(ffmbc40.otf) = %{tl_version}, tex(ffmbco40.otf) = %{tl_version}
Provides:       tex(ffmbo10.otf) = %{tl_version}, tex(ffmbo8.otf) = %{tl_version}
Provides:       tex(ffmbo9.otf) = %{tl_version}, tex(ffmbw10.otf) = %{tl_version}
Provides:       tex(ffmbwo10.otf) = %{tl_version}, tex(ffmc10.otf) = %{tl_version}
Provides:       tex(ffmco10.otf) = %{tl_version}, tex(ffmh10.otf) = %{tl_version}
Provides:       tex(ffmh8.otf) = %{tl_version}, tex(ffmh9.otf) = %{tl_version}
Provides:       tex(ffmho10.otf) = %{tl_version}, tex(ffmho8.otf) = %{tl_version}
Provides:       tex(ffmho9.otf) = %{tl_version}, tex(ffmhw10.otf) = %{tl_version}
Provides:       tex(ffmhwo10.otf) = %{tl_version}, tex(ffml10.otf) = %{tl_version}
Provides:       tex(ffmlc10.otf) = %{tl_version}, tex(ffmlco10.otf) = %{tl_version}
Provides:       tex(ffmlo10.otf) = %{tl_version}, tex(ffmlq10.otf) = %{tl_version}
Provides:       tex(ffmlqo10.otf) = %{tl_version}, tex(ffmlw10.otf) = %{tl_version}
Provides:       tex(ffmlwo10.otf) = %{tl_version}, tex(ffmo10.otf) = %{tl_version}
Provides:       tex(ffmo8.otf) = %{tl_version}, tex(ffmo9.otf) = %{tl_version}
Provides:       tex(ffmr10.otf) = %{tl_version}, tex(ffmr8.otf) = %{tl_version}
Provides:       tex(ffmr9.otf) = %{tl_version}, tex(ffmw10.otf) = %{tl_version}
Provides:       tex(ffmwo10.otf) = %{tl_version}, tex(ffmb10.tfm) = %{tl_version}
Provides:       tex(ffmb8.tfm) = %{tl_version}, tex(ffmb9.tfm) = %{tl_version}
Provides:       tex(ffmbc40.tfm) = %{tl_version}, tex(ffmbco40.tfm) = %{tl_version}
Provides:       tex(ffmbo10.tfm) = %{tl_version}, tex(ffmbo8.tfm) = %{tl_version}
Provides:       tex(ffmbo9.tfm) = %{tl_version}, tex(ffmbw10.tfm) = %{tl_version}
Provides:       tex(ffmbwo10.tfm) = %{tl_version}, tex(ffmc10.tfm) = %{tl_version}
Provides:       tex(ffmco10.tfm) = %{tl_version}, tex(ffmh10.tfm) = %{tl_version}
Provides:       tex(ffmh8.tfm) = %{tl_version}, tex(ffmh9.tfm) = %{tl_version}
Provides:       tex(ffmho10.tfm) = %{tl_version}, tex(ffmho8.tfm) = %{tl_version}
Provides:       tex(ffmho9.tfm) = %{tl_version}, tex(ffmhw10.tfm) = %{tl_version}
Provides:       tex(ffmhwo10.tfm) = %{tl_version}, tex(ffml10.tfm) = %{tl_version}
Provides:       tex(ffmlc10.tfm) = %{tl_version}, tex(ffmlco10.tfm) = %{tl_version}
Provides:       tex(ffmlo10.tfm) = %{tl_version}, tex(ffmlq10.tfm) = %{tl_version}
Provides:       tex(ffmlqo10.tfm) = %{tl_version}, tex(ffmlw10.tfm) = %{tl_version}
Provides:       tex(ffmlwo10.tfm) = %{tl_version}, tex(ffmo10.tfm) = %{tl_version}
Provides:       tex(ffmo8.tfm) = %{tl_version}, tex(ffmo9.tfm) = %{tl_version}
Provides:       tex(ffmr10.tfm) = %{tl_version}, tex(ffmr8.tfm) = %{tl_version}
Provides:       tex(ffmr9.tfm) = %{tl_version}, tex(ffmw10.tfm) = %{tl_version}
Provides:       tex(ffmwo10.tfm) = %{tl_version}, tex(ffmb10.pfb) = %{tl_version}
Provides:       tex(ffmb8.pfb) = %{tl_version}, tex(ffmb9.pfb) = %{tl_version}
Provides:       tex(ffmbc40.pfb) = %{tl_version}, tex(ffmbco40.pfb) = %{tl_version}
Provides:       tex(ffmbo10.pfb) = %{tl_version}, tex(ffmbo8.pfb) = %{tl_version}
Provides:       tex(ffmbo9.pfb) = %{tl_version}, tex(ffmbw10.pfb) = %{tl_version}
Provides:       tex(ffmbwo10.pfb) = %{tl_version}, tex(ffmc10.pfb) = %{tl_version}
Provides:       tex(ffmco10.pfb) = %{tl_version}, tex(ffmh10.pfb) = %{tl_version}
Provides:       tex(ffmh8.pfb) = %{tl_version}, tex(ffmh9.pfb) = %{tl_version}
Provides:       tex(ffmho10.pfb) = %{tl_version}, tex(ffmho8.pfb) = %{tl_version}
Provides:       tex(ffmho9.pfb) = %{tl_version}, tex(ffmhw10.pfb) = %{tl_version}
Provides:       tex(ffmhwo10.pfb) = %{tl_version}, tex(ffml10.pfb) = %{tl_version}
Provides:       tex(ffmlc10.pfb) = %{tl_version}, tex(ffmlco10.pfb) = %{tl_version}
Provides:       tex(ffmlo10.pfb) = %{tl_version}, tex(ffmlq10.pfb) = %{tl_version}
Provides:       tex(ffmlqo10.pfb) = %{tl_version}, tex(ffmlw10.pfb) = %{tl_version}
Provides:       tex(ffmlwo10.pfb) = %{tl_version}, tex(ffmo10.pfb) = %{tl_version}
Provides:       tex(ffmo8.pfb) = %{tl_version}, tex(ffmo9.pfb) = %{tl_version}
Provides:       tex(ffmr10.pfb) = %{tl_version}, tex(ffmr8.pfb) = %{tl_version}
Provides:       tex(ffmr9.pfb) = %{tl_version}, tex(ffmw10.pfb) = %{tl_version}
Provides:       tex(ffmwo10.pfb) = %{tl_version}, tex(T1ffm.fd) = %{tl_version}
Provides:       tex(T1ffmw.fd) = %{tl_version}, tex(fetamont.sty) = %{tl_version}

%description -n texlive-fetamont
The fetamont typeface was designed in METAFONT and extends the
Logo fonts to complete the T1 encoding. The designs of the
glyphs A, E, F, M, N, O, P, S and T are based on the METAFONT
constructions by D. E. Knuth. The glyphs Y and 1 imitate the
shapes of the corresponding glyphs in the METATYPE1 logo.

%package -n texlive-fetamont-doc
Summary:        Documentation for fetamont
Version:        svn43812
Provides:       tex-fetamont-doc
AutoReqProv:    No

%description -n texlive-fetamont-doc
Documentation for fetamont

%package -n texlive-feyn
Provides:       tex-feyn = %{tl_version}
License:        GPL+
Summary:        A font for in-text Feynman diagrams
Version:        svn45679
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(feyn10.tfm) = %{tl_version}, tex(feyn11.tfm) = %{tl_version}
Provides:       tex(feyn12.tfm) = %{tl_version}, tex(feyn18.tfm) = %{tl_version}
Provides:       tex(feyn24.tfm) = %{tl_version}, tex(feyntext10.tfm) = %{tl_version}
Provides:       tex(feyntext11.tfm) = %{tl_version}, tex(feyntext12.tfm) = %{tl_version}
Provides:       tex(feyntext18.tfm) = %{tl_version}, tex(feyntext24.tfm) = %{tl_version}
Provides:       tex(feyn.sty) = %{tl_version}

%description -n texlive-feyn
Feyn may be used to produce relatively simple Feynman diagrams
within equations in a LaTeX document. While the feynmf package
is good at drawing large diagrams for figures, the present
package and its fonts allow diagrams within equations or text,
at a matching size. The fonts are distributed as Metafont
source, and macros for their use are also provided.

%package -n texlive-feyn-doc
Summary:        Documentation for feyn
Version:        svn45679
Provides:       tex-feyn-doc
AutoReqProv:    No

%description -n texlive-feyn-doc
Documentation for feyn

%package -n texlive-fge
Provides:       tex-fge = %{tl_version}
License:        LPPL
Summary:        A font for Frege's Grundgesetze der Arithmetik
Version:        svn37628.1.25

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(fge.map) = %{tl_version}, tex(fgeit10.tfm) = %{tl_version}
Provides:       tex(fgerm10.tfm) = %{tl_version}, tex(fgeit10.pfb) = %{tl_version}
Provides:       tex(fgerm10.pfb) = %{tl_version}, tex(Ufgeit.fd) = %{tl_version}
Provides:       tex(Ufgerm.fd) = %{tl_version}, tex(fge.cfg) = %{tl_version}
Provides:       tex(fge.sty) = %{tl_version}

%description -n texlive-fge
The fonts are provided as Metafont source and Adobe Type 1
(pfb) files. A small LaTeX package (fge) is included.

%package -n texlive-fge-doc
Summary:        Documentation for fge
Version:        svn37628.1.25

Provides:       tex-fge-doc
AutoReqProv:    No

%description -n texlive-fge-doc
Documentation for fge

%package -n texlive-fira
Provides:       tex-fira = %{tl_version}
License:        OFL
Summary:        Fira fonts with LaTeX support
Version:        svn47835
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty), tex(fontspec.sty)
Requires:       tex(fontenc.sty), tex(mweights.sty), tex(fontaxes.sty)
Provides:       tex(fir_4k5dce.enc) = %{tl_version}, tex(fir_4vuazg.enc) = %{tl_version}
Provides:       tex(fir_53mytn.enc) = %{tl_version}, tex(fir_5bzluk.enc) = %{tl_version}
Provides:       tex(fir_6j4iko.enc) = %{tl_version}, tex(fir_6jvuba.enc) = %{tl_version}
Provides:       tex(fir_6lpfuz.enc) = %{tl_version}, tex(fir_75hvjh.enc) = %{tl_version}
Provides:       tex(fir_765q6w.enc) = %{tl_version}, tex(fir_ah2d2f.enc) = %{tl_version}
Provides:       tex(fir_cvh4ps.enc) = %{tl_version}, tex(fir_ekigrt.enc) = %{tl_version}
Provides:       tex(fir_f2p3ju.enc) = %{tl_version}, tex(fir_ggv6fu.enc) = %{tl_version}
Provides:       tex(fir_jbldwq.enc) = %{tl_version}, tex(fir_k64qxk.enc) = %{tl_version}
Provides:       tex(fir_kinqlf.enc) = %{tl_version}, tex(fir_ljq7ir.enc) = %{tl_version}
Provides:       tex(fir_mmg3bv.enc) = %{tl_version}, tex(fir_mpt7xh.enc) = %{tl_version}
Provides:       tex(fir_mxpi7y.enc) = %{tl_version}, tex(fir_ou66re.enc) = %{tl_version}
Provides:       tex(fir_qeo2k2.enc) = %{tl_version}, tex(fir_qudyll.enc) = %{tl_version}
Provides:       tex(fir_sekxdc.enc) = %{tl_version}, tex(fir_tg6zf6.enc) = %{tl_version}
Provides:       tex(fir_ufojbl.enc) = %{tl_version}, tex(fir_wfjhwq.enc) = %{tl_version}
Provides:       tex(fir_wx5a6m.enc) = %{tl_version}, tex(fir_xbqiro.enc) = %{tl_version}
Provides:       tex(fir_xeq6li.enc) = %{tl_version}, tex(fir_xrafnf.enc) = %{tl_version}
Provides:       tex(fir_xsutkk.enc) = %{tl_version}, tex(fir_yhyk3t.enc) = %{tl_version}
Provides:       tex(fir_yow4fl.enc) = %{tl_version}, tex(fir_zei36n.enc) = %{tl_version}
Provides:       tex(fir_zrx7he.enc) = %{tl_version}, tex(fira.map) = %{tl_version}
Provides:       tex(FiraMono-Bold.otf) = %{tl_version}, tex(FiraMono-Medium.otf) = %{tl_version}
Provides:       tex(FiraMono-Regular.otf) = %{tl_version}
Provides:       tex(FiraSans-Bold.otf) = %{tl_version}, tex(FiraSans-BoldItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-Book.otf) = %{tl_version}, tex(FiraSans-BookItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold.otf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight.otf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-Heavy.otf) = %{tl_version}, tex(FiraSans-HeavyItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-Light.otf) = %{tl_version}, tex(FiraSans-LightItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-Medium.otf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-Regular.otf) = %{tl_version}
Provides:       tex(FiraSans-RegularItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold.otf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-Thin.otf) = %{tl_version}, tex(FiraSans-ThinItalic.otf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight.otf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic.otf) = %{tl_version}
Provides:       tex(FiraMono-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(FiraMono-Bold.pfb) = %{tl_version}, tex(FiraMono-Medium.pfb) = %{tl_version}
Provides:       tex(FiraMono-Regular.pfb) = %{tl_version}
Provides:       tex(FiraSans-Bold.pfb) = %{tl_version}, tex(FiraSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-Book.pfb) = %{tl_version}, tex(FiraSans-BookItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold.pfb) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight.pfb) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-Heavy.pfb) = %{tl_version}, tex(FiraSans-HeavyItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-Light.pfb) = %{tl_version}, tex(FiraSans-LightItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-Medium.pfb) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-Regular.pfb) = %{tl_version}
Provides:       tex(FiraSans-RegularItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-SemiBold.pfb) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-Thin.pfb) = %{tl_version}, tex(FiraSans-ThinItalic.pfb) = %{tl_version}
Provides:       tex(FiraSans-UltraLight.pfb) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic.pfb) = %{tl_version}
Provides:       tex(FiraMono-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraMono-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Book-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-BookItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ExtraLightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Heavy-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-HeavyItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-SemiBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-Thin-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-ThinItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(FiraSans-UltraLightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(FiraMono.sty) = %{tl_version}, tex(FiraSans.sty) = %{tl_version}
Provides:       tex(LY1FiraMono-Sup.fd) = %{tl_version}, tex(LY1FiraMono-TLF.fd) = %{tl_version}
Provides:       tex(LY1FiraMono-TOsF.fd) = %{tl_version}
Provides:       tex(LY1FiraSans-LF.fd) = %{tl_version}, tex(LY1FiraSans-OsF.fd) = %{tl_version}
Provides:       tex(LY1FiraSans-Sup.fd) = %{tl_version}, tex(LY1FiraSans-TLF.fd) = %{tl_version}
Provides:       tex(LY1FiraSans-TOsF.fd) = %{tl_version}
Provides:       tex(OT1FiraMono-Sup.fd) = %{tl_version}, tex(OT1FiraMono-TLF.fd) = %{tl_version}
Provides:       tex(OT1FiraMono-TOsF.fd) = %{tl_version}
Provides:       tex(OT1FiraSans-LF.fd) = %{tl_version}, tex(OT1FiraSans-OsF.fd) = %{tl_version}
Provides:       tex(OT1FiraSans-Sup.fd) = %{tl_version}, tex(OT1FiraSans-TLF.fd) = %{tl_version}
Provides:       tex(OT1FiraSans-TOsF.fd) = %{tl_version}
Provides:       tex(T1FiraMono-Sup.fd) = %{tl_version}, tex(T1FiraMono-TLF.fd) = %{tl_version}
Provides:       tex(T1FiraMono-TOsF.fd) = %{tl_version}, tex(T1FiraSans-LF.fd) = %{tl_version}
Provides:       tex(T1FiraSans-OsF.fd) = %{tl_version}, tex(T1FiraSans-Sup.fd) = %{tl_version}
Provides:       tex(T1FiraSans-TLF.fd) = %{tl_version}, tex(T1FiraSans-TOsF.fd) = %{tl_version}
Provides:       tex(TS1FiraMono-TLF.fd) = %{tl_version}, tex(TS1FiraMono-TOsF.fd) = %{tl_version}
Provides:       tex(TS1FiraSans-LF.fd) = %{tl_version}, tex(TS1FiraSans-OsF.fd) = %{tl_version}
Provides:       tex(TS1FiraSans-TLF.fd) = %{tl_version}, tex(TS1FiraSans-TOsF.fd) = %{tl_version}

%description -n texlive-fira
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Fira Sans family of fonts designed by Erik
Spiekermann and Ralph du Carrois of Carrois Type Design. Fira
Sans is available in eleven weights with corresponding italics:
light, regular, medium, bold, ...

%package -n texlive-fira-doc
Summary:        Documentation for fira
Version:        svn47835
Provides:       tex-fira-doc
AutoReqProv:    No

%description -n texlive-fira-doc
Documentation for fira

%package -n texlive-foekfont
Provides:       tex-foekfont = %{tl_version}
License:        GPL+
Summary:        The title font of the Mads Fok magazine
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(foekfont.map) = %{tl_version}, tex(foekfont.tfm) = %{tl_version}
Provides:       tex(FoekFont.pfb) = %{tl_version}, tex(foekfont.sty) = %{tl_version}
Provides:       tex(ot1foekfont.fd) = %{tl_version}, tex(t1foekfont.fd) = %{tl_version}

%description -n texlive-foekfont
The bundle provides an Adobe Type 1 font, and LaTeX support for
its use. The magazine web site shows the font in use in a few
places.

%package -n texlive-foekfont-doc
Summary:        Documentation for foekfont
Version:        svn15878.0

Provides:       tex-foekfont-doc
AutoReqProv:    No

%description -n texlive-foekfont-doc
Documentation for foekfont

%package -n texlive-fonetika
Provides:       tex-fonetika = %{tl_version}
License:        GPL+ and LPPL
Summary:        Support for the Danish "Dania" phonetic system
Version:        svn21326.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty)
Provides:       tex(fonetika.map) = %{tl_version}, tex(fonetika.tfm) = %{tl_version}
Provides:       tex(fonetikabold.tfm) = %{tl_version}, tex(fonetikasans.tfm) = %{tl_version}
Provides:       tex(fonetikasansbold.tfm) = %{tl_version}
Provides:       tex(FonetikaDaniaIwonaeBold.ttf) = %{tl_version}
Provides:       tex(FonetikaDaniaIwonaeRegular.ttf) = %{tl_version}
Provides:       tex(FonetikaDaniaPallaeBold.ttf) = %{tl_version}
Provides:       tex(FonetikaDaniaPallaeRegular.ttf) = %{tl_version}
Provides:       tex(FonetikaDaniaIwonaeBold.pfb) = %{tl_version}
Provides:       tex(FonetikaDaniaIwonaeRegular.pfb) = %{tl_version}
Provides:       tex(FonetikaDaniaPallaeBold.pfb) = %{tl_version}
Provides:       tex(FonetikaDaniaPallaeRegular.pfb) = %{tl_version}
Provides:       tex(fonetika.sty) = %{tl_version}, tex(t1fonetika.fd) = %{tl_version}

%description -n texlive-fonetika
Fonetika Dania is a font bundle with a serif font and a sans
serif font for the danish phonetic system Dania. Both fonts
exist in regular and bold weights. LaTeX support is provided.
The fonts are based on URW Palladio and Iwona Condensed, and
were created using FontForge.

%package -n texlive-fonetika-doc
Summary:        Documentation for fonetika
Version:        svn21326.0

Provides:       tex-fonetika-doc
AutoReqProv:    No

%description -n texlive-fonetika-doc
Documentation for fonetika

%package -n texlive-fontawesome
Provides:       tex-fontawesome = %{tl_version}
License:        LPPL 1.3
Summary:        Font containing web-related icons
Version:        svn48145
Requires:       fontawesome-fonts, texlive-base, texlive-kpathsea-bin, tex-kpathsea, texlive-tetex-bin, tex-tetex
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(fontawesomeone.enc) = %{tl_version}, tex(fontawesomethree.enc) = %{tl_version}
Provides:       tex(fontawesometwo.enc) = %{tl_version}, tex(fontawesome.map) = %{tl_version}
Provides:       tex(FontAwesome.otf) = %{tl_version}, tex(FontAwesome--fontawesomeone.tfm) = %{tl_version}
Provides:       tex(FontAwesome--fontawesomethree.tfm) = %{tl_version}
Provides:       tex(FontAwesome--fontawesometwo.tfm) = %{tl_version}
Provides:       tex(FontAwesome.pfb) = %{tl_version}, tex(fontawesome.sty) = %{tl_version}
Provides:       tex(fontawesomesymbols-generic.tex) = %{tl_version}
Provides:       tex(fontawesomesymbols-pdftex.tex) = %{tl_version}
Provides:       tex(fontawesomesymbols-xeluatex.tex) = %{tl_version}
Provides:       tex(ufontawesomeone.fd) = %{tl_version}, tex(ufontawesomethree.fd) = %{tl_version}
Provides:       tex(ufontawesometwo.fd) = %{tl_version}

%description -n texlive-fontawesome
The package offers access to the large number of web-related
icons provided by the included font. The package requires the
package, fontspec, if run with XeTeX or LuaTeX.

%package -n texlive-fontawesome-doc
Summary:        Documentation for fontawesome
Version:        svn48145
Provides:       tex-fontawesome-doc
AutoReqProv:    No

%description -n texlive-fontawesome-doc
Documentation for fontawesome

%package -n texlive-fontmfizz
Provides:       tex-fontmfizz = %{tl_version}
License:        MIT
Summary:        Font Mfizz icons for use in LaTeX
Version:        svn43546
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(font-mfizz.ttf) = %{tl_version}, tex(fontmfizz.sty) = %{tl_version}

%description -n texlive-fontmfizz
The MFizz font provides scalable vector icons representing
programming languages, operating systems, software engineering,
and technology. It can be seen as an extension to FontAwesome.
This package requires the fontspec package and either the
Xe(La)TeX or Lua(La)TeX engine to load the included ttf font.

%package -n texlive-fontmfizz-doc
Summary:        Documentation for fontmfizz
Version:        svn43546
Provides:       tex-fontmfizz-doc
AutoReqProv:    No

%description -n texlive-fontmfizz-doc
Documentation for fontmfizz

%package -n texlive-fourier
Provides:       tex-fourier = %{tl_version}
License:        LPPL
Summary:        Using Utopia fonts in LaTeX documents
Version:        svn15878.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty), tex(textcomp.sty)
Provides:       tex(fourier-utopia-expert.map) = %{tl_version}
Provides:       tex(fourier.map) = %{tl_version}, tex(fourier-alt-black.tfm) = %{tl_version}
Provides:       tex(fourier-alt-bold-sl.tfm) = %{tl_version}
Provides:       tex(fourier-alt-bold.tfm) = %{tl_version}
Provides:       tex(fourier-alt-boldita.tfm) = %{tl_version}
Provides:       tex(fourier-alt-ita.tfm) = %{tl_version}
Provides:       tex(fourier-alt-semi-sl.tfm) = %{tl_version}
Provides:       tex(fourier-alt-semi.tfm) = %{tl_version}
Provides:       tex(fourier-alt-semiita.tfm) = %{tl_version}
Provides:       tex(fourier-alt-sl.tfm) = %{tl_version}, tex(fourier-alt.tfm) = %{tl_version}
Provides:       tex(fourier-bb.tfm) = %{tl_version}, tex(fourier-mcl.tfm) = %{tl_version}
Provides:       tex(fourier-mex.tfm) = %{tl_version}, tex(fourier-ml.tfm) = %{tl_version}
Provides:       tex(fourier-mlb.tfm) = %{tl_version}, tex(fourier-mlit.tfm) = %{tl_version}
Provides:       tex(fourier-mlitb.tfm) = %{tl_version}, tex(fourier-ms.tfm) = %{tl_version}
Provides:       tex(fourier-orns.tfm) = %{tl_version}, tex(futb8c.tfm) = %{tl_version}
Provides:       tex(futb8r.tfm) = %{tl_version}, tex(futb8t.tfm) = %{tl_version}
Provides:       tex(futb8x.tfm) = %{tl_version}, tex(futb9c.tfm) = %{tl_version}
Provides:       tex(futb9d.tfm) = %{tl_version}, tex(futb9e.tfm) = %{tl_version}
Provides:       tex(futbc8t.tfm) = %{tl_version}, tex(futbi8c.tfm) = %{tl_version}
Provides:       tex(futbi8r.tfm) = %{tl_version}, tex(futbi8t.tfm) = %{tl_version}
Provides:       tex(futbi8x.tfm) = %{tl_version}, tex(futbi9c.tfm) = %{tl_version}
Provides:       tex(futbi9d.tfm) = %{tl_version}, tex(futbi9e.tfm) = %{tl_version}
Provides:       tex(futbo8c.tfm) = %{tl_version}, tex(futbo8r.tfm) = %{tl_version}
Provides:       tex(futbo8t.tfm) = %{tl_version}, tex(futbo8x.tfm) = %{tl_version}
Provides:       tex(futbo9c.tfm) = %{tl_version}, tex(futbo9d.tfm) = %{tl_version}
Provides:       tex(futbo9e.tfm) = %{tl_version}, tex(futboorn.tfm) = %{tl_version}
Provides:       tex(futborn.tfm) = %{tl_version}, tex(futc8r.tfm) = %{tl_version}
Provides:       tex(futc8x.tfm) = %{tl_version}, tex(futc9c.tfm) = %{tl_version}
Provides:       tex(futc9d.tfm) = %{tl_version}, tex(futc9e.tfm) = %{tl_version}
Provides:       tex(futcorn.tfm) = %{tl_version}, tex(futmi.tfm) = %{tl_version}
Provides:       tex(futmib.tfm) = %{tl_version}, tex(futmii.tfm) = %{tl_version}
Provides:       tex(futmiib.tfm) = %{tl_version}, tex(futr8c.tfm) = %{tl_version}
Provides:       tex(futr8r.tfm) = %{tl_version}, tex(futr8t.tfm) = %{tl_version}
Provides:       tex(futr8x.tfm) = %{tl_version}, tex(futr9c.tfm) = %{tl_version}
Provides:       tex(futr9d.tfm) = %{tl_version}, tex(futr9e.tfm) = %{tl_version}
Provides:       tex(futrc8r.tfm) = %{tl_version}, tex(futrc8t.tfm) = %{tl_version}
Provides:       tex(futrc9d.tfm) = %{tl_version}, tex(futrc9e.tfm) = %{tl_version}
Provides:       tex(futrd8r.tfm) = %{tl_version}, tex(futrd8t.tfm) = %{tl_version}
Provides:       tex(futri8c.tfm) = %{tl_version}, tex(futri8r.tfm) = %{tl_version}
Provides:       tex(futri8t.tfm) = %{tl_version}, tex(futri8x.tfm) = %{tl_version}
Provides:       tex(futri9c.tfm) = %{tl_version}, tex(futri9d.tfm) = %{tl_version}
Provides:       tex(futri9e.tfm) = %{tl_version}, tex(futro8c.tfm) = %{tl_version}
Provides:       tex(futro8r.tfm) = %{tl_version}, tex(futro8t.tfm) = %{tl_version}
Provides:       tex(futro8x.tfm) = %{tl_version}, tex(futro9c.tfm) = %{tl_version}
Provides:       tex(futro9d.tfm) = %{tl_version}, tex(futro9e.tfm) = %{tl_version}
Provides:       tex(futroorn.tfm) = %{tl_version}, tex(futrorn.tfm) = %{tl_version}
Provides:       tex(futs8r.tfm) = %{tl_version}, tex(futs8x.tfm) = %{tl_version}
Provides:       tex(futs9c.tfm) = %{tl_version}, tex(futs9d.tfm) = %{tl_version}
Provides:       tex(futs9e.tfm) = %{tl_version}, tex(futsc8r.tfm) = %{tl_version}
Provides:       tex(futsc9d.tfm) = %{tl_version}, tex(futsc9e.tfm) = %{tl_version}
Provides:       tex(futsi8r.tfm) = %{tl_version}, tex(futsi8x.tfm) = %{tl_version}
Provides:       tex(futsi9c.tfm) = %{tl_version}, tex(futsi9d.tfm) = %{tl_version}
Provides:       tex(futsi9e.tfm) = %{tl_version}, tex(futso8r.tfm) = %{tl_version}
Provides:       tex(futso8x.tfm) = %{tl_version}, tex(futso9c.tfm) = %{tl_version}
Provides:       tex(futso9d.tfm) = %{tl_version}, tex(futso9e.tfm) = %{tl_version}
Provides:       tex(futsoorn.tfm) = %{tl_version}, tex(futsorn.tfm) = %{tl_version}
Provides:       tex(futsy.tfm) = %{tl_version}, tex(fourier-alt-black.pfb) = %{tl_version}
Provides:       tex(fourier-alt-bold.pfb) = %{tl_version}
Provides:       tex(fourier-alt-boldita.pfb) = %{tl_version}
Provides:       tex(fourier-alt-ita.pfb) = %{tl_version}
Provides:       tex(fourier-alt-semi.pfb) = %{tl_version}
Provides:       tex(fourier-alt-semiita.pfb) = %{tl_version}
Provides:       tex(fourier-alt.pfb) = %{tl_version}, tex(fourier-bb.pfb) = %{tl_version}
Provides:       tex(fourier-mcl.pfb) = %{tl_version}, tex(fourier-mex.pfb) = %{tl_version}
Provides:       tex(fourier-ml.pfb) = %{tl_version}, tex(fourier-mlb.pfb) = %{tl_version}
Provides:       tex(fourier-mlit.pfb) = %{tl_version}, tex(fourier-mlitb.pfb) = %{tl_version}
Provides:       tex(fourier-ms.pfb) = %{tl_version}, tex(fourier-orns.pfb) = %{tl_version}
Provides:       tex(futb8c.vf) = %{tl_version}, tex(futb8t.vf) = %{tl_version}
Provides:       tex(futb9c.vf) = %{tl_version}, tex(futb9d.vf) = %{tl_version}
Provides:       tex(futb9e.vf) = %{tl_version}, tex(futbc8t.vf) = %{tl_version}
Provides:       tex(futbi8c.vf) = %{tl_version}, tex(futbi8t.vf) = %{tl_version}
Provides:       tex(futbi9c.vf) = %{tl_version}, tex(futbi9d.vf) = %{tl_version}
Provides:       tex(futbi9e.vf) = %{tl_version}, tex(futbo8c.vf) = %{tl_version}
Provides:       tex(futbo8t.vf) = %{tl_version}, tex(futbo9c.vf) = %{tl_version}
Provides:       tex(futbo9d.vf) = %{tl_version}, tex(futbo9e.vf) = %{tl_version}
Provides:       tex(futboorn.vf) = %{tl_version}, tex(futborn.vf) = %{tl_version}
Provides:       tex(futc9c.vf) = %{tl_version}, tex(futc9d.vf) = %{tl_version}
Provides:       tex(futc9e.vf) = %{tl_version}, tex(futcorn.vf) = %{tl_version}
Provides:       tex(futmi.vf) = %{tl_version}, tex(futmib.vf) = %{tl_version}
Provides:       tex(futmii.vf) = %{tl_version}, tex(futmiib.vf) = %{tl_version}
Provides:       tex(futr8c.vf) = %{tl_version}, tex(futr8t.vf) = %{tl_version}
Provides:       tex(futr9c.vf) = %{tl_version}, tex(futr9d.vf) = %{tl_version}
Provides:       tex(futr9e.vf) = %{tl_version}, tex(futrc8t.vf) = %{tl_version}
Provides:       tex(futrc9d.vf) = %{tl_version}, tex(futrc9e.vf) = %{tl_version}
Provides:       tex(futrd8t.vf) = %{tl_version}, tex(futri8c.vf) = %{tl_version}
Provides:       tex(futri8t.vf) = %{tl_version}, tex(futri9c.vf) = %{tl_version}
Provides:       tex(futri9d.vf) = %{tl_version}, tex(futri9e.vf) = %{tl_version}
Provides:       tex(futro8c.vf) = %{tl_version}, tex(futro8t.vf) = %{tl_version}
Provides:       tex(futro9c.vf) = %{tl_version}, tex(futro9d.vf) = %{tl_version}
Provides:       tex(futro9e.vf) = %{tl_version}, tex(futroorn.vf) = %{tl_version}
Provides:       tex(futrorn.vf) = %{tl_version}, tex(futs9c.vf) = %{tl_version}
Provides:       tex(futs9d.vf) = %{tl_version}, tex(futs9e.vf) = %{tl_version}
Provides:       tex(futsc9d.vf) = %{tl_version}, tex(futsc9e.vf) = %{tl_version}
Provides:       tex(futsi9c.vf) = %{tl_version}, tex(futsi9d.vf) = %{tl_version}
Provides:       tex(futsi9e.vf) = %{tl_version}, tex(futso9c.vf) = %{tl_version}
Provides:       tex(futso9d.vf) = %{tl_version}, tex(futso9e.vf) = %{tl_version}
Provides:       tex(futsoorn.vf) = %{tl_version}, tex(futsorn.vf) = %{tl_version}
Provides:       tex(futsy.vf) = %{tl_version}, tex(fmlfutm.fd) = %{tl_version}
Provides:       tex(fmlfutmi.fd) = %{tl_version}, tex(fmsfutm.fd) = %{tl_version}
Provides:       tex(fmxfutm.fd) = %{tl_version}, tex(fourier-orns.sty) = %{tl_version}
Provides:       tex(fourier.sty) = %{tl_version}, tex(t1futj.fd) = %{tl_version}
Provides:       tex(t1futs.fd) = %{tl_version}, tex(t1futx.fd) = %{tl_version}
Provides:       tex(ts1futj.fd) = %{tl_version}, tex(ts1futs.fd) = %{tl_version}
Provides:       tex(ts1futx.fd) = %{tl_version}, tex(ufuts.fd) = %{tl_version}

%description -n texlive-fourier
Fourier-GUTenberg is a LaTeX typesetting system which uses
Adobe Utopia as its standard base font. Fourier-GUTenberg
provides all complementary typefaces needed to allow Utopia
based TeX typesetting, including an extensive mathematics set
and several other symbols. The system is absolutely stand-
alone: apart from Utopia and Fourier, no other typefaces are
required. The fourier fonts will also work with Adobe Utopia
Expert fonts, which are only available for purchase. Utopia is
a registered trademark of Adobe Systems Incorporated

%package -n texlive-fourier-doc
Summary:        Documentation for fourier
Version:        svn15878.1.3

Provides:       tex-fourier-doc
AutoReqProv:    No

%description -n texlive-fourier-doc
Documentation for fourier

%package -n texlive-fouriernc
Provides:       tex-fouriernc = %{tl_version}
License:        LPPL
Summary:        Use New Century Schoolbook text with Fourier maths fonts
Version:        svn29646.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fourier.sty)
Provides:       tex(fncmi.tfm) = %{tl_version}, tex(fncmib.tfm) = %{tl_version}
Provides:       tex(fncmii.tfm) = %{tl_version}, tex(fncmiib.tfm) = %{tl_version}
Provides:       tex(fncsy.tfm) = %{tl_version}, tex(fncmi.vf) = %{tl_version}
Provides:       tex(fncmib.vf) = %{tl_version}, tex(fncmii.vf) = %{tl_version}
Provides:       tex(fncmiib.vf) = %{tl_version}, tex(fncsy.vf) = %{tl_version}
Provides:       tex(fmlfncm.fd) = %{tl_version}, tex(fmlfncmi.fd) = %{tl_version}
Provides:       tex(fmsfncm.fd) = %{tl_version}, tex(fouriernc.sty) = %{tl_version}
Provides:       tex(t1fnc.fd) = %{tl_version}, tex(ts1fnc.fd) = %{tl_version}

%description -n texlive-fouriernc
This package provides a LaTeX mathematics font setup for use
with New Century Schoolbook text. In order to use it you need
to have the Fourier-GUTenberg fonts installed.

%package -n texlive-fouriernc-doc
Summary:        Documentation for fouriernc
Version:        svn29646.0

Provides:       tex-fouriernc-doc
AutoReqProv:    No

%description -n texlive-fouriernc-doc
Documentation for fouriernc

%package -n texlive-frcursive
Provides:       tex-frcursive = %{tl_version}
License:        LPPL 1.2
Summary:        French cursive hand fonts
Version:        svn24559.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty)
Provides:       tex(frcursive.map) = %{tl_version}, tex(frca10.tfm) = %{tl_version}
Provides:       tex(frcbx10.tfm) = %{tl_version}, tex(frcbx14.tfm) = %{tl_version}
Provides:       tex(frcbx6.tfm) = %{tl_version}, tex(frcc10.tfm) = %{tl_version}
Provides:       tex(frcc14.tfm) = %{tl_version}, tex(frcc6.tfm) = %{tl_version}
Provides:       tex(frcf10.tfm) = %{tl_version}, tex(frcf14.tfm) = %{tl_version}
Provides:       tex(frcf6.tfm) = %{tl_version}, tex(frcr10.tfm) = %{tl_version}
Provides:       tex(frcr14.tfm) = %{tl_version}, tex(frcr6.tfm) = %{tl_version}
Provides:       tex(frcsl10.tfm) = %{tl_version}, tex(frcsl14.tfm) = %{tl_version}
Provides:       tex(frcsl6.tfm) = %{tl_version}, tex(frcslbx10.tfm) = %{tl_version}
Provides:       tex(frcslbx14.tfm) = %{tl_version}, tex(frcslbx6.tfm) = %{tl_version}
Provides:       tex(frcslc10.tfm) = %{tl_version}, tex(frcslc14.tfm) = %{tl_version}
Provides:       tex(frcslc6.tfm) = %{tl_version}, tex(frcw10.tfm) = %{tl_version}
Provides:       tex(frca10.pfb) = %{tl_version}, tex(frcbx10.pfb) = %{tl_version}
Provides:       tex(frcbx14.pfb) = %{tl_version}, tex(frcbx6.pfb) = %{tl_version}
Provides:       tex(frcc10.pfb) = %{tl_version}, tex(frcc14.pfb) = %{tl_version}
Provides:       tex(frcc6.pfb) = %{tl_version}, tex(frcf10.pfb) = %{tl_version}
Provides:       tex(frcf14.pfb) = %{tl_version}, tex(frcf6.pfb) = %{tl_version}
Provides:       tex(frcr10.pfb) = %{tl_version}, tex(frcr14.pfb) = %{tl_version}
Provides:       tex(frcr6.pfb) = %{tl_version}, tex(frcsl10.pfb) = %{tl_version}
Provides:       tex(frcsl14.pfb) = %{tl_version}, tex(frcsl6.pfb) = %{tl_version}
Provides:       tex(frcslbx10.pfb) = %{tl_version}, tex(frcslbx14.pfb) = %{tl_version}
Provides:       tex(frcslbx6.pfb) = %{tl_version}, tex(frcslc10.pfb) = %{tl_version}
Provides:       tex(frcslc14.pfb) = %{tl_version}, tex(frcslc6.pfb) = %{tl_version}
Provides:       tex(frcw10.pfb) = %{tl_version}, tex(frcursive.sty) = %{tl_version}
Provides:       tex(ot1frc.fd) = %{tl_version}, tex(t1frc.fd) = %{tl_version}

%description -n texlive-frcursive
A hand-writing font in the style of the French academic running-
hand. The font was written in Metafont and and has been
converted to Adobe Type 1 format. LaTeX support (NFFS fd files,
and a package) and font maps are provided.

%package -n texlive-frcursive-doc
Summary:        Documentation for frcursive
Version:        svn24559.0

Provides:       tex-frcursive-doc
AutoReqProv:    No

%description -n texlive-frcursive-doc
Documentation for frcursive

%package -n texlive-fpl
Provides:       tex-fpl = %{tl_version}
License:        GPL+
Summary:        SC and OsF fonts for URW Palladio L
Version:        svn15878.1.002

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fplbij8a.pfb) = %{tl_version}, tex(fplbj8a.pfb) = %{tl_version}
Provides:       tex(fplrc8a.pfb) = %{tl_version}, tex(fplrij8a.pfb) = %{tl_version}

%description -n texlive-fpl
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L
which are compatible with respect to metrics with the Palatino
SC/OsF fonts from Adobe. Note that it is not my aim to exactly
reproduce the outlines of the original Adobe fonts. The SC and
OsF in the FPL Fonts were designed with the glyphs from URW
Palladio L as starting point. For some glyphs (e.g. 'o') I got
the best result by scaling and boldening. For others (e.g. 'h')
shifting selected portions of the character gave more
satisfying results. All this was done using the free font
editor FontForge. The kerning data in these fonts comes from
Walter Schmidt's improved Palatino metrics. LaTeX use is
enabled by the mathpazo package, which is part of the psnfss
distribution.

%package -n texlive-fpl-doc
Summary:        Documentation for fpl
Version:        svn15878.1.002

Provides:       tex-fpl-doc
AutoReqProv:    No

%description -n texlive-fpl-doc
Documentation for fpl

%package -n texlive-fenixpar
Provides:       tex-fenixpar = %{tl_version}
License:        LPPL
Summary:        One-shot changes to token registers such as \everypar
Version:        svn24730.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fenixpar.sty) = %{tl_version}, tex(fenixtok.sty) = %{tl_version}

%description -n texlive-fenixpar
The bundle provides two packages, fenxitok and fenixpar. The
fenixtok package provides user macros to add material to a
token register; the material will be (automatically) removed
from the token register when the register is executed. Material
may be added either to the left or to the right, and care is
taken not to override any redefinition that may be included in
the token register itself. The fenixpar package uses the macros
of fenixtok to provide a user interface to manipulation of the
\everypar token register. The packages require the e-TeX
extensions; with them, they work either with Plain TeX or with
LaTeX.

%package -n texlive-fenixpar-doc
Summary:        Documentation for fenixpar
Version:        svn24730.0.92

Provides:       tex-fenixpar-doc
AutoReqProv:    No

%description -n texlive-fenixpar-doc
Documentation for fenixpar

%package -n texlive-fltpoint
Provides:       tex-fltpoint = %{tl_version}
License:        LPPL
Summary:        Simple floating point arithmetic
Version:        svn15878.1.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(deccomma.sty) = %{tl_version}, tex(fltpoint.sty) = %{tl_version}
Provides:       tex(fltpoint.tex) = %{tl_version}

%description -n texlive-fltpoint
The package provides simple floating point operations
(addition, subtraction, multiplication, division and rounding).
Used, for example, by rccol.

%package -n texlive-fltpoint-doc
Summary:        Documentation for fltpoint
Version:        svn15878.1.1b

Provides:       tex-fltpoint-doc
AutoReqProv:    No

%description -n texlive-fltpoint-doc
Documentation for fltpoint

%package -n texlive-fntproof
Provides:       tex-fntproof = %{tl_version}
License:        Public Domain
Summary:        A programmable font test pattern generator
Version:        svn20638.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fntproof.tex) = %{tl_version}

%description -n texlive-fntproof
The package implements all the font testing commands of Knuth's
testfont.tex, but arranges that information necessary for each
command is supplied as arguments to that command, rather than
prompted for. This makes it possible to type all the tests in
one command line, and easy to input the package in a file and
to use the commands there. A few additional commands supporting
this last purpose are also made available.

%package -n texlive-fntproof-doc
Summary:        Documentation for fntproof
Version:        svn20638.0

Provides:       tex-fntproof-doc
AutoReqProv:    No

%description -n texlive-fntproof-doc
Documentation for fntproof

%package -n texlive-fontname
Provides:       tex-fontname = %{tl_version}
License:        GPL+
Summary:        Scheme for naming fonts in TeX
Version:        svn45930
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(adobe.map) = %{tl_version}, tex(apple.map) = %{tl_version}
Provides:       tex(bitstrea.map) = %{tl_version}, tex(dtc.map) = %{tl_version}
Provides:       tex(itc.map) = %{tl_version}, tex(linot-cd.map) = %{tl_version}
Provides:       tex(linotype-cd.map) = %{tl_version}, tex(linotype.map) = %{tl_version}
Provides:       tex(monotype.map) = %{tl_version}, tex(skey1250.map) = %{tl_version}
Provides:       tex(skey1555.map) = %{tl_version}, tex(softkey-1250.map) = %{tl_version}
Provides:       tex(softkey-1555.map) = %{tl_version}, tex(softkey.map) = %{tl_version}
Provides:       tex(special.map) = %{tl_version}, tex(supplier.map) = %{tl_version}
Provides:       tex(texfonts.map) = %{tl_version}, tex(typeface.map) = %{tl_version}
Provides:       tex(urw.map) = %{tl_version}, tex(variant.map) = %{tl_version}
Provides:       tex(weight.map) = %{tl_version}, tex(width.map) = %{tl_version}
Provides:       tex(yandy.map) = %{tl_version}

%description -n texlive-fontname
The scheme for assigning names is described (in the
documentation part of the package), and map files giving the
relation between foundry name and 'TeX-name' are also provided.

%package -n texlive-fontname-doc
Summary:        Documentation for fontname
Version:        svn45930
Provides:       tex-fontname-doc
AutoReqProv:    No

%description -n texlive-fontname-doc
Documentation for fontname

%package -n texlive-fc
Provides:       tex-fc = %{tl_version}
License:        GPLv2+
Summary:        Fonts for African languages
Version:        svn32796.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(newlfont.sty), tex(fontenc.sty)
Provides:       tex(fcbx10.tfm) = %{tl_version}, tex(fcbx11.tfm) = %{tl_version}
Provides:       tex(fcbx12.tfm) = %{tl_version}, tex(fcbx14.tfm) = %{tl_version}
Provides:       tex(fcbx17.tfm) = %{tl_version}, tex(fcbx20.tfm) = %{tl_version}
Provides:       tex(fcbx25.tfm) = %{tl_version}, tex(fcbx5.tfm) = %{tl_version}
Provides:       tex(fcbx6.tfm) = %{tl_version}, tex(fcbx7.tfm) = %{tl_version}
Provides:       tex(fcbx8.tfm) = %{tl_version}, tex(fcbx9.tfm) = %{tl_version}
Provides:       tex(fcbxi10.tfm) = %{tl_version}, tex(fcbxi11.tfm) = %{tl_version}
Provides:       tex(fcbxi12.tfm) = %{tl_version}, tex(fcbxi14.tfm) = %{tl_version}
Provides:       tex(fcbxi17.tfm) = %{tl_version}, tex(fcbxi20.tfm) = %{tl_version}
Provides:       tex(fcbxi25.tfm) = %{tl_version}, tex(fcbxi5.tfm) = %{tl_version}
Provides:       tex(fcbxi6.tfm) = %{tl_version}, tex(fcbxi7.tfm) = %{tl_version}
Provides:       tex(fcbxi8.tfm) = %{tl_version}, tex(fcbxi9.tfm) = %{tl_version}
Provides:       tex(fcbxsl10.tfm) = %{tl_version}, tex(fcbxsl11.tfm) = %{tl_version}
Provides:       tex(fcbxsl12.tfm) = %{tl_version}, tex(fcbxsl14.tfm) = %{tl_version}
Provides:       tex(fcbxsl17.tfm) = %{tl_version}, tex(fcbxsl20.tfm) = %{tl_version}
Provides:       tex(fcbxsl25.tfm) = %{tl_version}, tex(fcbxsl5.tfm) = %{tl_version}
Provides:       tex(fcbxsl6.tfm) = %{tl_version}, tex(fcbxsl7.tfm) = %{tl_version}
Provides:       tex(fcbxsl8.tfm) = %{tl_version}, tex(fcbxsl9.tfm) = %{tl_version}
Provides:       tex(fcbxu10.tfm) = %{tl_version}, tex(fcbxu11.tfm) = %{tl_version}
Provides:       tex(fcbxu12.tfm) = %{tl_version}, tex(fcbxu14.tfm) = %{tl_version}
Provides:       tex(fcbxu17.tfm) = %{tl_version}, tex(fcbxu20.tfm) = %{tl_version}
Provides:       tex(fcbxu25.tfm) = %{tl_version}, tex(fcbxu5.tfm) = %{tl_version}
Provides:       tex(fcbxu6.tfm) = %{tl_version}, tex(fcbxu7.tfm) = %{tl_version}
Provides:       tex(fcbxu8.tfm) = %{tl_version}, tex(fcbxu9.tfm) = %{tl_version}
Provides:       tex(fccsc10.tfm) = %{tl_version}, tex(fccsc11.tfm) = %{tl_version}
Provides:       tex(fccsc12.tfm) = %{tl_version}, tex(fccsc14.tfm) = %{tl_version}
Provides:       tex(fccsc17.tfm) = %{tl_version}, tex(fccsc20.tfm) = %{tl_version}
Provides:       tex(fccsc25.tfm) = %{tl_version}, tex(fccsc5.tfm) = %{tl_version}
Provides:       tex(fccsc6.tfm) = %{tl_version}, tex(fccsc7.tfm) = %{tl_version}
Provides:       tex(fccsc8.tfm) = %{tl_version}, tex(fccsc9.tfm) = %{tl_version}
Provides:       tex(fci10.tfm) = %{tl_version}, tex(fci11.tfm) = %{tl_version}
Provides:       tex(fci12.tfm) = %{tl_version}, tex(fci14.tfm) = %{tl_version}
Provides:       tex(fci17.tfm) = %{tl_version}, tex(fci20.tfm) = %{tl_version}
Provides:       tex(fci25.tfm) = %{tl_version}, tex(fci5.tfm) = %{tl_version}
Provides:       tex(fci6.tfm) = %{tl_version}, tex(fci7.tfm) = %{tl_version}
Provides:       tex(fci8.tfm) = %{tl_version}, tex(fci9.tfm) = %{tl_version}
Provides:       tex(fcitt10.tfm) = %{tl_version}, tex(fcitt11.tfm) = %{tl_version}
Provides:       tex(fcitt12.tfm) = %{tl_version}, tex(fcitt14.tfm) = %{tl_version}
Provides:       tex(fcitt17.tfm) = %{tl_version}, tex(fcitt20.tfm) = %{tl_version}
Provides:       tex(fcitt25.tfm) = %{tl_version}, tex(fcitt5.tfm) = %{tl_version}
Provides:       tex(fcitt6.tfm) = %{tl_version}, tex(fcitt7.tfm) = %{tl_version}
Provides:       tex(fcitt8.tfm) = %{tl_version}, tex(fcitt9.tfm) = %{tl_version}
Provides:       tex(fcr10.tfm) = %{tl_version}, tex(fcr11.tfm) = %{tl_version}
Provides:       tex(fcr12.tfm) = %{tl_version}, tex(fcr14.tfm) = %{tl_version}
Provides:       tex(fcr17.tfm) = %{tl_version}, tex(fcr20.tfm) = %{tl_version}
Provides:       tex(fcr25.tfm) = %{tl_version}, tex(fcr5.tfm) = %{tl_version}
Provides:       tex(fcr6.tfm) = %{tl_version}, tex(fcr7.tfm) = %{tl_version}
Provides:       tex(fcr8.tfm) = %{tl_version}, tex(fcr9.tfm) = %{tl_version}
Provides:       tex(fcsibx10.tfm) = %{tl_version}, tex(fcsibx11.tfm) = %{tl_version}
Provides:       tex(fcsibx12.tfm) = %{tl_version}, tex(fcsibx14.tfm) = %{tl_version}
Provides:       tex(fcsibx17.tfm) = %{tl_version}, tex(fcsibx20.tfm) = %{tl_version}
Provides:       tex(fcsibx25.tfm) = %{tl_version}, tex(fcsibx5.tfm) = %{tl_version}
Provides:       tex(fcsibx6.tfm) = %{tl_version}, tex(fcsibx7.tfm) = %{tl_version}
Provides:       tex(fcsibx8.tfm) = %{tl_version}, tex(fcsibx9.tfm) = %{tl_version}
Provides:       tex(fcsitt10.tfm) = %{tl_version}, tex(fcsitt11.tfm) = %{tl_version}
Provides:       tex(fcsitt12.tfm) = %{tl_version}, tex(fcsitt14.tfm) = %{tl_version}
Provides:       tex(fcsitt17.tfm) = %{tl_version}, tex(fcsitt20.tfm) = %{tl_version}
Provides:       tex(fcsitt25.tfm) = %{tl_version}, tex(fcsitt5.tfm) = %{tl_version}
Provides:       tex(fcsitt6.tfm) = %{tl_version}, tex(fcsitt7.tfm) = %{tl_version}
Provides:       tex(fcsitt8.tfm) = %{tl_version}, tex(fcsitt9.tfm) = %{tl_version}
Provides:       tex(fcsl10.tfm) = %{tl_version}, tex(fcsl11.tfm) = %{tl_version}
Provides:       tex(fcsl12.tfm) = %{tl_version}, tex(fcsl14.tfm) = %{tl_version}
Provides:       tex(fcsl17.tfm) = %{tl_version}, tex(fcsl20.tfm) = %{tl_version}
Provides:       tex(fcsl25.tfm) = %{tl_version}, tex(fcsl5.tfm) = %{tl_version}
Provides:       tex(fcsl6.tfm) = %{tl_version}, tex(fcsl7.tfm) = %{tl_version}
Provides:       tex(fcsl8.tfm) = %{tl_version}, tex(fcsl9.tfm) = %{tl_version}
Provides:       tex(fcss10.tfm) = %{tl_version}, tex(fcss11.tfm) = %{tl_version}
Provides:       tex(fcss12.tfm) = %{tl_version}, tex(fcss14.tfm) = %{tl_version}
Provides:       tex(fcss17.tfm) = %{tl_version}, tex(fcss20.tfm) = %{tl_version}
Provides:       tex(fcss25.tfm) = %{tl_version}, tex(fcss5.tfm) = %{tl_version}
Provides:       tex(fcss6.tfm) = %{tl_version}, tex(fcss7.tfm) = %{tl_version}
Provides:       tex(fcss8.tfm) = %{tl_version}, tex(fcss9.tfm) = %{tl_version}
Provides:       tex(fcssbx10.tfm) = %{tl_version}, tex(fcssbx11.tfm) = %{tl_version}
Provides:       tex(fcssbx12.tfm) = %{tl_version}, tex(fcssbx14.tfm) = %{tl_version}
Provides:       tex(fcssbx17.tfm) = %{tl_version}, tex(fcssbx20.tfm) = %{tl_version}
Provides:       tex(fcssbx25.tfm) = %{tl_version}, tex(fcssbx5.tfm) = %{tl_version}
Provides:       tex(fcssbx6.tfm) = %{tl_version}, tex(fcssbx7.tfm) = %{tl_version}
Provides:       tex(fcssbx8.tfm) = %{tl_version}, tex(fcssbx9.tfm) = %{tl_version}
Provides:       tex(fcssi10.tfm) = %{tl_version}, tex(fcssi11.tfm) = %{tl_version}
Provides:       tex(fcssi12.tfm) = %{tl_version}, tex(fcssi14.tfm) = %{tl_version}
Provides:       tex(fcssi17.tfm) = %{tl_version}, tex(fcssi20.tfm) = %{tl_version}
Provides:       tex(fcssi25.tfm) = %{tl_version}, tex(fcssi5.tfm) = %{tl_version}
Provides:       tex(fcssi6.tfm) = %{tl_version}, tex(fcssi7.tfm) = %{tl_version}
Provides:       tex(fcssi8.tfm) = %{tl_version}, tex(fcssi9.tfm) = %{tl_version}
Provides:       tex(fcsstt10.tfm) = %{tl_version}, tex(fcsstt11.tfm) = %{tl_version}
Provides:       tex(fcsstt12.tfm) = %{tl_version}, tex(fcsstt14.tfm) = %{tl_version}
Provides:       tex(fcsstt17.tfm) = %{tl_version}, tex(fcsstt20.tfm) = %{tl_version}
Provides:       tex(fcsstt25.tfm) = %{tl_version}, tex(fcsstt5.tfm) = %{tl_version}
Provides:       tex(fcsstt6.tfm) = %{tl_version}, tex(fcsstt7.tfm) = %{tl_version}
Provides:       tex(fcsstt8.tfm) = %{tl_version}, tex(fcsstt9.tfm) = %{tl_version}
Provides:       tex(fctt10.tfm) = %{tl_version}, tex(fctt11.tfm) = %{tl_version}
Provides:       tex(fctt12.tfm) = %{tl_version}, tex(fctt14.tfm) = %{tl_version}
Provides:       tex(fctt17.tfm) = %{tl_version}, tex(fctt20.tfm) = %{tl_version}
Provides:       tex(fctt25.tfm) = %{tl_version}, tex(fctt5.tfm) = %{tl_version}
Provides:       tex(fctt6.tfm) = %{tl_version}, tex(fctt7.tfm) = %{tl_version}
Provides:       tex(fctt8.tfm) = %{tl_version}, tex(fctt9.tfm) = %{tl_version}
Provides:       tex(fcu10.tfm) = %{tl_version}, tex(fcu11.tfm) = %{tl_version}
Provides:       tex(fcu12.tfm) = %{tl_version}, tex(fcu14.tfm) = %{tl_version}
Provides:       tex(fcu17.tfm) = %{tl_version}, tex(fcu20.tfm) = %{tl_version}
Provides:       tex(fcu25.tfm) = %{tl_version}, tex(fcu5.tfm) = %{tl_version}
Provides:       tex(fcu6.tfm) = %{tl_version}, tex(fcu7.tfm) = %{tl_version}
Provides:       tex(fcu8.tfm) = %{tl_version}, tex(fcu9.tfm) = %{tl_version}
Provides:       tex(fclfont.sty) = %{tl_version}, tex(fcuse.sty) = %{tl_version}
Provides:       tex(t4cmr.fd) = %{tl_version}, tex(t4cmss.fd) = %{tl_version}
Provides:       tex(t4cmtt.fd) = %{tl_version}, tex(t4enc.def) = %{tl_version}
Provides:       tex(t4fcr.fd) = %{tl_version}, tex(t4phonet.sty) = %{tl_version}

%description -n texlive-fc
The fonts are provided as Metafont source, in the familiar
arrangement of lots of (autogenerated) preamble files and a
modest set of glyph specifications. (A similar arrangement
appears in the ec and lh font bundles.)

%package -n texlive-fc-doc
Summary:        Documentation for fc
Version:        svn32796.1.4

Provides:       tex-fc-doc
AutoReqProv:    No

%description -n texlive-fc-doc
Documentation for fc

%package -n texlive-fandol
Provides:       tex-fandol = %{tl_version}
License:        GPL+
Summary:        Four basic fonts for Chinese typesetting
Version:        svn37889.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(FandolBraille-Display.otf) = %{tl_version}
Provides:       tex(FandolBraille-Regular.otf) = %{tl_version}
Provides:       tex(FandolFang-Regular.otf) = %{tl_version}
Provides:       tex(FandolHei-Bold.otf) = %{tl_version}, tex(FandolHei-Regular.otf) = %{tl_version}
Provides:       tex(FandolKai-Regular.otf) = %{tl_version}
Provides:       tex(FandolSong-Bold.otf) = %{tl_version}
Provides:       tex(FandolSong-Regular.otf) = %{tl_version}

%description -n texlive-fandol
Fandol fonts designed for Chinese typesetting. The current
version contains four styles: Song, Hei, Kai, Fang. All fonts
are in OpenType format.

%package -n texlive-fandol-doc
Summary:        Documentation for fandol
Version:        svn37889.0.3

Provides:       tex-fandol-doc
AutoReqProv:    No

%description -n texlive-fandol-doc
Documentation for fandol

%package -n texlive-FAQ-en-doc
Summary:        Documentation for FAQ-en
Version:        svn34303.3.28

Provides:       tex-FAQ-en-doc
AutoReqProv:    No

%description -n texlive-FAQ-en-doc
Documentation for FAQ-en

%package -n texlive-first-latex-doc-doc
Summary:        Documentation for first-latex-doc
Version:        svn15878.0

Provides:       tex-first-latex-doc-doc
AutoReqProv:    No

%description -n texlive-first-latex-doc-doc
Documentation for first-latex-doc

%package -n texlive-finbib
Provides:       tex-finbib = %{tl_version}
License:        Bibtex
Summary:        A Finnish version of plain.bst
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-finbib
finbib package

%package -n texlive-facture
Provides:       tex-facture = %{tl_version}
License:        CC-BY-SA
Summary:        Generate an invoice
Version:        svn43865
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontspec.sty), tex(xunicode.sty), tex(polyglossia.sty), tex(numprint.sty)
Requires:       tex(fltpoint.sty), tex(tikz.sty), tex(graphicx.sty), tex(fancyhdr.sty)
Requires:       tex(array.sty), tex(longtable.sty), tex(colortbl.sty), tex(advdate.sty)
Requires:       tex(xargs.sty)
Provides:       tex(facture.cls) = %{tl_version}

%description -n texlive-facture
Une classe simple permettant de produire une facture, avec ou
sans TVA, avec gestion d'une adresse differente pour la
livraison et pour la facturation. A simple class that allows
production of an invoice, with or without VAT; different
addresses for delivery and for billing are permitted.

%package -n texlive-facture-doc
Summary:        Documentation for facture
Version:        svn43865
Provides:       tex-facture-doc
AutoReqProv:    No

%description -n texlive-facture-doc
Documentation for facture

%package -n texlive-frletter
Provides:       tex-frletter = %{tl_version}
License:        Public Domain
Summary:        Typeset letters in the French style
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(frletter.cls) = %{tl_version}

%description -n texlive-frletter
A small class for typesetting letters in France. No assumption
is made about the language in use. The class represents a small
modification of the beletter class, which is itself a
modification of the standard LaTeX letter class.

%package -n texlive-frletter-doc
Summary:        Documentation for frletter
Version:        svn15878.0

Provides:       tex-frletter-doc
AutoReqProv:    No

%description -n texlive-frletter-doc
Documentation for frletter

%package -n texlive-fifinddo-info-doc
Summary:        Documentation for fifinddo-info
Version:        svn29349.1.1b

Provides:       tex-fifinddo-info-doc
AutoReqProv:    No

%description -n texlive-fifinddo-info-doc
Documentation for fifinddo-info

%package -n texlive-fancyhdr-it-doc
Summary:        Documentation for fancyhdr-it
Version:        svn21912.0

Provides:       tex-fancyhdr-it-doc
AutoReqProv:    No

%description -n texlive-fancyhdr-it-doc
Documentation for fancyhdr-it

%package -n texlive-fixltxhyph
Provides:       tex-fixltxhyph = %{tl_version}
License:        LPPL 1.3
Summary:        Allow hyphenation of partially-emphasised substrings
Version:        svn25832.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty)
Provides:       tex(fixltxhyph.sty) = %{tl_version}

%description -n texlive-fixltxhyph
The package fixes the problem of TeX failing to hyphenate
letter strings that seem (to TeX) to be words, but which are
followed by an apostrophe and then an emphasis command. The
cause of the problem is not the apostrophe, but the font change
in the middle of the string. The problem arises in Catalan,
French, Italian and Romansh.

%package -n texlive-fixltxhyph-doc
Summary:        Documentation for fixltxhyph
Version:        svn25832.0.4

Provides:       tex-fixltxhyph-doc
AutoReqProv:    No

%description -n texlive-fixltxhyph-doc
Documentation for fixltxhyph

%package -n texlive-frontespizio
Provides:       tex-frontespizio = %{tl_version}
License:        LPPL
Summary:        Create a frontispiece for Italian theses
Version:        svn24054.1.4a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(afterpage.sty), tex(graphicx.sty), tex(atbegshi.sty), tex(environ.sty)
Requires:       tex(ifpdf.sty), tex(ifxetex.sty)
Provides:       tex(frontespizio.sty) = %{tl_version}

%description -n texlive-frontespizio
Typesetting a frontispiece independently of the layout of the
main document is difficult. This package provides a solution by
producing an auxiliary TeX file to be typeset on its own and
the result is automatically included at the next run. The
markup necessary for the frontispiece is written in the main
document in a frontespizio environment. Documentation is mainly
in Italian, as the style is probably apt only to theses in
Italy.

%package -n texlive-frontespizio-doc
Summary:        Documentation for frontespizio
Version:        svn24054.1.4a

Provides:       tex-frontespizio-doc
AutoReqProv:    No

%description -n texlive-frontespizio-doc
Documentation for frontespizio

%package -n texlive-feupphdteses
Provides:       tex-feupphdteses = %{tl_version}
License:        LPPL
Summary:        Typeset Engineering PhD theses at the University of Porto
Version:        svn30962.4.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(fontenc.sty), tex(inputenc.sty), tex(babel.sty)
Requires:       tex(geometry.sty), tex(xcolor.sty), tex(mathptmx.sty), tex(couriers.sty)
Requires:       tex(helvet.sty), tex(graphicx.sty), tex(grffile.sty), tex(amsmath.sty)
Requires:       tex(tikz.sty), tex(pgfplots.sty), tex(url.sty), tex(setspace.sty)
Requires:       tex(makeidx.sty), tex(caption.sty), tex(multirow.sty), tex(eurosym.sty)
Requires:       tex(array.sty), tex(tabularx.sty), tex(tabulary.sty), tex(longtable.sty)
Requires:       tex(lineno.sty), tex(siunitx.sty), tex(float.sty), tex(subcaption.sty)
Requires:       tex(adjustbox.sty), tex(enumitem.sty), tex(placeins.sty), tex(booktabs.sty)
Requires:       tex(pgfgantt.sty), tex(pdflscape.sty), tex(pdfpages.sty), tex(listings.sty)
Requires:       tex(hyperref.sty), tex(bookmark.sty), tex(backref.sty), tex(fancyhdr.sty)
Requires:       tex(natbib.sty)
Provides:       tex(feupphdteses.sty) = %{tl_version}

%description -n texlive-feupphdteses
A complete template for thesis/works of Faculdade de Engenharia
da Universidade do Porto (FEUP) Faculty of Engineering
University of Porto.

%package -n texlive-feupphdteses-doc
Summary:        Documentation for feupphdteses
Version:        svn30962.4.0

Provides:       tex-feupphdteses-doc
AutoReqProv:    No

%description -n texlive-feupphdteses-doc
Documentation for feupphdteses

%package -n texlive-fancybox
Provides:       tex-fancybox = %{tl_version}
License:        LPPL 1.2
Summary:        Variants of \fbox and other games with boxes
Version:        svn18304.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fancybox.sty) = %{tl_version}

%description -n texlive-fancybox
Provides variants of \fbox: \shadowbox, \doublebox, \ovalbox,
\Ovalbox, with helpful tools for using box macros and flexible
verbatim macros. You can box mathematics, floats, center,
flushleft, and flushright, lists, and pages.

%package -n texlive-fancybox-doc
Summary:        Documentation for fancybox
Version:        svn18304.1.4

Provides:       tex-fancybox-doc
AutoReqProv:    No

%description -n texlive-fancybox-doc
Documentation for fancybox

%package -n texlive-fancyref
Provides:       tex-fancyref = %{tl_version}
License:        GPL+
Summary:        A LaTeX package for fancy cross-referencing
Version:        svn15878.0.9c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(varioref.sty)
Provides:       tex(fancyref.sty) = %{tl_version}

%description -n texlive-fancyref
Provides fancy cross-referencing support, based on the
package's reference commands (\fref and \Fref) that recognise
what sort of object is being referenced. So, for example, the
label for a \section would be expected to be of the form
'sec:foo': the package would recognise the 'sec:' part.

%package -n texlive-fancyref-doc
Summary:        Documentation for fancyref
Version:        svn15878.0.9c

Provides:       tex-fancyref-doc
AutoReqProv:    No

%description -n texlive-fancyref-doc
Documentation for fancyref

%package -n texlive-fancyvrb
Provides:       tex-fancyvrb = %{tl_version}
License:        LPPL
Summary:        Sophisticated verbatim text
Version:        svn18492.2.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(pstricks.sty), tex(color.sty), tex(hbaw.sty)
Provides:       tex(fancyvrb.sty) = %{tl_version}, tex(fvrb-ex.sty) = %{tl_version}
Provides:       tex(hbaw.sty) = %{tl_version}, tex(hcolor.sty) = %{tl_version}

%description -n texlive-fancyvrb
Flexible handling of verbatim text including: verbatim commands
in footnotes; a variety of verbatim environments with many
parameters; ability to define new customized verbatim
environments; save and restore verbatim text and environments;
write and read files in verbatim mode; build "example"
environments (showing both result and verbatim source).

%package -n texlive-fancyvrb-doc
Summary:        Documentation for fancyvrb
Version:        svn18492.2.8

Provides:       tex-fancyvrb-doc
AutoReqProv:    No

%description -n texlive-fancyvrb-doc
Documentation for fancyvrb

%package -n texlive-float
Provides:       tex-float = %{tl_version}
License:        LPPL
Summary:        Improved interface for floating objects
Version:        svn15878.1.3d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(float.sty) = %{tl_version}

%description -n texlive-float
Improves the interface for defining floating objects such as
figures and tables. Introduces the boxed float, the ruled float
and the plaintop float. You can define your own floats and
improve the behaviour of the old ones. The package also
provides the H float modifier option of the obsolete here
package. You can select this as automatic default with
\floatplacement{figure}{H}.

%package -n texlive-float-doc
Summary:        Documentation for float
Version:        svn15878.1.3d

Provides:       tex-float-doc
AutoReqProv:    No

%description -n texlive-float-doc
Documentation for float

%package -n texlive-fontspec
Provides:       tex-fontspec = %{tl_version}
License:        LPPL 1.3
Summary:        Advanced font selection in XeLaTeX and LuaLaTeX
Version:        svn48320
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-iftex, tex-kastrup, tex-l3kernel, tex-l3packages
Requires:       tex-lm, tex(fontenc.sty), tex(xunicode.sty), tex(expl3.sty)
Requires:       tex(xparse.sty), tex(luaotfload.sty)
Provides:       tex(fontspec-luatex.sty) = %{tl_version}
Provides:       tex(fontspec-patches.sty) = %{tl_version}
Provides:       tex(fontspec-xetex.sty) = %{tl_version}, tex(fontspec.cfg) = %{tl_version}
Provides:       tex(fontspec.sty) = %{tl_version}

%description -n texlive-fontspec
Fontspec is a package for XeLaTeX and LuaLaTeX. It provides an
automatic and unified interface to feature-rich AAT and
OpenType fonts through the NFSS in LaTeX running on XeTeX or
LuaTeX engines. The package requires the l3kernel and xparse
bundles from the LaTeX 3 development team.

%package -n texlive-fontspec-doc
Summary:        Documentation for fontspec
Version:        svn48320
Provides:       tex-fontspec-doc
AutoReqProv:    No
Requires:       tex-iftex-doc, tex-kastrup-doc, tex-l3kernel-doc, tex-l3packages-doc
Requires:       tex-lm-doc

%description -n texlive-fontspec-doc
Documentation for fontspec

%package -n texlive-fp
Provides:       tex-fp = %{tl_version}
License:        LPPL
Summary:        Fixed point arithmetic
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp-upn.sty)
Provides:       tex(defpattern.sty) = %{tl_version}, tex(fp-addons.sty) = %{tl_version}
Provides:       tex(fp-basic.sty) = %{tl_version}, tex(fp-eqn.sty) = %{tl_version}
Provides:       tex(fp-eval.sty) = %{tl_version}, tex(fp-exp.sty) = %{tl_version}
Provides:       tex(fp-pas.sty) = %{tl_version}, tex(fp-random.sty) = %{tl_version}
Provides:       tex(fp-snap.sty) = %{tl_version}, tex(fp-trigo.sty) = %{tl_version}
Provides:       tex(fp-upn.sty) = %{tl_version}, tex(fp.sty) = %{tl_version}
Provides:       tex(lfp.sty) = %{tl_version}, tex(fp.tex) = %{tl_version}

%description -n texlive-fp
An extensive collection of arithmetic operations for fixed
point real numbers of high precision.

%package -n texlive-fp-doc
Summary:        Documentation for fp
Version:        svn15878.0

Provides:       tex-fp-doc
AutoReqProv:    No

%description -n texlive-fp-doc
Documentation for fp

%package -n texlive-fast-diagram
Provides:       tex-fast-diagram = %{tl_version}
License:        LPPL 1.3
Summary:        Easy generation of FAST diagrams
Version:        svn29264.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty), tex(relsize.sty), tex(xargs.sty)
Provides:       tex(fast-diagram.sty) = %{tl_version}

%description -n texlive-fast-diagram
The package provides simple means of producing FAST diagrams,
using TikZ/pgf tools. FAST diagrams are useful for functional
analysis techniques in design methods.

%package -n texlive-fast-diagram-doc
Summary:        Documentation for fast-diagram
Version:        svn29264.1.1

Provides:       tex-fast-diagram-doc
AutoReqProv:    No

%description -n texlive-fast-diagram-doc
Documentation for fast-diagram

%package -n texlive-fitbox
Provides:       tex-fitbox = %{tl_version}
License:        LPPL 1.3
Summary:        Fit graphics on a page
Version:        svn38139.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty)
Provides:       tex(fitbox.sty) = %{tl_version}

%description -n texlive-fitbox
The package allows a box (usually an \includegraphics box) to
fit on the page. It scales the box to the maximal allowed size
within the user-set limits. If there is not enough space on the
page, the box is moved to the next one.

%package -n texlive-fitbox-doc
Summary:        Documentation for fitbox
Version:        svn38139.1.00

Provides:       tex-fitbox-doc
AutoReqProv:    No

%description -n texlive-fitbox-doc
Documentation for fitbox

%package -n texlive-flowchart
Provides:       tex-flowchart = %{tl_version}
License:        LPPL 1.3
Summary:        Shapes for drawing flowcharts, using TikZ
Version:        svn36572.3.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(makeshape.sty), tex(tikz.sty)
Provides:       tex(flowchart.sty) = %{tl_version}

%description -n texlive-flowchart
The package provides a set of 'traditional' flowchart element
shapes; the documentation shows how to build a flowchart from
these elements, using pgf/TikZ. The package also requires the
makeshape package.

%package -n texlive-flowchart-doc
Summary:        Documentation for flowchart
Version:        svn36572.3.3

Provides:       tex-flowchart-doc
AutoReqProv:    No

%description -n texlive-flowchart-doc
Documentation for flowchart

%package -n texlive-forest
Provides:       tex-forest = %{tl_version}
License:        LPPL 1.3
Summary:        Drawing (linguistic) trees
Version:        svn44797
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(pgfopts.sty), tex(etoolbox.sty), tex(elocalloc.sty)
Requires:       tex(environ.sty)
Provides:       tex(forest.sty) = %{tl_version}

%description -n texlive-forest
The package is provides a PGF/TikZ-based mechanism for drawing
linguistic (and other kinds of) trees. Its main features are: a
packing algorithm which can produce very compact trees; a user-
friendly interface consisting of the familiar bracket encoding
of trees plus the key-value interface to option-setting; many
tree-formatting options, with control over option values of
individual nodes and mechanisms for their manipulation; the
possibility to decorate the tree using the full power of
PGF/TikZ; and an externalization mechanism sensitive to code-
changes.

%package -n texlive-forest-doc
Summary:        Documentation for forest
Version:        svn44797
Provides:       tex-forest-doc
AutoReqProv:    No

%description -n texlive-forest-doc
Documentation for forest

%package -n texlive-facsimile
Provides:       tex-facsimile = %{tl_version}
License:        LPPL
Summary:        Document class for preparing faxes
Version:        svn21328.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(lastpage.sty), tex(fancyhdr.sty)
Provides:       tex(fac-de.cfg) = %{tl_version}, tex(fac-en.cfg) = %{tl_version}
Provides:       tex(facsimile.cls) = %{tl_version}

%description -n texlive-facsimile
The facsimile class provides a simple interface for creating a
document for sending as a fax, with LaTeX. The class covers two
areas: First, a title page is created with a detailed fax
header; second, every page gets headers and footers so that the
recipient can be sure that every page has been received and all
pages are complete, and in the correct order. The class evolved
from the fax package, and provides much better language
support.

%package -n texlive-facsimile-doc
Summary:        Documentation for facsimile
Version:        svn21328.1.0

Provides:       tex-facsimile-doc
AutoReqProv:    No

%description -n texlive-facsimile-doc
Documentation for facsimile

%package -n texlive-factura
Provides:       tex-factura = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset and calculate invoices according to Venezuelan law
Version:        svn48333
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xifthen.sty), tex(etoolbox.sty), tex(xparse.sty), tex(textpos.sty)
Requires:       tex(geometry.sty), tex(xstring.sty), tex(pbox.sty), tex(calc.sty)
Requires:       tex(fp-upn.sty), tex(numprint.sty), tex(tikz.sty), tex(tabularx.sty)
Requires:       tex(environ.sty), tex(fancyhdr.sty), tex(graphicx.sty), tex(babel.sty)
Requires:       tex(fontenc.sty), tex(lmodern.sty), tex(zref-savepos.sty), tex(eso-pic.sty)
Provides:       tex(factura.cls) = %{tl_version}, tex(factura.def) = %{tl_version}

%description -n texlive-factura
The class provides convenient means for typesetting and
calculating invoices, according to the requirements of SENIAT
legislation (tax collecting entity of the Bolivarian Republic
of Venezuela). The author suggests that the class may well be
re-usable for other jurisdictions, by rather simple editing.

%package -n texlive-factura-doc
Summary:        Documentation for factura
Version:        svn48333
Provides:       tex-factura-doc
AutoReqProv:    No

%description -n texlive-factura-doc
Documentation for factura

%package -n texlive-fancylabel
Provides:       tex-fancylabel = %{tl_version}
License:        LPPL 1.2
Summary:        Complex labelling with LaTeX
Version:        svn46736
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(ifthen.sty), tex(suffix.sty)
Provides:       tex(fancylabel.sty) = %{tl_version}

%description -n texlive-fancylabel
The package provides a complex labelling scheme. It is designed
to support the needs of the author's chemschemex package

%package -n texlive-fancylabel-doc
Summary:        Documentation for fancylabel
Version:        svn46736
Provides:       tex-fancylabel-doc
AutoReqProv:    No

%description -n texlive-fancylabel-doc
Documentation for fancylabel

%package -n texlive-fancynum
Provides:       tex-fancynum = %{tl_version}
License:        LPPL
Summary:        Typeset numbers
Version:        svn15878.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fancynum.sty) = %{tl_version}

%description -n texlive-fancynum
A LaTeX package for typesetting numbers, in particular floating
point numbers, such as you find in program output.

%package -n texlive-fancynum-doc
Summary:        Documentation for fancynum
Version:        svn15878.0.92

Provides:       tex-fancynum-doc
AutoReqProv:    No

%description -n texlive-fancynum-doc
Documentation for fancynum

%package -n texlive-fancypar
Provides:       tex-fancypar = %{tl_version}
License:        LPPL 1.3
Summary:        Decoration of individual paragraphs
Version:        svn18018.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(tikz.sty), tex(xcolor.sty)
Provides:       tex(fancypar.sty) = %{tl_version}

%description -n texlive-fancypar
Decorates individual paragraphs of a document, offering five
pre-defined styles. The command offers an optional 'key-value'
argument with the user may define parameters of the selected
style. Predefined styles offer a spiral-notebook, a zebra-like,
a dashed, a marked design, and an underlined style. Users may
also define their own styles. Decorated paragraphs may not
include displayed mathematics.

%package -n texlive-fancypar-doc
Summary:        Documentation for fancypar
Version:        svn18018.1.1

Provides:       tex-fancypar-doc
AutoReqProv:    No

%description -n texlive-fancypar-doc
Documentation for fancypar

%package -n texlive-fancyslides
Provides:       tex-fancyslides = %{tl_version}
License:        LPPL 1.3
Summary:        Custom presentation class built upon LaTeX Beamer
Version:        svn36263.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(framed.sty), tex(tikz.sty)
Provides:       tex(fancyslides.cls) = %{tl_version}

%description -n texlive-fancyslides
This class is prepared for short presentations with a modern
look & feel. It offers the following features: custom
background for each slide, predefined types of slides,
simplified commands (e.g. for starting and ending slide). The
class is built upon LaTeX beamer, so all beamer commands should
work.

%package -n texlive-fancyslides-doc
Summary:        Documentation for fancyslides
Version:        svn36263.1.0

Provides:       tex-fancyslides-doc
AutoReqProv:    No

%description -n texlive-fancyslides-doc
Documentation for fancyslides

%package -n texlive-fancytabs
Provides:       tex-fancytabs = %{tl_version}
License:        LPPL 1.3
Summary:        Fancy page border tabs
Version:        svn27684.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(fancytabs.sty) = %{tl_version}

%description -n texlive-fancytabs
The package can typeset tabs on the side of a page. It requires
TikZ from the pgf bundle.

%package -n texlive-fancytabs-doc
Summary:        Documentation for fancytabs
Version:        svn27684.1.8

Provides:       tex-fancytabs-doc
AutoReqProv:    No

%description -n texlive-fancytabs-doc
Documentation for fancytabs

%package -n texlive-fancytooltips
Provides:       tex-fancytooltips = %{tl_version}
License:        LPPL 1.2
Summary:        Include a wide range of material in PDF tooltips
Version:        svn27129.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(xkeyval.sty), tex(atbegshi.sty), tex(transparent.sty)
Requires:       tex(eso-pic.sty)
Provides:       tex(fancytooltips.sty) = %{tl_version}

%description -n texlive-fancytooltips
The package was inspired by the cooltooltips package. In
contrast to cooltooltips, fancytooltips allows inclusion of
tooltips which contain arbitrary TeX material or a series of
TeX materials (animated graphics) from an external PDF file. To
see the tooltips, you have to open the files in Adobe Reader.
The links and JavaScripts are inserted using eforms package
from the AcroTeX bundle.

%package -n texlive-fancytooltips-doc
Summary:        Documentation for fancytooltips
Version:        svn27129.1.8

Provides:       tex-fancytooltips-doc
AutoReqProv:    No

%description -n texlive-fancytooltips-doc
Documentation for fancytooltips

%package -n texlive-fcolumn
Provides:       tex-fcolumn = %{tl_version}
License:        LPPL 1.2
Summary:        Typesetting financial tables
Version:        svn38489

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty)
Provides:       tex(fcolumn.sty) = %{tl_version}

%description -n texlive-fcolumn
In financial reports, text and currency amounts are regularly
put in one table, e.g., a year balance or a profit-and-loss
overview. This package provides the settings for automatically
typesetting such columns, including the sum line (preceded by a
rule of the correct width) using the specifier "f".

%package -n texlive-fcolumn-doc
Summary:        Documentation for fcolumn
Version:        svn38489

Provides:       tex-fcolumn-doc
AutoReqProv:    No

%description -n texlive-fcolumn-doc
Documentation for fcolumn

%package -n texlive-fifo-stack
Provides:       tex-fifo-stack = %{tl_version}
License:        LPPL
Summary:        FIFO and stack implementation for package writers
Version:        svn33288.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(fifo-stack.sty) = %{tl_version}

%description -n texlive-fifo-stack
A LaTeX implementation of a combined FIFO Stack modified from
the existing stack package by Benjamin Bayart. The package
renames the original's \Push and \Pop commands \FSPush and
\FSPop, and which work on the top/end of the FIFO/Stack), and
adds the ability to \FSUnshift and \FSShift from the the
bottom(front) of the FIFO/Stack.

%package -n texlive-fifo-stack-doc
Summary:        Documentation for fifo-stack
Version:        svn33288.1.0

Provides:       tex-fifo-stack-doc
AutoReqProv:    No

%description -n texlive-fifo-stack-doc
Documentation for fifo-stack

%package -n texlive-figsize
Provides:       tex-figsize = %{tl_version}
License:        LPPL
Summary:        Auto-size graphics
Version:        svn18784.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(subfigure.sty), tex(graphicx.sty), tex(ifthen.sty)
Provides:       tex(figsize.sty) = %{tl_version}

%description -n texlive-figsize
The FigSize package enables automatic sizing of graphics,
especially when including graphics with the graphicx package.
The user only has to specify the number of graphics that should
fit to a page or fraction there of and the package will
dynamically calculate the correct graphics sizes relative to
the page size. Thus, graphics can be auto-sized to fill a whole
page or fraction and manual changes of graphic sizes are never
needed when changing document layouts. Finally, the package's
dynamic lengths can be used to allow other document element
sizes to be dynamic.

%package -n texlive-figsize-doc
Summary:        Documentation for figsize
Version:        svn18784.0.1

Provides:       tex-figsize-doc
AutoReqProv:    No

%description -n texlive-figsize-doc
Documentation for figsize

%package -n texlive-filecontents
Provides:       tex-filecontents = %{tl_version}
License:        LPPL
Summary:        Extended filecontents and filecontents* environments
Version:        svn47890
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(filecontents.sty) = %{tl_version}

%description -n texlive-filecontents
LaTeX2e's filecontents and filecontents* environments enable a
LaTeX source file to generate external files as it runs through
LaTeX. However, there are two limitations of these
environments: they refuse to overwrite existing files, and they
can only be used in the preamble of a document. The
filecontents package removes these limitations, letting you
overwrite existing files and letting you use
filecontents/filecontents* anywhere.

%package -n texlive-filecontents-doc
Summary:        Documentation for filecontents
Version:        svn47890
Provides:       tex-filecontents-doc
AutoReqProv:    No

%description -n texlive-filecontents-doc
Documentation for filecontents

%package -n texlive-filedate
Provides:       tex-filedate = %{tl_version}
License:        LPPL
Summary:        Access and compare info and modification dates
Version:        svn29529.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(filedate.sty) = %{tl_version}

%description -n texlive-filedate
The package provides basic access to the date of a LaTeX source
file according to its \Provides... entry (the "info date") as
well as to its modification date according to \pdffilemoddate
if the latter is available.

%package -n texlive-filedate-doc
Summary:        Documentation for filedate
Version:        svn29529.0

Provides:       tex-filedate-doc
AutoReqProv:    No

%description -n texlive-filedate-doc
Documentation for filedate

%package -n texlive-filehook
Provides:       tex-filehook = %{tl_version}
License:        LPPL 1.3
Summary:        Hooks for input files
Version:        svn24280.0.5d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(currfile.sty), tex(kvoptions.sty), tex(pgfkeys.sty)
Provides:       tex(filehook-fink.sty) = %{tl_version}, tex(filehook-listings.sty) = %{tl_version}
Provides:       tex(filehook-memoir.sty) = %{tl_version}
Provides:       tex(filehook-scrlfile.sty) = %{tl_version}
Provides:       tex(filehook.sty) = %{tl_version}, tex(pgf-filehook.sty) = %{tl_version}

%description -n texlive-filehook
The package provides several file hooks (AtBegin, AtEnd, ...)
for files read by \input, \include and \InputIfFileExists.
General hooks for all such files (e.g. all \include'd ones) and
file specific hooks only used for named files are provided; two
hooks are provided for the end of \included files -- one
before, and one after the final \clearpage.

%package -n texlive-filehook-doc
Summary:        Documentation for filehook
Version:        svn24280.0.5d

Provides:       tex-filehook-doc
AutoReqProv:    No

%description -n texlive-filehook-doc
Documentation for filehook

%package -n texlive-fileinfo
Provides:       tex-fileinfo = %{tl_version}
License:        LPPL 1.3
Summary:        Enhanced display of LaTeX File Information
Version:        svn28421.0.81a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(myfilist.sty) = %{tl_version}, tex(readprov.sty) = %{tl_version}

%description -n texlive-fileinfo
The bundle provides two packages, readprov and myfilist. The
readprov package provides a means of reading file information
without loading the body of the file. The myfilist package uses
readprov and controls what \listfiles will report.

%package -n texlive-fileinfo-doc
Summary:        Documentation for fileinfo
Version:        svn28421.0.81a

Provides:       tex-fileinfo-doc
AutoReqProv:    No

%description -n texlive-fileinfo-doc
Documentation for fileinfo

%package -n texlive-filemod
Provides:       tex-filemod = %{tl_version}
License:        LPPL 1.3
Summary:        Provide file modification times, and compare them
Version:        svn24042.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pdftexcmds.sty)
Provides:       tex(filemod-expmin.tex) = %{tl_version}, tex(filemod.tex) = %{tl_version}
Provides:       tex(filemod-expmin.sty) = %{tl_version}, tex(filemod.sty) = %{tl_version}

%description -n texlive-filemod
The package provides macros to read and compare the
modification dates of files. The files may be .tex files,
images or other files (as long as they can be found by LaTeX).
It uses the \pdffilemoddate primitive of pdfLaTeX to find the
file modification date as PDF date string, parses the string
and returns the value to the user. The package will also work
for DVI output with recent versions of the LaTeX compiler which
uses pdfLaTeX in DVI mode. The functionality is provided by
purely expandable macros or by faster but non-expandable ones.

%package -n texlive-filemod-doc
Summary:        Documentation for filemod
Version:        svn24042.1.2

Provides:       tex-filemod-doc
AutoReqProv:    No

%description -n texlive-filemod-doc
Documentation for filemod

%package -n texlive-fink
Provides:       tex-fink = %{tl_version}
License:        LPPL
Summary:        The LaTeX2e File Name Keeper
Version:        svn24329.2.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty)
Provides:       tex(fink.sty) = %{tl_version}

%description -n texlive-fink
This package "looks over your shoulder" and keeps track of
files \input'ed (the LaTeX way) or \include'ed in your
document. You then have permanent access to the name of the
file currently being processed through the macro \finkfile.
FiNK also comes with support for AUC-TeX. As of version 2.2.1,
FiNK has been deprecated and is not maintained anymore. People
interested in FiNK's functionality are invited to use a package
named currfile instead.

%package -n texlive-fink-doc
Summary:        Documentation for fink
Version:        svn24329.2.2.1

Provides:       tex-fink-doc
AutoReqProv:    No

%description -n texlive-fink-doc
Documentation for fink

%package -n texlive-finstrut
Provides:       tex-finstrut = %{tl_version}
License:        LPPL 1.3
Summary:        Adjust behaviour of the ends of footnotes
Version:        svn21719.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(finstrut.sty) = %{tl_version}

%description -n texlive-finstrut
The LaTeX internal command \@finalstrut is used automatically
used at the end of footnote texts to insert a strut to avoid
mis-spacing of multiple footnotes. Unfortunately the command
can cause a blank line at the end of a footnote. The package
provides a solution to this problem.

%package -n texlive-finstrut-doc
Summary:        Documentation for finstrut
Version:        svn21719.0.5

Provides:       tex-finstrut-doc
AutoReqProv:    No

%description -n texlive-finstrut-doc
Documentation for finstrut

%package -n texlive-fithesis
Provides:       tex-fithesis = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis class and template for Masaryk University (Brno, Czech Republic)
Version:        svn47409
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty), tex(etoolbox.sty), tex(ifxetex.sty), tex(ifluatex.sty)
Requires:       tex(inputenc.sty), tex(cmap.sty), tex(fontenc.sty)
Provides:       tex(fithesis.cls) = %{tl_version}, tex(fithesis2.cls) = %{tl_version}
Provides:       tex(fithesis3.cls) = %{tl_version}, tex(fithesis-czech.def) = %{tl_version}
Provides:       tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-czech.def) = %{tl_version}, tex(fithesis-english.def) = %{tl_version}
Provides:       tex(fithesis-slovak.def) = %{tl_version}
Provides:       tex(fithesis-base.sty) = %{tl_version}, tex(fithesis-10.clo) = %{tl_version}
Provides:       tex(fithesis-11.clo) = %{tl_version}, tex(fithesis-12.clo) = %{tl_version}
Provides:       tex(fithesis-base.sty) = %{tl_version}, tex(fithesis-econ.sty) = %{tl_version}
Provides:       tex(fithesis-fi.sty) = %{tl_version}, tex(fithesis-fsps.sty) = %{tl_version}
Provides:       tex(fithesis-fss.sty) = %{tl_version}, tex(fithesis-law.sty) = %{tl_version}
Provides:       tex(fithesis-med.sty) = %{tl_version}, tex(fithesis-ped.sty) = %{tl_version}
Provides:       tex(fithesis-phil.sty) = %{tl_version}, tex(fithesis-sci.sty) = %{tl_version}

%description -n texlive-fithesis
A document class for the typesetting of theses at the Masaryk
University (Brno, Czech Republic). The class has been designed
for easy extensibility by style and locale files of other
academic institutions.

%package -n texlive-fithesis-doc
Summary:        Documentation for fithesis
Version:        svn47409
Provides:       tex-fithesis-doc
AutoReqProv:    No

%description -n texlive-fithesis-doc
Documentation for fithesis

%package -n texlive-fixfoot
Provides:       tex-fixfoot = %{tl_version}
License:        LPPL
Summary:        Multiple use of the same footnote text
Version:        svn17131.0.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fixfoot.sty) = %{tl_version}

%description -n texlive-fixfoot
Provides a \DeclareFixedFootnote command to provide a single
command for a frequently-used footnote. The package ensures
that only one instance of the footnote text appears on each
page (LaTeX needs to be run several times to achieve this).

%package -n texlive-fixfoot-doc
Summary:        Documentation for fixfoot
Version:        svn17131.0.3a

Provides:       tex-fixfoot-doc
AutoReqProv:    No

%description -n texlive-fixfoot-doc
Documentation for fixfoot

%package -n texlive-fixme
Provides:       tex-fixme = %{tl_version}
License:        LPPL
Summary:        Insert "fixme" notes into draft documents
Version:        svn43413
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(verbatim.sty), tex(xkeyval.sty), tex(color.sty)
Requires:       tex(marginnote.sty), tex(pdfcomment.sty)
Requires:       tex(xcolor.sty), tex(changebar.sty)
Provides:       tex(fixme.sty) = %{tl_version}, tex(fxenvlayoutcolor.sty) = %{tl_version}
Provides:       tex(fxenvlayoutcolorsig.sty) = %{tl_version}
Provides:       tex(fxlayoutmarginnote.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfcmargin.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfcnote.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfcsigmargin.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfcsignote.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfmargin.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfnote.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfsigmargin.sty) = %{tl_version}
Provides:       tex(fxlayoutpdfsignote.sty) = %{tl_version}
Provides:       tex(fxtargetlayoutchangebar.sty) = %{tl_version}
Provides:       tex(fxtargetlayoutcolor.sty) = %{tl_version}
Provides:       tex(fxtargetlayoutcolorcb.sty) = %{tl_version}
Provides:       tex(fxthemecolor.sty) = %{tl_version}, tex(fxthemecolorsig.sty) = %{tl_version}
Provides:       tex(fxthemesignature.sty) = %{tl_version}

%description -n texlive-fixme
This package provides a way to insert fixme notes in documents
being developed (in draft mode). Such notes can appear in the
margin of the document, as index entries, in the log file and
as warnings on stdout. It is also possible to summarize them in
a list. If your document is in a final version, any remaining
fixme notes will produce an error. FiXme also comes with
support for AUC-TeX.

%package -n texlive-fixme-doc
Summary:        Documentation for fixme
Version:        svn43413
Provides:       tex-fixme-doc
AutoReqProv:    No

%description -n texlive-fixme-doc
Documentation for fixme

%package -n texlive-fixmetodonotes
Provides:       tex-fixmetodonotes = %{tl_version}
License:        Public Domain
Summary:        Add notes on document development
Version:        svn30168.0.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(color.sty), tex(transparent.sty), tex(watermark.sty)
Requires:       tex(fix-cm.sty), tex(ulem.sty), tex(tocloft.sty)
Provides:       tex(fixmetodonotes.sty) = %{tl_version}

%description -n texlive-fixmetodonotes
The package provides tools to highlight FIXME and TODO
annotations. The command \listofnotes prints a list of
outstanding notes, with links to the pages on which they
appear.

%package -n texlive-fixmetodonotes-doc
Summary:        Documentation for fixmetodonotes
Version:        svn30168.0.2.2

Provides:       tex-fixmetodonotes-doc
AutoReqProv:    No

%description -n texlive-fixmetodonotes-doc
Documentation for fixmetodonotes

%package -n texlive-fjodor
Provides:       tex-fjodor = %{tl_version}
License:        GPL+
Summary:        A selection of layout styles
Version:        svn20220.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fjodor.sty) = %{tl_version}

%description -n texlive-fjodor
The package provides several page layouts, selectable by
package options.

%package -n texlive-fjodor-doc
Summary:        Documentation for fjodor
Version:        svn20220.0

Provides:       tex-fjodor-doc
AutoReqProv:    No

%description -n texlive-fjodor-doc
Documentation for fjodor

%package -n texlive-flabels
Provides:       tex-flabels = %{tl_version}
License:        LPPL
Summary:        Labels for files and folders
Version:        svn17272.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(flabels.sty) = %{tl_version}

%description -n texlive-flabels
Macros for typesetting pretty labels (optionally colored) for
the back of files or binders (currently only the special A4
"Leitz-Ordner" ring binder is supported).

%package -n texlive-flabels-doc
Summary:        Documentation for flabels
Version:        svn17272.1.0

Provides:       tex-flabels-doc
AutoReqProv:    No

%description -n texlive-flabels-doc
Documentation for flabels

%package -n texlive-flacards
Provides:       tex-flacards = %{tl_version}
License:        GPL+
Summary:        Generate flashcards for printing
Version:        svn19440.0.1.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty)
Provides:       tex(flacards.cls) = %{tl_version}

%description -n texlive-flacards
The flacards class provides an easy interface to produce
flashcards. It will print several cards per page, on both sides
of the paper.

%package -n texlive-flacards-doc
Summary:        Documentation for flacards
Version:        svn19440.0.1.1b

Provides:       tex-flacards-doc
AutoReqProv:    No

%description -n texlive-flacards-doc
Documentation for flacards

%package -n texlive-flagderiv
Provides:       tex-flagderiv = %{tl_version}
License:        GPL+
Summary:        Flag style derivation package
Version:        svn15878.0.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(array.sty), tex(longtable.sty)
Provides:       tex(flagderiv.sty) = %{tl_version}

%description -n texlive-flagderiv
The flagderiv package is used to create mathematical
derivations using the flag/flagpole notation. The package
features an intuitive command syntax, opening and closing
multiple flagpoles, different comment styles, customizable
symbols and label namespaces.

%package -n texlive-flagderiv-doc
Summary:        Documentation for flagderiv
Version:        svn15878.0.10

Provides:       tex-flagderiv-doc
AutoReqProv:    No

%description -n texlive-flagderiv-doc
Documentation for flagderiv

%package -n texlive-flashcards
Provides:       tex-flashcards = %{tl_version}
License:        GPL+
Summary:        A class for typesetting flashcards
Version:        svn19667.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(geometry.sty)
Provides:       tex(avery5371.cfg) = %{tl_version}, tex(avery5388.cfg) = %{tl_version}
Provides:       tex(flashcards.cls) = %{tl_version}

%description -n texlive-flashcards
The FlashCards class provides for the typesetting of flash
cards. By flash card, we mean a two sided card which has a
prompt or a question on one side and the response or the answer
on the flip (back) side. Flash cards come in many sizes
depending on the nature of the information they contain.

%package -n texlive-flashcards-doc
Summary:        Documentation for flashcards
Version:        svn19667.1.0.1

Provides:       tex-flashcards-doc
AutoReqProv:    No

%description -n texlive-flashcards-doc
Documentation for flashcards

%package -n texlive-flashmovie
Provides:       tex-flashmovie = %{tl_version}
License:        LPPL 1.3
Summary:        Directly embed flash movies into PDF files
Version:        svn25768.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(ifthen.sty)
Provides:       tex(flashmovie.sty) = %{tl_version}

%description -n texlive-flashmovie
The package allows direct embedding of flash movies into PDF
files. It is designed for use with pdflatex. The package takes
advantage of the embedded Adobe Flash player in Adobe Reader 9;
the reader is invoked with the 'rich media annotation' feature,
described in "Adobe Supplement to the ISO 32000 BaseVersion:        
1.7 ExtensionLevel: 3". This method of embedding movies is
attractive since it removes all platform dependencies; however,
the user is required to use Acrobat 9.

%package -n texlive-flashmovie-doc
Summary:        Documentation for flashmovie
Version:        svn25768.0.4

Provides:       tex-flashmovie-doc
AutoReqProv:    No

%description -n texlive-flashmovie-doc
Documentation for flashmovie

%package -n texlive-flipbook
Provides:       tex-flipbook = %{tl_version}
License:        LPPL
Summary:        Typeset flipbook animations, in the corners of documents
Version:        svn25584.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyhdr.sty), tex(graphicx.sty), tex(scalefnt.sty), tex(verbatim.sty)
Requires:       tex(everypage.sty), tex(ifthen.sty)
Provides:       tex(flipbook.sty) = %{tl_version}

%description -n texlive-flipbook
The package provides techniques for adding flip book animations
in the corner of your LaTeX documents (using images or ASCII
art). Animations are defined as a set of numbered files (e.g.,
"im1.pdf", "im2.pdf", "im3.pdf", ...). The package relies on
fancyhdr to control the corners.

%package -n texlive-flipbook-doc
Summary:        Documentation for flipbook
Version:        svn25584.0.2

Provides:       tex-flipbook-doc
AutoReqProv:    No

%description -n texlive-flipbook-doc
Documentation for flipbook

%package -n texlive-flippdf
Provides:       tex-flippdf = %{tl_version}
License:        LPPL
Summary:        Horizontal flipping of pages with pdfLaTeX
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(everypage.sty)
Provides:       tex(flippdf.sty) = %{tl_version}

%description -n texlive-flippdf
The package allows the production of a document with pages
"mirrored". This is sometimes required by publishers who want
camera-ready documents to be printed on transparent film (to be
viewed from the "wrong" side). The package requires everypage,
and only works with pdfLaTeX in PDF mode.

%package -n texlive-flippdf-doc
Summary:        Documentation for flippdf
Version:        svn15878.1.0

Provides:       tex-flippdf-doc
AutoReqProv:    No

%description -n texlive-flippdf-doc
Documentation for flippdf

%package -n texlive-floatflt
Provides:       tex-floatflt = %{tl_version}
License:        LPPL
Summary:        Wrap text around floats
Version:        svn25540.1.31

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(floatflt.sty) = %{tl_version}

%description -n texlive-floatflt
The package can float text around figures and tables which do
not span the full width of a page; it improves upon floatfig,
and allows tables/figures to be set left/right or alternating
on even/odd pages.

%package -n texlive-floatflt-doc
Summary:        Documentation for floatflt
Version:        svn25540.1.31

Provides:       tex-floatflt-doc
AutoReqProv:    No

%description -n texlive-floatflt-doc
Documentation for floatflt

%package -n texlive-floatrow
Provides:       tex-floatrow = %{tl_version}
License:        LPPL
Summary:        Modifying the layout of floats
Version:        svn15878.0.3b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(caption3.sty), tex(color.sty), tex(fr-subfig.sty)
Requires:       tex(fancybox.sty), tex(longtable.sty)
Provides:       tex(floatpagestyle.sty) = %{tl_version}, tex(floatrow.sty) = %{tl_version}
Provides:       tex(fr-fancy.sty) = %{tl_version}, tex(fr-longtable.sty) = %{tl_version}
Provides:       tex(fr-subfig.sty) = %{tl_version}, tex(listpen.sty) = %{tl_version}

%description -n texlive-floatrow
The floatrow package provides many ways to customize layouts of
floating environments and has code to cooperate with the
caption 3.x package. The package offers mechanisms to put
floats side by side, and to put the caption beside its float.
The floatrow settings could be expanded to the floats created
by packages rotating, wrapfig, subfig (in the case of rows of
subfloats), and longtable.

%package -n texlive-floatrow-doc
Summary:        Documentation for floatrow
Version:        svn15878.0.3b

Provides:       tex-floatrow-doc
AutoReqProv:    No

%description -n texlive-floatrow-doc
Documentation for floatrow

%package -n texlive-flowfram
Provides:       tex-flowfram = %{tl_version}
License:        LPPL 1.3
Summary:        Create text frames for posters, brochures or magazines
Version:        svn35291.1.17

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(xkeyval.sty), tex(graphics.sty), tex(afterpage.sty)
Requires:       tex(xfor.sty), tex(etoolbox.sty), tex(color.sty)
Provides:       tex(flowfram.sty) = %{tl_version}

%description -n texlive-flowfram
The flowfram package enables you to create frames in a document
such that the contents of the document environment flow from
one frame to the next in the order in which they were defined.
This is useful for creating posters or magazines, indeed any
form of document that does not conform to the standard one or
two column layout.

%package -n texlive-flowfram-doc
Summary:        Documentation for flowfram
Version:        svn35291.1.17

Provides:       tex-flowfram-doc
AutoReqProv:    No

%description -n texlive-flowfram-doc
Documentation for flowfram

%package -n texlive-fmp
Provides:       tex-fmp = %{tl_version}
License:        LPPL
Summary:        Include Functional MetaPost in LaTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(verbatim.sty)
Provides:       tex(fmp.sty) = %{tl_version}

%description -n texlive-fmp
fmp package

%package -n texlive-fmp-doc
Summary:        Documentation for fmp
Version:        svn15878.0

Provides:       tex-fmp-doc
AutoReqProv:    No

%description -n texlive-fmp-doc
Documentation for fmp

%package -n texlive-fmtcount
Provides:       tex-fmtcount = %{tl_version}
License:        LPPL 1.3
Summary:        Display the value of a LaTeX counter in a variety of formats
Version:        svn46159
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(keyval.sty), tex(xkeyval.sty), tex(etoolbox.sty)
Requires:       tex(ifxetex.sty), tex(amsgen.sty)
Provides:       tex(fc-UKenglish.def) = %{tl_version}, tex(fc-USenglish.def) = %{tl_version}
Provides:       tex(fc-american.def) = %{tl_version}, tex(fc-british.def) = %{tl_version}
Provides:       tex(fc-english.def) = %{tl_version}, tex(fc-francais.def) = %{tl_version}
Provides:       tex(fc-french.def) = %{tl_version}, tex(fc-frenchb.def) = %{tl_version}
Provides:       tex(fc-german.def) = %{tl_version}, tex(fc-germanb.def) = %{tl_version}
Provides:       tex(fc-italian.def) = %{tl_version}, tex(fc-ngerman.def) = %{tl_version}
Provides:       tex(fc-ngermanb.def) = %{tl_version}, tex(fc-portuges.def) = %{tl_version}
Provides:       tex(fc-portuguese.def) = %{tl_version}, tex(fc-spanish.def) = %{tl_version}
Provides:       tex(fcnumparser.sty) = %{tl_version}, tex(fcprefix.sty) = %{tl_version}
Provides:       tex(fmtcount.sty) = %{tl_version}

%description -n texlive-fmtcount
The package provides commands that display the value of a LaTeX
counter in a variety of formats (ordinal, text, hexadecimal,
decimal, octal, binary etc). The package offers some
multilingual support; configurations for use in English (both
British and American usage), French (including Belgian and
Swiss variants), German, Italian, Portuguese and Spanish
documents are provided. This package was originally provided as
part of the author's datetime package, but is now distributed
separately.

%package -n texlive-fmtcount-doc
Summary:        Documentation for fmtcount
Version:        svn46159
Provides:       tex-fmtcount-doc
AutoReqProv:    No

%description -n texlive-fmtcount-doc
Documentation for fmtcount

%package -n texlive-fn2end
Provides:       tex-fn2end = %{tl_version}
License:        Public Domain
Summary:        Convert footnotes to endnotes
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fn2end.sty) = %{tl_version}

%description -n texlive-fn2end
Defines macros \makeendnotes, which converts \footnote to
produce endnotes; and \theendnotes which prints them out.

%package -n texlive-fn2end-doc
Summary:        Documentation for fn2end
Version:        svn15878.1.1

Provides:       tex-fn2end-doc
AutoReqProv:    No

%description -n texlive-fn2end-doc
Documentation for fn2end

%package -n texlive-fnbreak
Provides:       tex-fnbreak = %{tl_version}
License:        LPPL
Summary:        Warn for split footnotes
Version:        svn25003.1.30

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(fnbreak.sty) = %{tl_version}

%description -n texlive-fnbreak
This package detects footnotes that are split over several
pages, and writes a warning to the log file.

%package -n texlive-fnbreak-doc
Summary:        Documentation for fnbreak
Version:        svn25003.1.30

Provides:       tex-fnbreak-doc
AutoReqProv:    No

%description -n texlive-fnbreak-doc
Documentation for fnbreak

%package -n texlive-fncychap
Provides:       tex-fncychap = %{tl_version}
License:        LPPL 1.3
Summary:        Seven predefined chapter heading styles
Version:        svn20710.v1.34

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(fncychap.sty) = %{tl_version}

%description -n texlive-fncychap
Each style can be modified using a set of simple commands.
Optionally one can modify the formatting routines in order to
create additional chapter headings. This package was previously
known as FancyChapter.

%package -n texlive-fncychap-doc
Summary:        Documentation for fncychap
Version:        svn20710.v1.34

Provides:       tex-fncychap-doc
AutoReqProv:    No

%description -n texlive-fncychap-doc
Documentation for fncychap

%package -n texlive-fncylab
Provides:       tex-fncylab = %{tl_version}
License:        LPPL
Summary:        Alter the format of \label references
Version:        svn17382.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fncylab.sty) = %{tl_version}

%description -n texlive-fncylab
LaTeX provides a mechanism for altering the appearance of
references to labels, but it's somewhat flawed, and requires
that the user manipulate internal commands. The package solves
the problem, by providing a \labelformat command for changing
the format of references to labels. The package also provides a
\Ref command to make reference to such redefined labels at the
start of a sentence.

%package -n texlive-fncylab-doc
Summary:        Documentation for fncylab
Version:        svn17382.1.0

Provides:       tex-fncylab-doc
AutoReqProv:    No

%description -n texlive-fncylab-doc
Documentation for fncylab

%package -n texlive-fnpara
Provides:       tex-fnpara = %{tl_version}
License:        LPPL 1.3
Summary:        Footnotes in paragraphs
Version:        svn25607.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fnpara.sty) = %{tl_version}

%description -n texlive-fnpara
Typeset footnotes in run-on paragraphs, instead of one above
another; this is a re-seating, for the LaTeX environment, of an
example in the TeXbook. The same basic code, improved for use
in e-TeX-based LaTeX, appears in the comprehensive footnote
package footmisc, and superior versions are also available in
the manyfoot and bigfoot packages.

%package -n texlive-fnpara-doc
Summary:        Documentation for fnpara
Version:        svn25607.0

Provides:       tex-fnpara-doc
AutoReqProv:    No

%description -n texlive-fnpara-doc
Documentation for fnpara

%package -n texlive-fnpct
Provides:       tex-fnpct = %{tl_version}
License:        LPPL 1.3
Summary:        Manage footnote marks' interaction with punctuation
Version:        svn40535

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xparse.sty), tex(l3keys2e.sty), tex(scrlfile.sty), tex(scrextend.sty)
Requires:       tex(translations.sty)
Provides:       tex(fnpct.sty) = %{tl_version}

%description -n texlive-fnpct
The package moves footnote marks after following punctuation
(comma or full stop), and adjusts kerning as appropriate. As a
side effect, a change to the handling of multiple footnotes is
provided.

%package -n texlive-fnpct-doc
Summary:        Documentation for fnpct
Version:        svn40535

Provides:       tex-fnpct-doc
AutoReqProv:    No

%description -n texlive-fnpct-doc
Documentation for fnpct

%package -n texlive-fnumprint
Provides:       tex-fnumprint = %{tl_version}
License:        LPPL 1.3
Summary:        Print a number in 'appropriate' format
Version:        svn29173.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xifthen.sty), tex(numprint.sty), tex(zahl2string.sty)
Provides:       tex(fnumprint.sty) = %{tl_version}

%description -n texlive-fnumprint
The package defines two macros which decide to typeset a number
either as an Arabic number or as a word (or words) for the
number. If the number is between zero and twelve (including
zero and twelve) then words will be used; if the number is
outside that range, it will be typeset using the package
numprint Words for English representation of numbers are
generated within the package, while those for German are
generated using the package zahl2string.

%package -n texlive-fnumprint-doc
Summary:        Documentation for fnumprint
Version:        svn29173.1.1a

Provides:       tex-fnumprint-doc
AutoReqProv:    No

%description -n texlive-fnumprint-doc
Documentation for fnumprint

%package -n texlive-foilhtml
Provides:       tex-foilhtml = %{tl_version}
License:        LPPL
Summary:        Interface between foiltex and LaTeX2HTML
Version:        svn21855.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(foilhtml.cfg) = %{tl_version}, tex(foilhtml.sty) = %{tl_version}

%description -n texlive-foilhtml
Provides integration between FoilTeX and LaTeX2HTML, adding
sectioning commands and elements of logical formatting to
FoilTeX and providing support for FoilTeX commands in
LaTeX2HTML.

%package -n texlive-foilhtml-doc
Summary:        Documentation for foilhtml
Version:        svn21855.1.2

Provides:       tex-foilhtml-doc
AutoReqProv:    No

%description -n texlive-foilhtml-doc
Documentation for foilhtml

%package -n texlive-fontaxes
Provides:       tex-fontaxes = %{tl_version}
License:        LPPL 1.3
Summary:        Additional font axes for LaTeX
Version:        svn33276.1.0d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fontaxes.sty) = %{tl_version}

%description -n texlive-fontaxes
The package adds several new font axes on top of LaTeX's New
Font Selection Scheme. In particular, it splits the shape axis
into a primary and a secondary shape axis, and it adds three
new axes to deal with the different figure versions offered by
many professional fonts.

%package -n texlive-fontaxes-doc
Summary:        Documentation for fontaxes
Version:        svn33276.1.0d

Provides:       tex-fontaxes-doc
AutoReqProv:    No

%description -n texlive-fontaxes-doc
Documentation for fontaxes

%package -n texlive-fonttable
Provides:       tex-fonttable = %{tl_version}
License:        LPPL 1.3
Summary:        Print font tables from a LaTeX document
Version:        svn44799
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(fonttable.sty) = %{tl_version}

%description -n texlive-fonttable
This is a package version of nfssfont.tex (part of the LaTeX
distribution); it enables you to print a table of the
characters of a font and/or some text (for demonstration or
testing purposes), from within a document. (Packages such as
testfont and nfssfont.tex provide these facilities, but they
run as interactive programs: the user is expected to type
details of what is needed.) Note that the package mftinc also
has a \fonttable function; the documentation explains how avoid
a clash with that package.

%package -n texlive-fonttable-doc
Summary:        Documentation for fonttable
Version:        svn44799
Provides:       tex-fonttable-doc
AutoReqProv:    No

%description -n texlive-fonttable-doc
Documentation for fonttable

%package -n texlive-footmisc
Provides:       tex-footmisc = %{tl_version}
License:        LPPL 1.3
Summary:        A range of footnote options
Version:        svn23330.5.5b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(footmisc.sty) = %{tl_version}

%description -n texlive-footmisc
A collection of ways to change the typesetting of footnotes.
The package provides means of changing the layout of the
footnotes themselves (including setting them in 'paragraphs' --
the para option), a way to number footnotes per page (the
perpage option), to make footnotes disappear in a 'moving'
argument (stable option) and to deal with multiple references
to footnotes from the same place (multiple option). The package
also has a range of techniques for labelling footnotes with
symbols rather than numbers. Some of the functions of the
package are overlap with the functionality of other packages.
The para option is also provided by the manyfoot and bigfoot
packages, though those are both also portmanteau packages.
(Don't be seduced by fnpara, whose implementation is improved
by the present package.) The perpage option is also offered by
footnpag and by the rather more general-purpose perpage

%package -n texlive-footmisc-doc
Summary:        Documentation for footmisc
Version:        svn23330.5.5b

Provides:       tex-footmisc-doc
AutoReqProv:    No

%description -n texlive-footmisc-doc
Documentation for footmisc

%package -n texlive-footnotebackref
Provides:       tex-footnotebackref = %{tl_version}
License:        LPPL 1.3
Summary:        Back-references from footnotes
Version:        svn27034.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(letltxmacro.sty), tex(hyperref.sty), tex(kvoptions.sty)
Provides:       tex(footnotebackref.sty) = %{tl_version}

%description -n texlive-footnotebackref
The package provides the means of creating hyperlinks, from a
footnote at the bottom of the page, back to the occurence of
the footnote in the main text.

%package -n texlive-footnotebackref-doc
Summary:        Documentation for footnotebackref
Version:        svn27034.1.0

Provides:       tex-footnotebackref-doc
AutoReqProv:    No

%description -n texlive-footnotebackref-doc
Documentation for footnotebackref

%package -n texlive-footnoterange
Provides:       tex-footnoterange = %{tl_version}
License:        LPPL 1.3
Summary:        References to ranges of footnotes
Version:        svn25430.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ltxcmds.sty), tex(xspace.sty)
Provides:       tex(footnoterange.sty) = %{tl_version}

%description -n texlive-footnoterange
The package provides environments footnoterange and
footnoterange*. Multiple footnotes inside these environments
are not referenced as (e.g.) "1 2 3 4" but as "1-4", i.e., the
range (from first to last referred footnote at that place) is
given. If hyperref package and use of its hyperfootnotes-option
the references are hyperlinked. (References to footnotes in the
footnoterange* environment are never hyperlinked.)

%package -n texlive-footnoterange-doc
Summary:        Documentation for footnoterange
Version:        svn25430.1.0a

Provides:       tex-footnoterange-doc
AutoReqProv:    No

%description -n texlive-footnoterange-doc
Documentation for footnoterange

%package -n texlive-footnpag
Provides:       tex-footnpag = %{tl_version}
License:        GPL+
Summary:        Per-page numbering of footnotes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(footnpag.sty) = %{tl_version}

%description -n texlive-footnpag
Allows footnotes on individual pages to be numbered from 1,
rather than being numbered sequentially through the document.

%package -n texlive-footnpag-doc
Summary:        Documentation for footnpag
Version:        svn15878.0

Provides:       tex-footnpag-doc
AutoReqProv:    No

%description -n texlive-footnpag-doc
Documentation for footnpag

%package -n texlive-forarray
Provides:       tex-forarray = %{tl_version}
License:        LPPL
Summary:        Using array structures in LaTeX
Version:        svn15878.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(forarray.sty) = %{tl_version}

%description -n texlive-forarray
The package provides functionality for processing lists and
array structures in LaTeX. Arrays can contain characters as
well as TeX and LaTeX commands, nesting of arrays is possible,
and arrays are processed within the same brace level as their
surrounding environment. Array levels can be delimited by
characters or control sequences defined by the user. Practical
uses of this package include data management, construction of
lists and tables, and calculations based on the contents of
lists and arrays.

%package -n texlive-forarray-doc
Summary:        Documentation for forarray
Version:        svn15878.1.01

Provides:       tex-forarray-doc
AutoReqProv:    No

%description -n texlive-forarray-doc
Documentation for forarray

%package -n texlive-foreign
Provides:       tex-foreign = %{tl_version}
License:        LPPL 1.3
Summary:        Systematic treatment of 'foreign' words in documents
Version:        svn27819.2.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xpunctuate.sty), tex(xspace.sty)
Provides:       tex(foreign.sty) = %{tl_version}

%description -n texlive-foreign
The package supports authors' use of consistent typesetting of
foreign words in documents.

%package -n texlive-foreign-doc
Summary:        Documentation for foreign
Version:        svn27819.2.7

Provides:       tex-foreign-doc
AutoReqProv:    No

%description -n texlive-foreign-doc
Documentation for foreign

%package -n texlive-forloop
Provides:       tex-forloop = %{tl_version}
License:        LGPLv2+
Summary:        Iteration in LaTeX
Version:        svn15878.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(forloop.sty) = %{tl_version}

%description -n texlive-forloop
The package provides a command \forloop for doing iteration in
LaTeX macro programming.

%package -n texlive-forloop-doc
Summary:        Documentation for forloop
Version:        svn15878.3.0

Provides:       tex-forloop-doc
AutoReqProv:    No

%description -n texlive-forloop-doc
Documentation for forloop

%package -n texlive-formlett
Provides:       tex-formlett = %{tl_version}
License:        GPL+
Summary:        Letters to multiple recipients
Version:        svn21480.2.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(formlett.sty) = %{tl_version}

%description -n texlive-formlett
A package for multiple letters from the same basic source; the
package offers parametrisation of the letters actually sent.

%package -n texlive-formlett-doc
Summary:        Documentation for formlett
Version:        svn21480.2.3

Provides:       tex-formlett-doc
AutoReqProv:    No

%description -n texlive-formlett-doc
Documentation for formlett

%package -n texlive-formular
Provides:       tex-formular = %{tl_version}
License:        LPPL
Summary:        Create forms containing field for manual entry
Version:        svn15878.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(formular.sty) = %{tl_version}

%description -n texlive-formular
When typesetting forms there often arises the need for defining
fields which consist of one or more lines where the customer
can write something down manually. This package offers some
commands for defining such fields in a distinctive way.

%package -n texlive-formular-doc
Summary:        Documentation for formular
Version:        svn15878.1.0a

Provides:       tex-formular-doc
AutoReqProv:    No

%description -n texlive-formular-doc
Documentation for formular

%package -n texlive-fragments
Provides:       tex-fragments = %{tl_version}
License:        Public Domain
Summary:        Fragments of LaTeX code
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(checklab.tex) = %{tl_version}, tex(overrightarrow.sty) = %{tl_version}
Provides:       tex(removefr.tex) = %{tl_version}, tex(subscript.sty) = %{tl_version}

%description -n texlive-fragments
A collection of fragments of LaTeX code, suitable for inclusion
in packages, or (possibly) in users' documents. Included are:
checklab, for modifying the label checking code at
\end{document}; overrightarrow, defining a doubled over-arrow
macro; removefr, for removing 'reset' relations between
counters; and subscript, defining a \textsubscript command.

%package -n texlive-fragments-doc
Summary:        Documentation for fragments
Version:        svn15878.0

Provides:       tex-fragments-doc
AutoReqProv:    No

%description -n texlive-fragments-doc
Documentation for fragments

%package -n texlive-frame
Provides:       tex-frame = %{tl_version}
License:        LPPL
Summary:        Framed boxes for Plain TeX
Version:        svn18312.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(frame.sty) = %{tl_version}, tex(frame.tex) = %{tl_version}

%description -n texlive-frame
A jiffy file (taken from fancybox) for placing a frame around a
box of text. The macros also provide for typesetting an empty
box of given dimensions.

%package -n texlive-frame-doc
Summary:        Documentation for frame
Version:        svn18312.1.0

Provides:       tex-frame-doc
AutoReqProv:    No

%description -n texlive-frame-doc
Documentation for frame

%package -n texlive-framed
Provides:       tex-framed = %{tl_version}
License:        Copyright only
Summary:        Framed or shaded regions that can break across pages
Version:        svn26789.0.96

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(framed.sty) = %{tl_version}

%description -n texlive-framed
The package creates three environments: framed, which puts an
ordinary frame box around the region, shaded, which shades the
region, and leftbar, which places a line at the left side. The
environments allow a break at their start (the \FrameCommand
enables creation of a title that is "attached" to the
environment); breaks are also allowed in the course of the
framed/shaded matter. There is also a command \MakeFramed to
make your own framed-style environments.

%package -n texlive-framed-doc
Summary:        Documentation for framed
Version:        svn26789.0.96

Provides:       tex-framed-doc
AutoReqProv:    No

%description -n texlive-framed-doc
Documentation for framed

%package -n texlive-frankenstein
Provides:       tex-frankenstein = %{tl_version}
License:        Public Domain
Summary:        A collection of LaTeX packages
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(slemph.sty)
Provides:       tex(abbrevs.cfg) = %{tl_version}, tex(abbrevs.sty) = %{tl_version}
Provides:       tex(achicago.sty) = %{tl_version}, tex(attrib.sty) = %{tl_version}
Provides:       tex(blkcntrl.sty) = %{tl_version}, tex(compsci.cfg) = %{tl_version}
Provides:       tex(compsci.sty) = %{tl_version}, tex(dialogue.sty) = %{tl_version}
Provides:       tex(lips.sty) = %{tl_version}, tex(moredefs.sty) = %{tl_version}
Provides:       tex(newclude.sty) = %{tl_version}, tex(slemph.cfg) = %{tl_version}
Provides:       tex(slemph.sty) = %{tl_version}, tex(titles.cfg) = %{tl_version}
Provides:       tex(titles.sty) = %{tl_version}

%description -n texlive-frankenstein
Frankenstein is a bundle of LaTeX packages serving various
purposes and a BibTeX bibliography style. Descriptions are
given under the individual packages: abbrevs, achicago package,
achicago bibstyle, attrib, blkcntrl, compsci, dialogue, lips,
moredefs, newclude, slemph, titles.

%package -n texlive-frankenstein-doc
Summary:        Documentation for frankenstein
Version:        svn15878.0

Provides:       tex-frankenstein-doc
AutoReqProv:    No

%description -n texlive-frankenstein-doc
Documentation for frankenstein

%package -n texlive-frege
Provides:       tex-frege = %{tl_version}
License:        GPL+
Summary:        Typeset fregean Begriffsschrift
Version:        svn27417.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty), tex(ifthen.sty), tex(bguq.sty)
Provides:       tex(frege.sty) = %{tl_version}

%description -n texlive-frege
The package defines a number of new commands for typesetting
fregean Begriffsschrift in LaTeX. It is loosely based on the
package begriff, and offers a number of improvements including
better relative lengths of the content stroke with respect to
other strokes, content strokes that point at the middle of
lines rather than the bottom, a greater width for the assertion
stroke as compared to the content stroke, a more intuitive
structure for the conditional, greater care taken to allow for
the linewidth in the spacing of formulas.

%package -n texlive-frege-doc
Summary:        Documentation for frege
Version:        svn27417.1.3

Provides:       tex-frege-doc
AutoReqProv:    No

%description -n texlive-frege-doc
Documentation for frege

%package -n texlive-ftcap
Provides:       tex-ftcap = %{tl_version}
License:        GPL+
Summary:        Allows \caption at the beginning of a table-environment
Version:        svn17275.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ftcap.sty) = %{tl_version}

%description -n texlive-ftcap
For several reasons a \caption may be desirable at the top of a
table environment. This package changes the table environment
such that \abovecaptionskip and \belowcaptionskip are swapped.
The package should also work with a non-standard table
environment.

%package -n texlive-ftcap-doc
Summary:        Documentation for ftcap
Version:        svn17275.1.4

Provides:       tex-ftcap-doc
AutoReqProv:    No

%description -n texlive-ftcap-doc
Documentation for ftcap

%package -n texlive-ftnxtra
Provides:       tex-ftnxtra = %{tl_version}
License:        LPPL
Summary:        Extend the applicability of the \footnote command
Version:        svn29652.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ftnxtra.sty) = %{tl_version}

%description -n texlive-ftnxtra
The package treats footnotes in \caption, the tabular
environment, and \chapter and other \section-like commands.

%package -n texlive-ftnxtra-doc
Summary:        Documentation for ftnxtra
Version:        svn29652.0.1

Provides:       tex-ftnxtra-doc
AutoReqProv:    No

%description -n texlive-ftnxtra-doc
Documentation for ftnxtra

%package -n texlive-fullblck
Provides:       tex-fullblck = %{tl_version}
License:        LPPL
Summary:        Left-blocking for letter class
Version:        svn25434.1.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fullblck.sty) = %{tl_version}

%description -n texlive-fullblck
Used with the letter documentclass to set the letter in a
fullblock style (everything at the left margin).

%package -n texlive-fullblck-doc
Summary:        Documentation for fullblck
Version:        svn25434.1.03

Provides:       tex-fullblck-doc
AutoReqProv:    No

%description -n texlive-fullblck-doc
Documentation for fullblck

%package -n texlive-fullminipage
Provides:       tex-fullminipage = %{tl_version}
License:        GPLv3+
Summary:        Minipage spanning a complete page
Version:        svn34545.0.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(color.sty)
Provides:       tex(fullminipage.sty) = %{tl_version}

%description -n texlive-fullminipage
This package provides the environment fullminipage, which
generates a minipage spanning a new, complete page with page
style empty. The environment provides options to set margins
around the minipage and configure the background.

%package -n texlive-fullminipage-doc
Summary:        Documentation for fullminipage
Version:        svn34545.0.1.1

Provides:       tex-fullminipage-doc
AutoReqProv:    No

%description -n texlive-fullminipage-doc
Documentation for fullminipage

%package -n texlive-fullwidth
Provides:       tex-fullwidth = %{tl_version}
License:        LPPL
Summary:        Adjust margins of text block
Version:        svn24684.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(etoolbox.sty), tex(zref-abspage.sty)
Provides:       tex(fullwidth.sty) = %{tl_version}

%description -n texlive-fullwidth
The package provides the environment fullwidth, which sets the
left and right margins in a simple way. There is no constraint
about page breaks; if you are using the twoside mode, you can
set the inner and outer margins to avoid the effects of the
different margins.

%package -n texlive-fullwidth-doc
Summary:        Documentation for fullwidth
Version:        svn24684.0.1

Provides:       tex-fullwidth-doc
AutoReqProv:    No

%description -n texlive-fullwidth-doc
Documentation for fullwidth

%package -n texlive-fundus-calligra
Provides:       tex-fundus-calligra = %{tl_version}
License:        LPPL
Summary:        Support for the calligra font in LaTeX documents
Version:        svn26018.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(calligra.sty) = %{tl_version}

%description -n texlive-fundus-calligra
The package offers support for the calligra handwriting font,
in LaTeX documents. The package is part of the fundus bundle.

%package -n texlive-fundus-calligra-doc
Summary:        Documentation for fundus-calligra
Version:        svn26018.1.2

Provides:       tex-fundus-calligra-doc
AutoReqProv:    No

%description -n texlive-fundus-calligra-doc
Documentation for fundus-calligra

%package -n texlive-fundus-cyr
Provides:       tex-fundus-cyr = %{tl_version}
License:        LPPL 1.3
Summary:        Support for Washington University Cyrillic fonts
Version:        svn26019.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(cyracc.def)
Provides:       tex(cyr.sty) = %{tl_version}

%description -n texlive-fundus-cyr
The package supports the use of the Washington Cyrillic fonts
with LaTeX (Note that standard LateX has support, too, as
encoding OT2). The package is distributed as part of the fundus
bundle.

%package -n texlive-fundus-sueterlin
Provides:       tex-fundus-sueterlin = %{tl_version}
License:        LPPL 1.3
Summary:        Sutterlin
Version:        svn26030.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(suetterl.sty) = %{tl_version}

%description -n texlive-fundus-sueterlin
The package supports use, in LaTeX, of the MetaFont emulation
of the Sueterlin handwriting fonts The package is distributed
as part of the fundus bundle..

%package -n texlive-fundus-sueterlin-doc
Summary:        Documentation for fundus-sueterlin
Version:        svn26030.1.2

Provides:       tex-fundus-sueterlin-doc
AutoReqProv:    No

%description -n texlive-fundus-sueterlin-doc
Documentation for fundus-sueterlin

%package -n texlive-fwlw
Provides:       tex-fwlw = %{tl_version}
License:        Copyright only
Summary:        Get first and last words of a page
Version:        svn29803.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fwlw.sty) = %{tl_version}

%description -n texlive-fwlw
The package extracts the first and last words of a page,
together with the first word of the next page, just before the
page is formed into the object to print. The package defines a
couple of page styles that use the words that have been
extracted.

%package -n texlive-fwlw-doc
Summary:        Documentation for fwlw
Version:        svn29803.0

Provides:       tex-fwlw-doc
AutoReqProv:    No

%description -n texlive-fwlw-doc
Documentation for fwlw

%package -n texlive-faktor
Provides:       tex-faktor = %{tl_version}
License:        LPPL
Summary:        Typeset quotient structures with LaTeX
Version:        svn15878.0.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(faktor.sty) = %{tl_version}

%description -n texlive-faktor
The package provides the means to typeset factor structures, as
are used in many areas of algebraic notation. The structure is
similar to the 'A/B' that is provided by the nicefrac package
(part of the units distribution), and by the xfrac package; the
most obvious difference is that the numerator and denominator's
sizes do not change in the \faktor command.

%package -n texlive-faktor-doc
Summary:        Documentation for faktor
Version:        svn15878.0.1b

Provides:       tex-faktor-doc
AutoReqProv:    No

%description -n texlive-faktor-doc
Documentation for faktor

%package -n texlive-featpost
Provides:       tex-featpost = %{tl_version}
License:        GPL+
Summary:        MetaPost macros for 3D
Version:        svn35346.0.8.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-featpost
These macros allow the production of three-dimensional schemes
containing: angles, circles, cylinders, cones and spheres,
among other things.

%package -n texlive-featpost-doc
Summary:        Documentation for featpost
Version:        svn35346.0.8.8

Provides:       tex-featpost-doc
AutoReqProv:    No

%description -n texlive-featpost-doc
Documentation for featpost

%package -n texlive-feynmf
Provides:       tex-feynmf = %{tl_version}
License:        GPL+
Summary:        Macros and fonts for creating Feynman (and other) diagrams
Version:        svn17259.1.08

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(feynmf.sty) = %{tl_version}, tex(feynmp.sty) = %{tl_version}

%description -n texlive-feynmf
The feynmf package provides an interface to Metafont (inspired
by the facilities of mfpic) to use simple structure
specifications to produce relatively complex diagrams. (The
feynmp package, also part of this bundle, uses MetaPost in the
same way.) While the package was designed for Feynman diagrams,
it could in principle be used for diagrams in graph and similar
theories, where the structure is semi-algorithmically
determined.

%package -n texlive-feynmf-doc
Summary:        Documentation for feynmf
Version:        svn17259.1.08

Provides:       tex-feynmf-doc
AutoReqProv:    No

%description -n texlive-feynmf-doc
Documentation for feynmf

%package -n texlive-feynmp-auto
Provides:       tex-feynmp-auto = %{tl_version}
License:        LPPL 1.3
Summary:        Automatic processing of feynmp graphics
Version:        svn30223.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(feynmp.sty), tex(ifpdf.sty), tex(ifxetex.sty), tex(pdftexcmds.sty)
Provides:       tex(feynmp-auto.sty) = %{tl_version}

%description -n texlive-feynmp-auto
The package takes care of running Metapost on the output files
produced by the feynmp package, so that the compiled pictures
will be available in the next run of LaTeX. The package honours
options that apply to feynmp.

%package -n texlive-feynmp-auto-doc
Summary:        Documentation for feynmp-auto
Version:        svn30223.1.1

Provides:       tex-feynmp-auto-doc
AutoReqProv:    No

%description -n texlive-feynmp-auto-doc
Documentation for feynmp-auto

%package -n texlive-figbas
Provides:       tex-figbas = %{tl_version}
License:        LPPL
Summary:        Mini-fonts for figured-bass notation in music
Version:        svn28943.1.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(figbas.map) = %{tl_version}, tex(cmrj.tfm) = %{tl_version}
Provides:       tex(cmssj.tfm) = %{tl_version}, tex(plrj.tfm) = %{tl_version}
Provides:       tex(cmrj.pfb) = %{tl_version}, tex(cmssj.pfb) = %{tl_version}
Provides:       tex(plrj.pfb) = %{tl_version}

%description -n texlive-figbas
This package consists of three mini-fonts (and associated
metrics) of conventional ligatures for the figured-bass
notations 2+, 4+, 5+, 6+ and 9+ in music manuscripts. The fonts
are usable with Computer Modern Roman and Sans, and
Palatino/Palladio, respectively.

%package -n texlive-figbas-doc
Summary:        Documentation for figbas
Version:        svn28943.1.0.3

Provides:       tex-figbas-doc
AutoReqProv:    No

%description -n texlive-figbas-doc
Documentation for figbas

%package -n texlive-figflow
Provides:       tex-figflow = %{tl_version}
License:        Copyright only
Summary:        Flow text around a figure
Version:        svn21462.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(figflow.tex) = %{tl_version}

%description -n texlive-figflow
Provides a Plain TeX macro \figflow that allows one to insert a
figure into an area inset into a paragraph. Command arguments
are width and height of the figure, and the figure (and its
caption) itself. Usage details are to be found in the TeX file
itself. The package does not work with LaTeX; packages such as
wrapfig, floatflt and picins support the needs of LaTeX users
in this area.

%package -n texlive-figflow-doc
Summary:        Documentation for figflow
Version:        svn21462.0

Provides:       tex-figflow-doc
AutoReqProv:    No

%description -n texlive-figflow-doc
Documentation for figflow

%package -n texlive-fixpdfmag
Provides:       tex-fixpdfmag = %{tl_version}
License:        Public Domain
Summary:        Fix magnification in PDFTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fixpdfmag.tex) = %{tl_version}

%description -n texlive-fixpdfmag
A recent change to PDFTeX has caused magnification to apply to
page dimensions. This small package changes the values set in
the page dimension variables from pt to truept, thus evading
the effects of \mag.

%package -n texlive-font-change
Provides:       tex-font-change = %{tl_version}
License:        CC-BY-SA
Summary:        Macros to change text and mathematics fonts in plain TeX
Version:        svn40403

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(font-change.tex) = %{tl_version}, tex(font-change_FRENCH.tex) = %{tl_version}
Provides:       tex(font_antp_euler.tex) = %{tl_version}
Provides:       tex(font_antt-condensed-light.tex) = %{tl_version}
Provides:       tex(font_antt-condensed-medium.tex) = %{tl_version}
Provides:       tex(font_antt-condensed.tex) = %{tl_version}
Provides:       tex(font_antt-light.tex) = %{tl_version}
Provides:       tex(font_antt-medium.tex) = %{tl_version}
Provides:       tex(font_antt.tex) = %{tl_version}, tex(font_arev.tex) = %{tl_version}
Provides:       tex(font_artemisia_euler.tex) = %{tl_version}
Provides:       tex(font_bera_concrete.tex) = %{tl_version}
Provides:       tex(font_bera_euler.tex) = %{tl_version}
Provides:       tex(font_bera_fnc.tex) = %{tl_version}, tex(font_bookman.tex) = %{tl_version}
Provides:       tex(font_century.tex) = %{tl_version}, tex(font_charter.tex) = %{tl_version}
Provides:       tex(font_cm.tex) = %{tl_version}, tex(font_cmbright.tex) = %{tl_version}
Provides:       tex(font_concrete.tex) = %{tl_version}, tex(font_epigrafica_euler.tex) = %{tl_version}
Provides:       tex(font_epigrafica_palatino.tex) = %{tl_version}
Provides:       tex(font_iwona-bold.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed-bold.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed-light.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed-medium.tex) = %{tl_version}
Provides:       tex(font_iwona-condensed.tex) = %{tl_version}
Provides:       tex(font_iwona-light.tex) = %{tl_version}
Provides:       tex(font_iwona-medium.tex) = %{tl_version}
Provides:       tex(font_iwona.tex) = %{tl_version}, tex(font_kp-light.tex) = %{tl_version}
Provides:       tex(font_kp.tex) = %{tl_version}, tex(font_kurier-bold.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed-bold.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed-light.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed-medium.tex) = %{tl_version}
Provides:       tex(font_kurier-condensed.tex) = %{tl_version}
Provides:       tex(font_kurier-light.tex) = %{tl_version}
Provides:       tex(font_kurier-medium.tex) = %{tl_version}
Provides:       tex(font_kurier.tex) = %{tl_version}, tex(font_libertine_kp.tex) = %{tl_version}
Provides:       tex(font_libertine_palatino.tex) = %{tl_version}
Provides:       tex(font_libertine_times.tex) = %{tl_version}
Provides:       tex(font_mdutopia.tex) = %{tl_version}, tex(font_pagella.tex) = %{tl_version}
Provides:       tex(font_palatino.tex) = %{tl_version}, tex(font_times.tex) = %{tl_version}
Provides:       tex(font_utopia.tex) = %{tl_version}

%description -n texlive-font-change
Macros to Change Text and Mathematics fonts in TeX: 45
Beautiful Variants The macros are written for plain TeX and may
be used with other packages like AmSTeX, eplain, etc. They also
work with XeTeX. The macros allow users to change the fonts
(for both text and mathematics) in their TeX document with only
one statement. The fonts may be used readily at various
predefined sizes. All the fonts called by these macro files are
free and are included in current MiKTeX and TeX Live
distributions.

%package -n texlive-font-change-doc
Summary:        Documentation for font-change
Version:        svn40403

Provides:       tex-font-change-doc
AutoReqProv:    No

%description -n texlive-font-change-doc
Documentation for font-change

%package -n texlive-fontch
Provides:       tex-fontch = %{tl_version}
License:        LPPL
Summary:        Changing fonts, sizes and encodings in Plain TeX
Version:        svn17859.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(DSmac.tex) = %{tl_version}, tex(TS1mac.tex) = %{tl_version}
Provides:       tex(bsymbols.tex) = %{tl_version}, tex(fontch.tex) = %{tl_version}
Provides:       tex(fontch_doc.tex) = %{tl_version}

%description -n texlive-fontch
The fontch macros allow the user to change font size and family
anywhere in a plain TeX document. Sizes of 8, 10, 12, 14, 20
and 24 points are available. A sans serif family (\sf) is
defined in addition to the families already defined in plain
TeX. Optional support for Latin Modern T1 and TS1 fonts is
given. There are macros for non-latin1 letters and for most TS1
symbols. Math mode always uses CM fonts. A command for
producing doubled-spaced documents is also provided. The
present version of the package is designed to deal with the
latest release of the Latin Modern fonts version 1.106.
Unfortunately, it can no longer support earlier versions of the
fonts, so an obsolete version of the package is retained for
users who don't yet have access to the latest version of the
fonts.

%package -n texlive-fontch-doc
Summary:        Documentation for fontch
Version:        svn17859.2.2

Provides:       tex-fontch-doc
AutoReqProv:    No

%description -n texlive-fontch-doc
Documentation for fontch

%package -n texlive-fbithesis
Provides:       tex-fbithesis = %{tl_version}
License:        LPPL
Summary:        Computer Science thesis class for University of Dortmund
Version:        svn21340.1.2m

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty)
Provides:       tex(fbithesis.cfg) = %{tl_version}, tex(fbithesis.cls) = %{tl_version}

%description -n texlive-fbithesis
At the department of computer science at the University of
Dortmund there are cardboard cover pages for research or
internal reports like master/phd-theses. The main function of
this LaTeX2e document-class is a replacement for the \maketitle
command to typeset a title page that is adjusted to these cover
pages.

%package -n texlive-fbithesis-doc
Summary:        Documentation for fbithesis
Version:        svn21340.1.2m

Provides:       tex-fbithesis-doc
AutoReqProv:    No

%description -n texlive-fbithesis-doc
Documentation for fbithesis

%package -n texlive-fcavtex
Provides:       tex-fcavtex = %{tl_version}
License:        LPPL 1.3
Summary:        A thesis class for the FCAV/UNESP (Brazil)
Version:        svn38074.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(babel.sty), tex(inputenc.sty), tex(helvet.sty)
Requires:       tex(layout.sty), tex(textpos.sty), tex(ragged2e.sty), tex(microtype.sty)
Requires:       tex(titlesec.sty), tex(tocloft.sty), tex(memhfixc.sty), tex(indentfirst.sty)
Requires:       tex(hyperref.sty), tex(chapterbib.sty), tex(abntex2cite.sty), tex(hyphenat.sty)
Requires:       tex(paralist.sty), tex(mfirstuc.sty), tex(pageslts.sty)
Provides:       tex(fcavtex.cls) = %{tl_version}

%description -n texlive-fcavtex
This package provides a class and a bibliography style for the
FCAV-UNESP (Faculdade de Ciencias Agrarias e Veterinarias de
Jaboticabal UNESP) brazilian university, written based on the
institution rules for thesis publications.

%package -n texlive-fcavtex-doc
Summary:        Documentation for fcavtex
Version:        svn38074.1.1

Provides:       tex-fcavtex-doc
AutoReqProv:    No

%description -n texlive-fcavtex-doc
Documentation for fcavtex

%package -n texlive-fcltxdoc
Provides:       tex-fcltxdoc = %{tl_version}
License:        LPPL 1.3
Summary:        Macros for use in the author's documentation
Version:        svn24500.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(filehook.sty), tex(ltxnew.sty), tex(etexcmds.sty)
Requires:       tex(ltxcmds.sty), tex(etoolbox.sty), tex(amsmath.sty), tex(amsfonts.sty)
Requires:       tex(amsopn.sty), tex(amssymb.sty), tex(xspace.sty), tex(fontenc.sty)
Requires:       tex(hologo.sty), tex(graphicx.sty), tex(grffile.sty), tex(needspace.sty)
Requires:       tex(moresize.sty), tex(manfnt.sty), tex(bbding.sty), tex(eurosym.sty)
Requires:       tex(fancyhdr.sty), tex(lastpage.sty), tex(marginnote.sty), tex(framed.sty)
Requires:       tex(ulem.sty), tex(nccfoots.sty), tex(nccstretch.sty), tex(linegoal.sty)
Requires:       tex(array.sty), tex(delarray.sty), tex(makecell.sty), tex(booktabs.sty)
Requires:       tex(embedfile.sty), tex(interfaces.sty), tex(relsize.sty), tex(titlesec.sty)
Requires:       tex(tocloft.sty), tex(hypdoc.sty), tex(hyperref.sty), tex(pdftexcmds.sty)
Requires:       tex(enumitem.sty), tex(bookmark.sty), tex(hypbmsec.sty), tex(fancyvrb.sty)
Requires:       tex(listings.sty), tex(xcolor.sty)
Provides:       tex(fcltxdoc.sty) = %{tl_version}

%description -n texlive-fcltxdoc
The package is not advertised for public use, but is necessary
for the support of others of the author's packages (which are
compiled under the ltxdoc class).

%package -n texlive-fcltxdoc-doc
Summary:        Documentation for fcltxdoc
Version:        svn24500.1.0

Provides:       tex-fcltxdoc-doc
AutoReqProv:    No

%description -n texlive-fcltxdoc-doc
Documentation for fcltxdoc

%package -n texlive-fei
Provides:       tex-fei = %{tl_version}
License:        LPPL 1.3
Summary:        Class for academic works at FEI University Center -- Brazil
Version:        svn46788
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(geometry.sty), tex(fancyhdr.sty), tex(babel.sty), tex(fontenc.sty)
Requires:       tex(setspace.sty), tex(caption.sty), tex(mathtools.sty), tex(lmodern.sty)
Requires:       tex(icomma.sty), tex(times.sty), tex(graphicx.sty), tex(morewrites.sty)
Requires:       tex(algorithm2e.sty), tex(amsthm.sty), tex(thmtools.sty), tex(enumitem.sty)
Requires:       tex(tocloft.sty), tex(pdfpages.sty), tex(ifthen.sty), tex(imakeidx.sty)
Requires:       tex(hyperref.sty), tex(glossaries.sty), tex(abntex2cite.sty)
Provides:       tex(fei.cls) = %{tl_version}

%description -n texlive-fei
fei is a class created by graduate students and LaTeX
enthusiasts that allows students from FEI University Center to
create their academic works, be it a monograph, masters
dissertation or phd thesis, under the typographic rules of the
institution. The class makes it possible to create a full
academic work, supporting functionalities such as cover, title
page, catalog entry, dedication, summary, lists of figures,
tables, algorithms, acronyms and symbols, multiple authors,
index, references, appendices and attachments. fei is loosely
based in the Brazilian National Standards Organization
(Associacao Brasileira de Normas Tecnicas, ABNT) standards for
the creation of academic works, such as ABNT NBR 10520:2002
(Citations) and ABNT NBR 6023:2002 (Bibliographic References).

%package -n texlive-fei-doc
Summary:        Documentation for fei
Version:        svn46788
Provides:       tex-fei-doc
AutoReqProv:    No

%description -n texlive-fei-doc
Documentation for fei

%package -n texlive-fouridx
Provides:       tex-fouridx = %{tl_version}
License:        LPPL
Summary:        Left sub- and superscripts in maths mode
Version:        svn32214.2.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fouridx.sty) = %{tl_version}

%description -n texlive-fouridx
The package enables left subscripts and superscripts in maths
mode. The sub- and superscripts are raised for optimum fitting
to the symbol indexed, in such a way that left and right sub-
and superscripts are set on the same level, as appropriate. The
package provides an alternative to the use of the \sideset
command in the amsmath package.

%package -n texlive-fouridx-doc
Summary:        Documentation for fouridx
Version:        svn32214.2.00

Provides:       tex-fouridx-doc
AutoReqProv:    No

%description -n texlive-fouridx-doc
Documentation for fouridx

%package -n texlive-functan
Provides:       tex-functan = %{tl_version}
License:        LPPL
Summary:        Macros for functional analysis and PDE theory
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty)
Provides:       tex(functan.sty) = %{tl_version}

%description -n texlive-functan
This package provides a convenient and coherent way to deal
with name of functional spaces (mainly Sobolev spaces) in
functional analysis and PDE theory. It also provides a set of
macros for dealing with norms, scalar products and convergence
with some object oriented flavor (it gives the possibility to
override the standard behavior of norms, ...).

%package -n texlive-functan-doc
Summary:        Documentation for functan
Version:        svn15878.0

Provides:       tex-functan-doc
AutoReqProv:    No

%description -n texlive-functan-doc
Documentation for functan

%package -n texlive-fixlatvian
Provides:       tex-fixlatvian = %{tl_version}
License:        LPPL 1.3
Summary:        Improve Latvian language support in XeLaTeX
Version:        svn21631.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(svn-prov.sty), tex(caption.sty), tex(etoolbox.sty), tex(perpage.sty)
Requires:       tex(polyglossia.sty), tex(xstring.sty), tex(indentfirst.sty), tex(icomma.sty)
Provides:       tex(fixlatvian.sty) = %{tl_version}

%description -n texlive-fixlatvian
The package offers improvement of the Latvian language support
in polyglossia, in particular in the area of the standard
classes.

%package -n texlive-fixlatvian-doc
Summary:        Documentation for fixlatvian
Version:        svn21631.1a

Provides:       tex-fixlatvian-doc
AutoReqProv:    No

%description -n texlive-fixlatvian-doc
Documentation for fixlatvian

%package -n texlive-fontbook
Provides:       tex-fontbook = %{tl_version}
License:        LPPL 1.3
Summary:        Generate a font book
Version:        svn23608.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontspec.sty), tex(xunicode.sty), tex(kvoptions.sty), tex(etoolbox.sty)
Provides:       tex(fontbook.sty) = %{tl_version}

%description -n texlive-fontbook
The package provides a means of producing a 'book' of font
samples (for evaluation, etc.).

%package -n texlive-fontbook-doc
Summary:        Documentation for fontbook
Version:        svn23608.0.2

Provides:       tex-fontbook-doc
AutoReqProv:    No

%description -n texlive-fontbook-doc
Documentation for fontbook

%package -n texlive-fontwrap
Provides:       tex-fontwrap = %{tl_version}
License:        GPL+
Summary:        Bind fonts to specific unicode blocks
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fontwrap.sty) = %{tl_version}

%description -n texlive-fontwrap
The package (which runs under XeLaTeX) lets you bind fonts to
specific unicode blocks, for automatic font tagging of
multilingual text. The package uses Perl (via perltex) to
construct its tables.

%package -n texlive-fontwrap-doc
Summary:        Documentation for fontwrap
Version:        svn15878.0

Provides:       tex-fontwrap-doc
AutoReqProv:    No

%description -n texlive-fontwrap-doc
Documentation for fontwrap

%package -n texlive-ffslides-doc
Provides:       tex-ffslides-doc = %{tl_version}
License:        LPPL
Summary:        doc files of ffslides
Version:        svn38895

AutoReqProv:    No

%description -n texlive-ffslides-doc
Documentation for ffslides

%package -n texlive-ffslides
Provides:       tex-ffslides = %{tl_version}
License:        LPPL
Summary:        Freeform slides based on the article class
Version:        svn38895

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ffslides.cls) = %{tl_version}

%description -n texlive-ffslides
The ffslides ("freeform slides") class is intended to make it
easier to place various types of content freely on the page,
and therefore easier to design documents with a strong visual
component: presentations, posters, research or lecture notes,
and so on. The goal of the class is to be less rigid and less
complex than some of the popular presentation-making options.
It is essentially a small set of macros added to the article
class. A well-organized template file is included, and the
documentation is itself an extensive example of the class's
capabilities.

%package -n texlive-fibeamer-doc
Provides:       tex-fibeamer-doc = %{tl_version}
License:        LPPL
Summary:        doc files of fibeamer
Version:        svn44239
AutoReqProv:    No

%description -n texlive-fibeamer-doc
Documentation for fibeamer

%package -n texlive-fibeamer
Provides:       tex-fibeamer = %{tl_version}
License:        LPPL
Summary:        Beamer theme for thesis defense presentations at Masaryk University (Brno, Czech Republic)
Version:        svn44239
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(beamerthemefibeamer.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-law.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-med.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-ped.sty) = %{tl_version}
Provides:       tex(beamerouterthemefibeamer-mu.sty) = %{tl_version}
Provides:       tex(beamerinnerthemefibeamer-mu.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-phil.sty) = %{tl_version}
Provides:       tex(beamerfontthemefibeamer-mu.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-sci.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-fss.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-fi.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-econ.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu.sty) = %{tl_version}
Provides:       tex(beamercolorthemefibeamer-mu-fsps.sty) = %{tl_version}

%description -n texlive-fibeamer
A beamer theme for the typesetting of thesis defense
presentations at the Masaryk University (Brno, Czech Republic).
The theme has been designed for easy extensibility by color
themes of other academic institutions.

%package -n texlive-fixcmex-doc
Provides:       tex-fixcmex-doc = %{tl_version}
License:        LPPL
Summary:        doc files of fixcmex
Version:        svn38816

AutoReqProv:    No

%description -n texlive-fixcmex-doc
Documentation for fixcmex

%package -n texlive-fixcmex
Provides:       tex-fixcmex = %{tl_version}
License:        LPPL
Summary:        Fully scalable version of Computer Modern Math Extension font
Version:        svn38816

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fixcmex.sty) = %{tl_version}

%description -n texlive-fixcmex
This package provides a fully scalable version of the Computer
Modern Math Extension font for curing sizing problems mainly
with lmodern. It can be used when the main font of the document
is Computer Modern (or European Modern, if T1 encoding is
selected), or Latin Modern. It redefines the math extension
font so that it becomes arbitrarily scalable, using the optical
size fonts provided by the AMS together with the original
cmex10 font.

%package -n texlive-font-change-xetex-doc
Provides:       tex-font-change-xetex-doc = %{tl_version}
License:        CC-BY-SA
Summary:        doc files of font-change-xetex
Version:        svn40404

AutoReqProv:    No

%description -n texlive-font-change-xetex-doc
Documentation for font-change-xetex

%package -n texlive-font-change-xetex
Provides:       tex-font-change-xetex = %{tl_version}
License:        CC-BY-SA
Summary:        Macros to change text and mathematics fonts in plain XeTeX
Version:        svn40404

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(font-change-xetex.tex) = %{tl_version}

%description -n texlive-font-change-xetex
This package consists of macros that can be used to typeset
"plain" XeTeX documents using any OpenType or TrueType font
installed on the computer system. The macros allow the user to
change the text mode fonts and some math mode fonts. For any
declared font family, various font style, weight, and size
variants like bold, italics, small caps, etc., are available
through standard and custom TeX control statements. Using the
optional argument of the macros, the available XeTeX font
features and OpenType tags can be accessed. Other features of
the package include activating and deactivating hanging
punctuation, and support for special Unicode characters.

%package -n texlive-fonts-churchslavonic
Provides:       tex-fonts-churchslavonic = %{tl_version}
License:        OFL
Summary:        Fonts for typesetting in Church Slavonic language
Version:        svn43121
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(FedorovskUnicode.otf) = %{tl_version}
Provides:       tex(MenaionUnicode.otf) = %{tl_version}, tex(PomorskyUnicode.otf) = %{tl_version}
Provides:       tex(PonomarUnicode.otf) = %{tl_version}, tex(FedorovskUnicode.ttf) = %{tl_version}
Provides:       tex(MenaionUnicode.ttf) = %{tl_version}, tex(PomorskyUnicode.ttf) = %{tl_version}
Provides:       tex(PonomarUnicode.ttf) = %{tl_version}

%description -n texlive-fonts-churchslavonic
The package provides Unicode-encoded OpenType fonts for Church
Slavonic.

%package -n texlive-fonts-churchslavonic-doc
Provides:       tex-fonts-churchslavonic-doc = %{tl_version}
License:        OFL
Summary:        doc files of fonts-churchslavonic
Version:        svn43121
AutoReqProv:    No

%description -n texlive-fonts-churchslavonic-doc
Documentation for fonts-churchslavonic.

%package -n texlive-footnotehyper-doc
Provides:       tex-footnotehyper-doc = %{tl_version}
License:        LPPL
Summary:        doc files of footnotehyper
Version:        svn46431
AutoReqProv:    No

%description -n texlive-footnotehyper-doc
Documentation for footnotehyper

%package -n texlive-footnotehyper
Provides:       tex-footnotehyper = %{tl_version}
License:        LPPL
Summary:        hyperref aware footnote.sty
Version:        svn46431
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(footnotehyper.sty) = %{tl_version}

%description -n texlive-footnotehyper
The footnote package by Mark Wooding dates back to 1997 and has
not been made hyperref compatible. The aim of the present
package is to do that.

%package -n texlive-fetchcls
Summary:        Fetch the current class name
Version:        svn45245
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fetchcls.sty) = %{tl_version}

%description -n texlive-fetchcls
With standard LaTeX you are able to check for the class in use
invoking the kernel command \@ifclassloaded. However, doing so
you cannot get the explicit class name, unless you want to loop
over every possible class name until \@ifclassloaded returns
true -- don't do that! With the help of the present package you
can obtain the name of the current class with significantly
less effort. Just load the package as usual:
\usepackage{fetchcls}; then, the control sequence \classname
will hold the name you were looking for.

%package -n texlive-fgruler
Summary:        draw rulers on the foreground or in the text
Version:        svn42966
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fgruler.sty) = %{tl_version}

%description -n texlive-fgruler
The fgruler is an abbreviation for the foreground ruler. This
package draws a horizontal and a vertical ruler on the
foreground of every (or a given) page at absolute position. In
this way, you can check the page layout dimensions. Besides,
you can draw various rulers in the text, too. The fgruler
package requires the services of the following packages:
kvoptions, etoolbox, xcolor, graphicx, eso-pic.

%package -n texlive-filecontentsdef
Summary:        filecontents + macro + verbatim
Version:        svn42107
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(filecontentsdef.sty) = %{tl_version}

%description -n texlive-filecontentsdef
The package provides two environments called filecontentsdef
and filecontentshere. They are derived from the LaTeX
filecontents environment as provided by Scott Pakin's
filecontents package. In addition to the file creation they
either store the (verbatim) contents in a macro
(filecontentsdef) or typeset them (verbatim) on the spot
(filecontentshere). The author developed the package to display
TeX code verbatim in documentation and the same time produce
the corresponding files during the LaTeX run in order to embed
them in the PDF as file attachment annotations (by using Scott
Pakin's package attachfile).

%package -n texlive-fixjfm
Summary:        Fix JFM (for *pTeX)
Version:        svn47113
License:        Knuth
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fixjfm.sty) = %{tl_version}

%description -n texlive-fixjfm
This package fixes several bugs in the JFM format. Both LaTeX
and plain TeX are supported.

%package -n texlive-fontloader-luaotfload
Summary:        Alternative fontloaders for luaotfload
Version:        svn45090
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%description -n texlive-fontloader-luaotfload
The package offers a few alternative fontloaders that can be
used with luaotfload to access some new features.

%package -n texlive-footmisx
Summary:        A range of footnote options
Version:        svn42621
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(footmisx.sty) = %{tl_version}

%description -n texlive-footmisx
This a fork of footmisc package allowing to use hyperref. Here
is a copy of the description of package footmisc: A collection
of ways to change the typesetting of footnotes. The package
provides means of changing the layout of the footnotes
themselves (including setting them in 'paragraphs' -- the para
option), a way to number footnotes per page (the perpage
option), to make footnotes disappear in a 'moving' argument
(stable option) and to deal with multiple references to
footnotes from the same place (multiple option). The package
also has a range of techniques for labelling footnotes with
symbols rather than numbers. Some of the functions of the
package are overlap with the functionality of other packages.
The para option is also provided by the manyfoot and bigfoot
packages, though those are both also portmanteau packages.
(Don't be seduced by fnpara, whose implementation is improved
by the present package.) The perpage option is also offered by
footnpag and by the rather more general-purpose perpage

%package -n texlive-forest-quickstart-doc
Summary:        Quickstart Guide for Linguists package "forest"
Version:        svn42503
License:        GFDL

%description -n texlive-forest-quickstart-doc
forest is a PGF/TikZ-based package for drawing linguistic (and
other kinds of) trees. This manual provides a quickstart guide
for linguists with just the essential things that you need to
get started.

%package -n texlive-forms16be
Summary:        Initialize form properties using big-endian encoding
Version:        svn45178
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(forms16be.sty) = %{tl_version}, tex(uni4basic-latin.def) = %{tl_version}

%description -n texlive-forms16be
This package provides support for UTF-16BE Unicode character
encoding (called a big-endian character string) for the text
string type (PDF Reference, version 1.7, beginning on page
158). Text strings are used in "text annotations, bookmark
names, article threads, document information, and so forth" (to
partially quote page 158). The particular application is to set
property values of form fields, at least those properties that
take the text strings as its value. The package contains
support for Basic Latin plus the ability to enter any unicode
character using the notation \uXXXX, where 'XXXX' are four hex
digits. The Package works for dvips/Distiller, pdfLaTeX,
LuaLaTeX, and XeLaTeX.

%package -n texlive-frederika2016
Summary:        An OpenType Greek calligraphy font
Version:        svn42157
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(Frederika2016.otf) = %{tl_version}

%description -n texlive-frederika2016
Frederika2016 is an attempt to digitize Hermann Zapf's
Frederika font. The font is the Greek companion of Virtuosa by
the same designer. This font is a calligraphy font and this is
an initial release.

%package -n texlive-fvextra
Summary:        Extensions and patches for fancyvrb
Version:        svn44787
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(ifthen.sty)
Requires:       tex(etoolbox.sty), tex(fancyvrb.sty), tex(upquote.sty), tex(textcomp.sty)
Requires:       tex(lineno.sty)
Provides:       tex(fvextra.sty) = %{tl_version}

%description -n texlive-fvextra
fvextra provides several extensions to fancyvrb, including
automatic line breaking and improved math mode. It also patches
some fancyvrb internals. Parts of fvextra were originally
developed as part of pythontex and minted.

%package -n texlive-fduthesis
Summary:        LaTeX thesis template for Fudan University
Version:        svn47628
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fdudoc.cls) = %{tl_version}, tex(fdulogo.sty) = %{tl_version}
Provides:       tex(fduthesis-en.cls) = %{tl_version}, tex(fduthesis.cls) = %{tl_version}
Provides:       tex(fduthesis.def) = %{tl_version}

%description -n texlive-fduthesis
This package is a LaTeX thesis template package for Fudan
University. It can make it easy to write theses both in Chinese
and English.

%package -n texlive-fnspe
Summary:        Macros for supporting mainly students of FNSPE CTU in Prague
Version:        svn45360
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fnspe.sty) = %{tl_version}

%description -n texlive-fnspe
This package is primary intended for students of FNSPE CTU in
Prague but many other students or scientists can found this
package as useful. This package implements different standards
of tensor notation, interval notation and complex notation.
Further many macros and shortcuts are added, e.q. for spaces,
operators, physics unit, etc.

%package -n texlive-fontawesome5
Summary:        Font Awesome 5 with with LaTeX support
Version:        svn48292
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fa5brands0.enc) = %{tl_version}, tex(fa5brands1.enc) = %{tl_version}
Provides:       tex(fa5free0.enc) = %{tl_version}, tex(fa5free1.enc) = %{tl_version}
Provides:       tex(fa5free2.enc) = %{tl_version}, tex(fontawesome5.map) = %{tl_version}
Provides:       tex(FontAwesome5Brands-Regular-400.otf) = %{tl_version}
Provides:       tex(FontAwesome5Free-Regular-400.otf) = %{tl_version}
Provides:       tex(FontAwesome5Free-Solid-900.otf) = %{tl_version}
Provides:       tex(fa5brands0.tfm) = %{tl_version}, tex(fa5brands1.tfm) = %{tl_version}
Provides:       tex(fa5free0regular.tfm) = %{tl_version}
Provides:       tex(fa5free0solid.tfm) = %{tl_version}, tex(fa5free1regular.tfm) = %{tl_version}
Provides:       tex(fa5free1solid.tfm) = %{tl_version}, tex(fa5free2regular.tfm) = %{tl_version}
Provides:       tex(fa5free2solid.tfm) = %{tl_version}, tex(FontAwesome5BrandsRegular.pfb) = %{tl_version}
Provides:       tex(FontAwesome5FreeRegular.pfb) = %{tl_version}
Provides:       tex(FontAwesome5FreeSolid.pfb) = %{tl_version}
Provides:       tex(fontawesome5-generic-helper.sty) = %{tl_version}
Provides:       tex(fontawesome5-mapping.def) = %{tl_version}
Provides:       tex(fontawesome5-utex-helper.sty) = %{tl_version}
Provides:       tex(fontawesome5.lua) = %{tl_version}, tex(fontawesome5.sty) = %{tl_version}
Provides:       tex(tufontawesomebrands.fd) = %{tl_version}
Provides:       tex(tufontawesomefree.fd) = %{tl_version}
Provides:       tex(tufontawesomepro.fd) = %{tl_version}
Provides:       tex(ufontawesomebrands0.fd) = %{tl_version}
Provides:       tex(ufontawesomebrands1.fd) = %{tl_version}
Provides:       tex(ufontawesomefree0.fd) = %{tl_version}
Provides:       tex(ufontawesomefree1.fd) = %{tl_version}
Provides:       tex(ufontawesomefree2.fd) = %{tl_version}

%description -n texlive-fontawesome5
This package provides LaTeX support for the included "Font
Awesome 5 Free" icon set. These icons were designed by Fort
Awesome and released under the SIL OFL 1.1 license. The
commercial "Pro" version is also supported, if it is installed
and XeLaTeX or LuaLaTeX is used.

%package -n texlive-formation-latex-ul
Summary:        Introductory LaTeX course in French
Version:        svn43005
License:        CC-BY-SA
Requires:       texlive-base texlive-kpathsea
Provides:       texlive-formation-latex-ul-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-formation-latex-ul-doc < 8:2018

%description -n texlive-formation-latex-ul
This package contains the supporting documentation, slides,
exercise files, and templates for an introductory LaTeX course
(in French) prepared for Universite Laval, Quebec, Canada.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts

font_names="public/fandol public/fbb public/fdsymbol public/fetamont public/fira"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir

install -d %{buildroot}/%{_infodir}/
mv %{buildroot}/%{_texdir}/texmf-dist/doc/info/* %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-fonts-tlwg
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/fonts-tlwg/
%{_texdir}/texmf-dist/fonts/enc/dvips/fonts-tlwg/
%{_texdir}/texmf-dist/fonts/map/dvips/fonts-tlwg/
%{_texdir}/texmf-dist/fonts/tfm/public/fonts-tlwg/
%{_texdir}/texmf-dist/fonts/type1/public/fonts-tlwg/
%{_texdir}/texmf-dist/fonts/vf/public/fonts-tlwg/
%{_texdir}/texmf-dist/tex/latex/fonts-tlwg/

%files -n texlive-fonts-tlwg-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/fonts-tlwg/

%files -n texlive-fancyhdr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fancyhdr/

%files -n texlive-fancyhdr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fancyhdr/

%files -n texlive-fix2col
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fix2col/

%files -n texlive-fix2col-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fix2col/

%files -n texlive-fbs
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/fbs/

%files -n texlive-figbib
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/figbib/
%{_texdir}/texmf-dist/tex/latex/figbib/

%files -n texlive-figbib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/figbib/

%files -n texlive-footbib
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/footbib/

%files -n texlive-footbib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/footbib/

%files -n texlive-francais-bst
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/francais-bst/
%{_texdir}/texmf-dist/tex/latex/francais-bst/

%files -n texlive-francais-bst-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/bibtex/francais-bst/

%files -n texlive-fbb
%license ofl.txt
%{_datadir}/fonts/fbb
%{_texdir}/texmf-dist/fonts/enc/dvips/fbb/
%{_texdir}/texmf-dist/fonts/map/dvips/fbb/
%{_texdir}/texmf-dist/fonts/opentype/public/fbb/
%{_texdir}/texmf-dist/fonts/tfm/public/fbb/
%{_texdir}/texmf-dist/fonts/type1/public/fbb/
%{_texdir}/texmf-dist/fonts/vf/public/fbb/
%{_texdir}/texmf-dist/tex/latex/fbb/

%files -n texlive-fbb-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/fbb/

%files -n texlive-fdsymbol
%license ofl.txt
%{_datadir}/fonts/fdsymbol
%{_texdir}/texmf-dist/fonts/enc/dvips/fdsymbol/
%{_texdir}/texmf-dist/fonts/map/dvips/fdsymbol/
%{_texdir}/texmf-dist/fonts/opentype/public/fdsymbol/
%{_texdir}/texmf-dist/fonts/source/public/fdsymbol/
%{_texdir}/texmf-dist/fonts/tfm/public/fdsymbol/
%{_texdir}/texmf-dist/fonts/type1/public/fdsymbol/
%{_texdir}/texmf-dist/tex/latex/fdsymbol/

%files -n texlive-fdsymbol-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/fdsymbol/
%{_texdir}/texmf-dist/doc/latex/fdsymbol/

%files -n texlive-fetamont
%license lppl1.3.txt
%{_datadir}/fonts/fetamont
%{_texdir}/texmf-dist/fonts/afm/public/fetamont/
%{_texdir}/texmf-dist/fonts/map/dvips/fetamont/
%{_texdir}/texmf-dist/fonts/opentype/public/fetamont/
%{_texdir}/texmf-dist/fonts/source/public/fetamont/
%{_texdir}/texmf-dist/fonts/tfm/public/fetamont/
%{_texdir}/texmf-dist/fonts/type1/public/fetamont/
%{_texdir}/texmf-dist/metapost/fetamont/
%{_texdir}/texmf-dist/tex/latex/fetamont/

%files -n texlive-fetamont-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/fetamont/

%files -n texlive-feyn
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/feyn/
%{_texdir}/texmf-dist/fonts/tfm/public/feyn/
%{_texdir}/texmf-dist/tex/latex/feyn/

%files -n texlive-feyn-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/feyn/

%files -n texlive-fge
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/fge/
%{_texdir}/texmf-dist/fonts/source/public/fge/
%{_texdir}/texmf-dist/fonts/tfm/public/fge/
%{_texdir}/texmf-dist/fonts/type1/public/fge/
%{_texdir}/texmf-dist/tex/latex/fge/

%files -n texlive-fge-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/fge/

%files -n texlive-fira
%license ofl.txt
%{_datadir}/fonts/fira
%{_texdir}/texmf-dist/fonts/enc/dvips/fira/
%{_texdir}/texmf-dist/fonts/map/dvips/fira/
%{_texdir}/texmf-dist/fonts/opentype/public/fira/
%{_texdir}/texmf-dist/fonts/tfm/public/fira/
%{_texdir}/texmf-dist/fonts/type1/public/fira/
%{_texdir}/texmf-dist/fonts/vf/public/fira/
%{_texdir}/texmf-dist/tex/latex/fira/

%files -n texlive-fira-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/fira/

%files -n texlive-foekfont
%license gpl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/foekfont/
%{_texdir}/texmf-dist/fonts/tfm/public/foekfont/
%{_texdir}/texmf-dist/fonts/type1/public/foekfont/
%{_texdir}/texmf-dist/tex/latex/foekfont/

%files -n texlive-foekfont-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/foekfont/

%files -n texlive-fonetika
%{_texdir}/texmf-dist/fonts/afm/public/fonetika/
%{_texdir}/texmf-dist/fonts/map/dvips/fonetika/
%{_texdir}/texmf-dist/fonts/tfm/public/fonetika/
%{_texdir}/texmf-dist/fonts/truetype/public/fonetika/
%{_texdir}/texmf-dist/fonts/type1/public/fonetika/
%{_texdir}/texmf-dist/tex/latex/fonetika/

%files -n texlive-fonetika-doc
%{_texdir}/texmf-dist/doc/fonts/fonetika/

%files -n texlive-fontawesome
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/fontawesome/
%{_texdir}/texmf-dist/fonts/map/dvips/fontawesome/
%{_texdir}/texmf-dist/fonts/opentype/public/fontawesome/
%{_texdir}/texmf-dist/fonts/tfm/public/fontawesome/
%{_texdir}/texmf-dist/fonts/type1/public/fontawesome/
%{_texdir}/texmf-dist/tex/latex/fontawesome/

%files -n texlive-fontawesome-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/fontawesome/

%files -n texlive-fontmfizz
%license other-free.txt
%{_texdir}/texmf-dist/fonts/truetype/public/fontmfizz/
%{_texdir}/texmf-dist/tex/latex/fontmfizz/

%files -n texlive-fontmfizz-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/fonts/fontmfizz/

%files -n texlive-fourier
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/fourier/
%{_texdir}/texmf-dist/fonts/map/dvips/fourier/
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/
%{_texdir}/texmf-dist/fonts/type1/public/fourier/
%{_texdir}/texmf-dist/fonts/vf/public/fourier/
%{_texdir}/texmf-dist/tex/latex/fourier/

%files -n texlive-fourier-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/fourier/

%files -n texlive-fouriernc
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/fouriernc/
%{_texdir}/texmf-dist/fonts/tfm/public/fouriernc/
%{_texdir}/texmf-dist/fonts/vf/public/fouriernc/
%{_texdir}/texmf-dist/tex/latex/fouriernc/

%files -n texlive-fouriernc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/fouriernc/

%files -n texlive-frcursive
%license lppl1.2.txt
%{_texdir}/texmf-dist/fonts/map/dvips/frcursive/
%{_texdir}/texmf-dist/fonts/source/public/frcursive/
%{_texdir}/texmf-dist/fonts/tfm/public/frcursive/
%{_texdir}/texmf-dist/fonts/type1/public/frcursive/
%{_texdir}/texmf-dist/tex/latex/frcursive/

%files -n texlive-frcursive-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/fonts/frcursive/

%files -n texlive-fpl
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/fpl/
%{_texdir}/texmf-dist/fonts/type1/public/fpl/

%files -n texlive-fpl-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/fpl/

%files -n texlive-fenixpar
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/fenixpar/

%files -n texlive-fenixpar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/fenixpar/

%files -n texlive-fltpoint
%{_texdir}/texmf-dist/tex/generic/fltpoint/

%files -n texlive-fltpoint-doc
%{_texdir}/texmf-dist/doc/generic/fltpoint/

%files -n texlive-fntproof
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/fntproof/

%files -n texlive-fntproof-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/fntproof/

%files -n texlive-fontname
%license gpl.txt
%{_infodir}/fontname.info*
%{_texdir}/texmf-dist/fonts/map/fontname/

%files -n texlive-fontname-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/fontname/

%files -n texlive-fc
%license gpl2.txt
%{_texdir}/texmf-dist/fonts/source/jknappen/fc/
%{_texdir}/texmf-dist/fonts/tfm/jknappen/fc/
%{_texdir}/texmf-dist/tex/latex/fc/

%files -n texlive-fc-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/fc/

%files -n texlive-fandol
%license gpl.txt
%{_datadir}/fonts/fandol
%{_texdir}/texmf-dist/fonts/opentype/public/fandol/

%files -n texlive-fandol-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/fandol/

%files -n texlive-FAQ-en-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/FAQ-en/

%files -n texlive-first-latex-doc-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/first-latex-doc/

%files -n texlive-finbib
%{_texdir}/texmf-dist/bibtex/bst/finbib/

%files -n texlive-facture
%{_texdir}/texmf-dist/tex/xelatex/facture/

%files -n texlive-facture-doc
%{_texdir}/texmf-dist/doc/xelatex/facture/

%files -n texlive-frletter
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/frletter/

%files -n texlive-frletter-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/frletter/

%files -n texlive-fifinddo-info-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fifinddo-info/

%files -n texlive-fancyhdr-it-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fancyhdr-it/

%files -n texlive-fixltxhyph
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fixltxhyph/

%files -n texlive-fixltxhyph-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fixltxhyph/

%files -n texlive-frontespizio
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/frontespizio/

%files -n texlive-frontespizio-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/frontespizio/

%files -n texlive-feupphdteses
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/feupphdteses/

%files -n texlive-feupphdteses-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/feupphdteses/

%files -n texlive-fancybox
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/fancybox/

%files -n texlive-fancybox-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/fancybox/

%files -n texlive-fancyref
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/fancyref/

%files -n texlive-fancyref-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/fancyref/

%files -n texlive-fancyvrb
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fancyvrb/

%files -n texlive-fancyvrb-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fancyvrb/

%files -n texlive-float
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/float/

%files -n texlive-float-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/float/

%files -n texlive-fontspec
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fontspec/

%files -n texlive-fontspec-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fontspec/

%files -n texlive-fp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fp/
%{_texdir}/texmf-dist/tex/plain/fp/

%files -n texlive-fp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fp/

%files -n texlive-fast-diagram
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fast-diagram/

%files -n texlive-fast-diagram-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fast-diagram/

%files -n texlive-fitbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fitbox/

%files -n texlive-fitbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fitbox/

%files -n texlive-flowchart
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/flowchart/

%files -n texlive-flowchart-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/flowchart/

%files -n texlive-forest
%license lppl1.3.txt
%{_texdir}/texmf-dist/makeindex/forest/
%{_texdir}/texmf-dist/tex/latex/forest/

%files -n texlive-forest-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/forest/

%files -n texlive-facsimile
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/facsimile/

%files -n texlive-facsimile-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/facsimile/

%files -n texlive-factura
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/factura/

%files -n texlive-factura-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/factura/

%files -n texlive-fancylabel
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/fancylabel/

%files -n texlive-fancylabel-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/fancylabel/

%files -n texlive-fancynum
%{_texdir}/texmf-dist/tex/latex/fancynum/

%files -n texlive-fancynum-doc
%{_texdir}/texmf-dist/doc/latex/fancynum/

%files -n texlive-fancypar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fancypar/

%files -n texlive-fancypar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fancypar/

%files -n texlive-fancyslides
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fancyslides/

%files -n texlive-fancyslides-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fancyslides/

%files -n texlive-fancytabs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fancytabs/

%files -n texlive-fancytabs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fancytabs/

%files -n texlive-fancytooltips
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/fancytooltips/

%files -n texlive-fancytooltips-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/fancytooltips/

%files -n texlive-fcolumn
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/fcolumn/

%files -n texlive-fcolumn-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/fcolumn/

%files -n texlive-fifo-stack
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fifo-stack/

%files -n texlive-fifo-stack-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fifo-stack/

%files -n texlive-figsize
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/figsize/

%files -n texlive-figsize-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/figsize/

%files -n texlive-filecontents
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/filecontents/

%files -n texlive-filecontents-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/filecontents/

%files -n texlive-filedate
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/filedate/

%files -n texlive-filedate-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/filedate/

%files -n texlive-filehook
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/filehook/

%files -n texlive-filehook-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/filehook/

%files -n texlive-fileinfo
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fileinfo/

%files -n texlive-fileinfo-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fileinfo/

%files -n texlive-filemod
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/filemod/
%{_texdir}/texmf-dist/tex/latex/filemod/

%files -n texlive-filemod-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/filemod/

%files -n texlive-fink
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fink/

%files -n texlive-fink-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fink/

%files -n texlive-finstrut
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/finstrut/

%files -n texlive-finstrut-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/finstrut/

%files -n texlive-fithesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fithesis/

%files -n texlive-fithesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fithesis/

%files -n texlive-fixfoot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fixfoot/

%files -n texlive-fixfoot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fixfoot/

%files -n texlive-fixme
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fixme/

%files -n texlive-fixme-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fixme/

%files -n texlive-fixmetodonotes
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/fixmetodonotes/

%files -n texlive-fixmetodonotes-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/fixmetodonotes/

%files -n texlive-fjodor
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/fjodor/

%files -n texlive-fjodor-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/fjodor/

%files -n texlive-flabels
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/flabels/

%files -n texlive-flabels-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/flabels/

%files -n texlive-flacards
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/flacards/

%files -n texlive-flacards-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/flacards/

%files -n texlive-flagderiv
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/flagderiv/

%files -n texlive-flagderiv-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/flagderiv/

%files -n texlive-flashcards
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/flashcards/

%files -n texlive-flashcards-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/flashcards/

%files -n texlive-flashmovie
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/flashmovie/

%files -n texlive-flashmovie-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/flashmovie/

%files -n texlive-flipbook
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/flipbook/

%files -n texlive-flipbook-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/flipbook/

%files -n texlive-flippdf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/flippdf/

%files -n texlive-flippdf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/flippdf/

%files -n texlive-floatflt
%{_texdir}/texmf-dist/tex/latex/floatflt/

%files -n texlive-floatflt-doc
%{_texdir}/texmf-dist/doc/latex/floatflt/

%files -n texlive-floatrow
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/floatrow/

%files -n texlive-floatrow-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/floatrow/

%files -n texlive-flowfram
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/flowfram/
%{_texdir}/texmf-dist/tex/latex/flowfram/

%files -n texlive-flowfram-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/flowfram/

%files -n texlive-fmp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fmp/

%files -n texlive-fmp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fmp/

%files -n texlive-fmtcount
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/fmtcount/
%{_texdir}/texmf-dist/tex/latex/fmtcount/

%files -n texlive-fmtcount-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fmtcount/

%files -n texlive-fn2end
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/fn2end/

%files -n texlive-fn2end-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/fn2end/

%files -n texlive-fnbreak
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fnbreak/

%files -n texlive-fnbreak-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fnbreak/

%files -n texlive-fncychap
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fncychap/

%files -n texlive-fncychap-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fncychap/

%files -n texlive-fncylab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fncylab/

%files -n texlive-fncylab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fncylab/

%files -n texlive-fnpara
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fnpara/

%files -n texlive-fnpara-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fnpara/

%files -n texlive-fnpct
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fnpct/

%files -n texlive-fnpct-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fnpct/

%files -n texlive-fnumprint
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fnumprint/

%files -n texlive-fnumprint-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fnumprint/

%files -n texlive-foilhtml
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/foilhtml/

%files -n texlive-foilhtml-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/foilhtml/

%files -n texlive-fontaxes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fontaxes/

%files -n texlive-fontaxes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fontaxes/

%files -n texlive-fonttable
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fonttable/

%files -n texlive-fonttable-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fonttable/

%files -n texlive-footmisc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/footmisc/

%files -n texlive-footmisc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/footmisc/

%files -n texlive-footnotebackref
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/footnotebackref/

%files -n texlive-footnotebackref-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/footnotebackref/

%files -n texlive-footnoterange
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/footnoterange/

%files -n texlive-footnoterange-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/footnoterange/

%files -n texlive-footnpag
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/footnpag/

%files -n texlive-footnpag-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/footnpag/

%files -n texlive-forarray
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/forarray/

%files -n texlive-forarray-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/forarray/

%files -n texlive-foreign
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/foreign/

%files -n texlive-foreign-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/foreign/

%files -n texlive-forloop
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/forloop/

%files -n texlive-forloop-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/forloop/

%files -n texlive-formlett
%{_texdir}/texmf-dist/tex/generic/formlett/

%files -n texlive-formlett-doc
%{_texdir}/texmf-dist/doc/generic/formlett/

%files -n texlive-formular
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/formular/

%files -n texlive-formular-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/formular/

%files -n texlive-fragments
%license collection.txt
%{_texdir}/texmf-dist/tex/latex/fragments/

%files -n texlive-fragments-doc
%license collection.txt
%{_texdir}/texmf-dist/doc/latex/fragments/

%files -n texlive-frame
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/frame/

%files -n texlive-frame-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/frame/

%files -n texlive-framed
%{_texdir}/texmf-dist/tex/latex/framed/

%files -n texlive-framed-doc
%{_texdir}/texmf-dist/doc/latex/framed/

%files -n texlive-frankenstein
%license collection.txt
%{_texdir}/texmf-dist/bibtex/bib/frankenstein/
%{_texdir}/texmf-dist/bibtex/bst/frankenstein/
%{_texdir}/texmf-dist/tex/latex/frankenstein/

%files -n texlive-frankenstein-doc
%license collection.txt
%{_texdir}/texmf-dist/doc/latex/frankenstein/

%files -n texlive-frege
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/frege/

%files -n texlive-frege-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/frege/

%files -n texlive-ftcap
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/ftcap/

%files -n texlive-ftcap-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ftcap/

%files -n texlive-ftnxtra
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ftnxtra/

%files -n texlive-ftnxtra-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ftnxtra/

%files -n texlive-fullblck
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fullblck/

%files -n texlive-fullblck-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fullblck/

%files -n texlive-fullminipage
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/fullminipage/

%files -n texlive-fullminipage-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/fullminipage/

%files -n texlive-fullwidth
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fullwidth/

%files -n texlive-fullwidth-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fullwidth/

%files -n texlive-fundus-calligra
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/fundus-calligra/

%files -n texlive-fundus-calligra-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/fundus-calligra/

%files -n texlive-fundus-cyr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fundus-cyr/

%files -n texlive-fundus-sueterlin
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fundus-sueterlin/

%files -n texlive-fundus-sueterlin-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fundus-sueterlin/

%files -n texlive-fwlw
%{_texdir}/texmf-dist/tex/latex/fwlw/

%files -n texlive-fwlw-doc
%{_texdir}/texmf-dist/doc/latex/fwlw/

%files -n texlive-faktor
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/faktor/

%files -n texlive-faktor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/faktor/

%files -n texlive-featpost
%license gpl.txt
%{_texdir}/texmf-dist/metapost/featpost/

%files -n texlive-featpost-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/metapost/featpost/

%files -n texlive-feynmf
%license gpl.txt
%{_texdir}/texmf-dist/metafont/feynmf/
%{_texdir}/texmf-dist/metapost/feynmf/
%{_texdir}/texmf-dist/tex/latex/feynmf/

%files -n texlive-feynmf-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/feynmf/

%files -n texlive-feynmp-auto
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/feynmp-auto/

%files -n texlive-feynmp-auto-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/feynmp-auto/

%files -n texlive-figbas
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/figbas/
%{_texdir}/texmf-dist/fonts/map/dvips/figbas/
%{_texdir}/texmf-dist/fonts/tfm/public/figbas/
%{_texdir}/texmf-dist/fonts/type1/public/figbas/

%files -n texlive-figbas-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/figbas/

%files -n texlive-figflow
%{_texdir}/texmf-dist/tex/plain/figflow/

%files -n texlive-figflow-doc
%{_texdir}/texmf-dist/doc/plain/figflow/

%files -n texlive-fixpdfmag
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/fixpdfmag/

%files -n texlive-font-change
%{_texdir}/texmf-dist/tex/plain/font-change/

%files -n texlive-font-change-doc
%{_texdir}/texmf-dist/doc/plain/font-change/

%files -n texlive-fontch
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/fontch/

%files -n texlive-fontch-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/fontch/

%files -n texlive-fbithesis
%{_texdir}/texmf-dist/tex/latex/fbithesis/

%files -n texlive-fbithesis-doc
%{_texdir}/texmf-dist/doc/latex/fbithesis/

%files -n texlive-fcavtex
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/fcavtex/
%{_texdir}/texmf-dist/tex/latex/fcavtex/

%files -n texlive-fcavtex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fcavtex/

%files -n texlive-fcltxdoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fcltxdoc/

%files -n texlive-fcltxdoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fcltxdoc/

%files -n texlive-fei
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fei/

%files -n texlive-fei-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fei/

%files -n texlive-fouridx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/fouridx/

%files -n texlive-fouridx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/fouridx/

%files -n texlive-functan
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/functan/

%files -n texlive-functan-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/functan/

%files -n texlive-fixlatvian
%license lppl1.3.txt
%{_texdir}/texmf-dist/makeindex/fixlatvian/
%{_texdir}/texmf-dist/tex/xelatex/fixlatvian/

%files -n texlive-fixlatvian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/fixlatvian/

%files -n texlive-fontbook
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/fontbook/

%files -n texlive-fontbook-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/fontbook/

%files -n texlive-fontwrap
%license gpl.txt
%{_texdir}/texmf-dist/tex/xelatex/fontwrap/

%files -n texlive-fontwrap-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/xelatex/fontwrap/

%files -n texlive-ffslides-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ffslides/

%files -n texlive-ffslides
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ffslides/

%files -n texlive-fibeamer-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fibeamer/

%files -n texlive-fibeamer
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fibeamer/

%files -n texlive-fixcmex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/fixcmex/

%files -n texlive-fixcmex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/fixcmex/

%files -n texlive-font-change-xetex-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/xetex/font-change-xetex/

%files -n texlive-font-change-xetex
%license other-free.txt
%{_texdir}/texmf-dist/tex/xetex/font-change-xetex/

%files -n texlive-fonts-churchslavonic
%license ofl.txt
%{_texdir}/texmf-dist/fonts/opentype/public/fonts-churchslavonic/
%{_texdir}/texmf-dist/fonts/truetype/public/fonts-churchslavonic/

%files -n texlive-fonts-churchslavonic-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/fonts-churchslavonic/

%files -n texlive-footnotehyper-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/footnotehyper/

%files -n texlive-footnotehyper
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/footnotehyper/

%files -n texlive-fetchcls
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/fetchcls/
%{_texdir}/texmf-dist/tex/latex/fetchcls/

%files -n texlive-fgruler
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/fgruler/
%{_texdir}/texmf-dist/tex/latex/fgruler/

%files -n texlive-filecontentsdef
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/filecontentsdef/
%{_texdir}/texmf-dist/tex/latex/filecontentsdef/

%files -n texlive-fixjfm
%license knuth.txt
%doc %{_texdir}/texmf-dist/doc/generic/fixjfm/
%{_texdir}/texmf-dist/tex/generic/fixjfm/

%files -n texlive-fontloader-luaotfload
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/luatex/fontloader-luaotfload/
%{_texdir}/texmf-dist/tex/luatex/fontloader-luaotfload/

%files -n texlive-footmisx
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/footmisx/
%{_texdir}/texmf-dist/tex/latex/footmisx/

%files -n texlive-forest-quickstart-doc
%license fdl.txt
%doc %{_texdir}/texmf-dist/doc/latex/forest-quickstart/

%files -n texlive-forms16be
%license lppl1.2.txt
%doc %{_texdir}/texmf-dist/doc/latex/forms16be/
%{_texdir}/texmf-dist/tex/latex/forms16be/

%files -n texlive-frederika2016
%license ofl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/frederika2016/
%{_texdir}/texmf-dist/fonts/opentype/public/frederika2016/

%files -n texlive-fvextra
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/fvextra/
%{_texdir}/texmf-dist/tex/latex/fvextra/

%files -n texlive-fduthesis
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/fduthesis/
%doc %{_texdir}/texmf-dist/doc/latex/fduthesis/

%files -n texlive-fnspe
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/fnspe/
%doc %{_texdir}/texmf-dist/doc/latex/fnspe/

%files -n texlive-fontawesome5
%license ofl.txt lppl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/fontawesome5/
%{_texdir}/texmf-dist/fonts/map/dvips/fontawesome5/
%{_texdir}/texmf-dist/fonts/opentype/public/fontawesome5/
%{_texdir}/texmf-dist/fonts/tfm/public/fontawesome5/
%{_texdir}/texmf-dist/fonts/type1/public/fontawesome5/
%{_texdir}/texmf-dist/tex/latex/fontawesome5/
%doc %{_texdir}/texmf-dist/doc/fonts/fontawesome5/

%files -n texlive-formation-latex-ul
%doc %{_texdir}/texmf-dist/doc/latex/formation-latex-ul/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
