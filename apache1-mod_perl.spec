# TODO:
# - orphaned dirs for %{_manualdocdir}/mod/*html
#
%bcond_without	ipv6		# disable IPv6 support. must match same bcond from apache1-devel
#
%include	/usr/lib/rpm/macros.perl
%define		mod_name	perl
%define 	apxs	/usr/sbin/apxs1
Summary:	A Perl interpreter for the Apache Web server
Summary(cs):	Vestavìný interpret Perlu pro WWW server Apache
Summary(da):	En indbygget Perl-fortolker for webtjeneren Apache
Summary(de):	Ein eingebetteter Perl-Interpreter für den Apache Web-Server
Summary(es):	Intérprete Perl para el servidor Web Apache
Summary(fr):	Interpréteur Perl intégré pour le serveur Web Apache
Summary(id):	Interpreter Perl untuk web server Apache
Summary(is):	Perl túlkur fyrir Apache vefþjóninn
Summary(it):	Interprete Perl integrato per il server Web Apache
Summary(ja):	Apache Web ¥µ¡¼¥Ð¡¼ÍÑ¤ÎÁÈ¹þ¤ß Perl ¥¤¥ó¥¿¡¼¥×¥ê¥¿
Summary(nb):	En Perl-fortolker for webtjeneren Apache
Summary(pl):	Interpreter Perla dla serwera WWW Apache
Summary(pt):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru):	÷ÓÔÒÏÅÎÎÙÊ ÉÎÔÅÒÐÒÅÔÁÔÏÒ Perl ÄÌÑ WWW-ÓÅÒ×ÅÒÁ Apache
Summary(sk):	Interpreter jazyka Perl pre webový server Apache
Summary(sl):	Vkljuèeni perlovski tolmaè za spletni stre¾nik Apache
Summary(sv):	En inbyggd Perl-interpretator för webbservern Apache
Summary(uk):	íÏÄÕÌØ ×ÂÕÄÏ×Õ×ÁÎÎÑ ¦ÎÔÅÒÐÒÅÔÁÔÏÒÁ Perl × ÓÅÒ×ÅÒ Apache
Summary(zh_CN):	ÓÃÓÚ Apache web ·þÎñ³ÌÐòµÄ Perl ½âÊÍ³ÌÐò¡£
Name:		apache1-mod_perl
Version:	1.29
Release:	14
License:	GPL
Group:		Networking/Daemons
Source0:	http://perl.apache.org/dist/mod_perl-%{version}.tar.gz
# Source0-md5:	1491931790509b9af06fc037d02b0e7a
Patch0:		apache-perl-rh.patch
# from ftp://ftp.kddlabs.co.jp/Linux/packages/Kondara/pub/Jirai/
Patch1:		mod_perl-v6.patch
Patch2:		%{name}-optimize.patch
URL:		http://perl.apache.org/
BuildRequires:	%{apxs}
%{?with_ipv6:BuildRequires:	apache1(ipv6)-devel}
BuildRequires:	apache1-devel >= 1.3.33-2
BuildRequires:	perl-B-Graph
BuildRequires:	perl-BSD-Resource
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(triggerpostun):	sed >= 4.0
Requires:	apache1(EAPI)
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
Provides:	apache(mod_perl)
Obsoletes:	mod_perl
Obsoletes:	mod_perl-common
# older apache1-mod_perl could make bad autodeps to perl-mod_perl1
BuildConflicts:	apache1-mod_perl < 1.29-12.1
%{!?with_ipv6:Conflicts:	apache1(ipv6)}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)
%define		_noautoreqdep	'perl(Apache::.*)' 'perl(mod_perl)'
%define		_manualdocdir	%{_datadir}/apache1-manual

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code. Mod_perl
links the Perl runtime library into the Apache web server and provides
an object-oriented Perl interface for Apache's C language API. The end
result is a quicker CGI script turnaround process, since no external
Perl interpreter has to be started.

%description -l cs
Modul mod_perl zaèleòuje interpret Perlu do WWW serveru Apache, tak¾e
WWW server mù¾e pøímo provádìt programy v Perlu. Mod_perl pøipojuje
bìhovou knihovnu Perlu do Apache WWW serveru a poskytuje objektovì
orientované perlovské rozhraní pro API serveru Apache. Výsledkem je
rychlej¹í start CGI skriptù, proto¾e nemusí být startován externí
interpret Perlu.

%description -l de
Mod_perl integriert einen Perl-Interpreter in den Apache Web-Server,
so dass dieser Perl-Code direkt ausführen kann. Das Programm verknüpft
die Perl-Runtime-Bibliothek mit dem Apache Web-Sever und stellt eine
objektorientierte Perl-Benutzeroberfläche für die C-API des
Apache-Servers bereit. Das Resultat ist eine schnellere Ausführung von
CGI-Skripten, da kein externer Perl-Interpreter gestartet werden muss.

%description -l es
Mod_perl incluye un intérprete Perl en el servidor Apache, de manera
que se puede ejecutar el código Perl directamente desde el servidor
Web. Mod_perl enumera las bibliotecas runtime del Perl al Web servidor
Apache y proporciona una interfaz Perl object-oriented para las API
del lenguaje C. De tal modo que se obtiene una ejecución más rápida de
los script CGI sin necesidad de apoyarse en un intérprete Perl.

%description -l fr
Mod_perl incorpore un interpréteur Perl dans le serveur Web Apache, de
manière à ce que le serveur Web Apache puisse exécuter directement du
code Perl. Mod_perl lie la bibliothèque d'exécution Perl au serveur
Web Apache et fournit une interface Perl orientée objet pour l'API en
langage C d'Apache. Le résultat final est une exécution des scripts
CGI plus rapide, du fait qu'aucun interpréteur Perl externe ne doit
être démarré.

%description -l id
Mod_perl memasukkan interpreter Perl ke dalam web server Apache,
sehingga Apache dapat secara langsung menjalankan kode Perl. Mod_perl
me-link runtime library Perl ke dalam web server Apache dan
menyediakan antarmuka Perl yang object-oriented untuk API Apache yang
ditulis dalam C. Hasilnya, respon proses CGI lebih cepat, karena tidak
perlu lagi menjalankan interpreter Perl eksternal.

%description -l is
Mod_perl vinnur með perl á Apache vefþjóninum svo að Apache geti beint
keyrt Perl kóða. Mod_perl tengir Perl keyrslu söfnin við Apache
vefþjóninn og býður upp á hlutbundið Perl fyrir Apache C
forritunarmáls API. Það sem græðist er Hraðari CGI scriptur þar sem
það er engar úttengd Perl köll.

%description -l it
Mod_perl incorpora un interprete Perl nel server web Apache, in modo
che quest'ultimo possa eseguire direttamente il codice Perl. Mod_perl
collega la libreria runtime di Perl al server web Apache e fornisce
un'interfaccia Perl orientata all'oggetto per le API in linguaggio C
di Apache. In tal modo si velocizza il processo di turnaround degli
script CGI, poiché non è più necessario appoggiarsi ad un interprete
Perl esterno.

%description -l ja
mod_perl ¤Ï¡¢Apache Web ¥µ¡¼¥Ð¡¼¤¬Ä¾ÀÜ Perl ¥³¡¼¥É¤ò¼Â¹Ô¤Ç¤­¤ë¤è¤¦¤Ë¡¢
Perl ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤ò Apache Web ¥µ¡¼¥Ð¡¼¤ËÁÈ¤ß¹þ¤ß¤Þ¤¹¡£mod_perl ¤Ï¡¢
Perl ¤Î¥é¥ó¥¿¥¤¥à¥é¥¤¥Ö¥é¥ê¤ò Apache Web ¥µ¡¼¥Ð¡¼¤Ë¥ê¥ó¥¯¤µ¤»¡¢Apache
¤Î C ¸À¸ì API ÍÑ¤Î¥ª¥Ö¥¸¥§¥¯¥È»Ø¸þ¤Î Perl ¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òÄó¶¡
¤·¤Þ¤¹¡£¤½¤Î·ë²Ì¡¢³°Éô¤Î Perl ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤¬µ¯Æ°¤¹¤ëÉ¬Í×¤¬¤Ê¤¤¤¿¤á¡¢
CGI ¥¹¥¯¥ê¥×¥È¤Î¥¿¡¼¥ó¥¢¥é¥¦¥ó¥É¥×¥í¥»¥¹¤¬Â®¤¯¤Ê¤ê¤Þ¤¹¡£

%description -l pl
Mod_perl jest modu³em, który wyposa¿a serwer Apache w interpreter
Perla, umo¿liwiaj±c w ten sposób bezpo¶rednie wykonywanie kodu Perla
przez serwer bez potrzeby anga¿owania zewnêtrznego interpretera, co
przyspiesza procesy zwi±zane z uruchamianiem skryptów CGI.

%description -l pt
O mod_perl incorpora um interpretador de Perl no servidor Web Apache,
para que assim o servidor Web Apache possa executar directamente
código em Perl. O mod_perl associa a biblioteca de execução do Perl
com o servidor Web Apache e oferece uma interface orientada por
objectos do Perl para a API de C do Apache. O resultado final é um
processo de torneamento dos 'scripts' CGI mais rápido, dado que não
tem que se iniciar um interpretador de Perl externo.

%description -l ru
Mod_perl ×ÓÔÒÁÉ×ÁÅÔ Perl-ÉÎÔÒÅÐÒÅÔÁÔÏÒ × WWW-ÓÅÒ×ÅÒ Apache, ÔÁË ÞÔÏ
ÜÔÏÔ ÓÅÒ×ÅÒ ÍÏÖÅÔ ÎÁÐÒÑÍÕÀ ÒÁÂÏÔÁÔØ Ó ËÏÄÏÍ Perl. Mod_perl Ó×ÑÚÙ×ÁÅÔ
ÂÉÂÌÉÏÔÅËÕ ÒÅÁÌØÎÏÇÏ ×ÒÅÍÅÎÉ Perl Ó ÓÅÒ×ÅÒÏÍ Apache É ÓÏÄÅÒÖÉÔ
ÏÂßÅËÔÎÏ-ÏÒÉÅÎÔÉÒÏ×ÁÎÎÙÊ ÉÎÔÅÒÆÅÊÓ Perl API ÑÚÙËÁ Apache C. ëÏÎÅÞÎÙÊ
ÒÅÚÕÌØÔÁÔ - ÕÓËÏÒÅÎÎÁÑ ÒÁÂÏÔÁ ÓÏ ÓËÒÉÐÔÁÍÉ CGI.

%description -l sk
Mod_perl zaèleòuje interpreter Perlu do webového servera Apache;
server Apache potom mô¾e priamo vykonáva» príkazy Perlu. Mod_perl
zlinkuje kni¾nicu Perlu s webovým serverom Apache a poskytne tak
objektovo orietované rozhranie Perlu pre aplikaèné rozhranie servera
Apache v jazyku C. Výsledkom je rýchlej¹ie vykonanie CGI skriptu, bez
akéhokoµvek spustenia externého interpretera jazyka Perl.

%description -l sv
Mod_perl införlivar en Perl-interpretator i webbservern Apache, så att
webbervern Apach kan köra Perl-kod direkt. Mod_perl länkar in Perls
körtidsbibliotek i webbservern Apache och ger ett objektorienterat
Perl-gränssnitt till Apaches API i språket C. Slutresultatet är en
snabbare processomsättning av CGI-skript, eftersom ingen extern
Perl-interpretator behöver startas.

%description -l uk
ðÒÏÅËÔ ¦ÎÔÅÇÒÁÃ¦§ Apache ÔÁ Perl ÄÏÚ×ÏÌÑ¤ ×ÁÍ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ ×ÓÀ
ÐÏÔÕÖÎ¦ÓÔØ ÍÏ×É ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Perl ÔÁ web-ÓÅÒ×ÅÒÕ Apache. ãÅ
ÄÏÓÑÇÁ¤ÔØÓÑ ÛÌÑÈÏÍ ×ÂÕÄÏ×Õ×ÁÎÎÑ Â¦ÂÌ¦ÏÔÅË Perl ×ÓÅÒÅÄÉÎÕ ÓÅÒ×ÅÒÁ
Apache ÞÅÒÅÚ DSO ÔÁ ÎÁÄÁÎÎÑ ÏÂ'¤ËÔÎÏ-ÏÒ¦¤ÎÔÏ×ÁÎÉÈ Perl-Â¦ÂÌ¦ÏÔÅË ÄÌÑ
ÄÏÓÔÕÐÕ ÄÏ Apache API.

ãÅ ÄÏÓÑÇÁ¤ÔØÓÑ ÚÁ ÄÏÐÏÍÏÇÏÀ mod_perl'Á, ËÏÔÒÉÊ ÄÏÚ×ÏÌÑ¤ ÓÔ×ÏÒÀ×ÁÔÉ
ÍÏÄÕÌ¦ ÄÌÑ Apache ÂÅÚÐÏÓÅÒÅÄÎØÏ ÎÁ ÍÏ×¦ Perl. ëÒ¦Í ÃØÏÇÏ, ÃÅ ÄÏÚ×ÏÌÑ¤
ÕÎÉËÎÕÔÉ ÎÁËÌÁÄÎÉÈ ×ÉÔÒÁÔ ÎÁ ÚÁ×ÁÎÔÁÖÅÎÎÑ ¦ÎÔÅÒÐÒÅÔÁÔÏÒÁ Perl ÐÒÉ
ÏÂÒÏÂÃ¦ ËÏÖÎÏÇÏ ÚÁÐÉÔÕ.

%description -l zh_CN
Mod_perl ½« Perl ½âÊÍ³ÌÐòÓë Apache web ·þÎñ³ÌÐò½áºÏÔÚÒ»Æð£¬
ÒÔ±ãºóÕß¿ÉÒÔÖ±½ÓÖ´ÐÐ Perl ´úÂë¡£ Mod_perl ½« Perl ÔËÐÐÊ±¼ä³ÌÐò¿âÁ´½ÓÖÁ
Apache web ·þÎñ³ÌÐò£¬ ²¢Îª Apache µÄ C ÓïÑÔ API Ìá¹©ÃæÏò¶ÔÏóµÄ Perl
½Ó¿Ú¡£ ÓÉÓÚ²»±ØÆô¶¯ÈÎºÎÍâ²¿ Perl ½âÊÍ³ÌÐò£¬Òò´Ë»áÊ¹ CGI
½Å±¾»Ø×ª¹ý³Ì¸üÎª¿ìËÙ¡£

%package devel
Summary:	Files needed for building XS modules that use mod_perl
Summary(pl):	Pliki potrzebne do budowania modu³ów XS korzystaj±cych z mod_perla
Group:		Development/Libraries
Requires:	apache1-devel
Requires:	perl-mod_%{mod_name}1 = %{version}-%{release}

%description devel
The apache1-mod_perl-devel package contains the files needed for
building XS modules that use mod_perl.

%description devel -l pl
Ten pakiet zawiera pliki potrzebne do budowania modu³ów XS
korzystaj±cych z mod_perla.

%package -n perl-mod_%{mod_name}1
Summary:	Perl APIs for mod_perl
Summary(pl):	Perlowe API dla mod_perla
Group:		Development/Languages/Perl

%description -n perl-mod_%{mod_name}1
Perl APIs for mod_perl.

%description -n perl-mod_%{mod_name}1 -l pl
Perlowe API dla mod_perl.

%prep
%setup  -q -n mod_perl-%{version}
%patch0 -p1
%{?with_ipv6:%patch1 -p1}
%patch2 -p1

%build
%{__perl} Makefile.PL \
	USE_APXS=1 \
	WITH_APXS=%{apxs} \
	EVERYTHING=1 \
	PERL_STACKED_HANDLERS=1 \
	OPTIMIZE="%{rpmcflags}" \
	INSTALLDIRS=vendor

ln -s ../src/modules apaci/modules
chmod +x apaci/find_source

%{__make} \
	OPTIMIZE="%{rpmcflags}"
%{__make} -C faq

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/conf.d,%{_manualdocdir}/mod}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install apaci/libperl.so $RPM_BUILD_ROOT%{_pkglibdir}
install htdocs/manual/mod/mod_perl.html \
	$RPM_BUILD_ROOT%{_manualdocdir}/mod

echo 'LoadModule %{mod_name}_module	modules/lib%{mod_name}.so' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d/90_mod_%{mod_name}.conf

# clean known unpackaged files
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/*.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Bundle/Apache.pm
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/mod_%{mod_name}/.packlist
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/Bundle::Apache.3pm*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q apache restart

%postun
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%triggerpostun -- apache1-mod_%{mod_name} < 1.29-7.1
# check that they're not using old apache.conf
if grep -q '^Include conf\.d' /etc/apache/apache.conf; then
	%{__sed} -i -e '/^\(Add\|Load\)Module.*libperl\.\(so\|c\)/d' /etc/apache/apache.conf
fi

%files
%defattr(644,root,root,755)
%doc README INSTALL CREDITS faq/*.html faq/*.txt apache-modlist.html eg
# FIXME: parent dirs not owned as the manualdocdir (via apache1-doc) is not in deps
%doc %{_manualdocdir}/mod/*html

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*

%files -n perl-mod_%{mod_name}1
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/*.PL

%dir %{perl_vendorarch}/Apache
%{perl_vendorarch}/Apache/*.pm
%{perl_vendorarch}/Apache/Constants
%dir %{perl_vendorarch}/auto/Apache
%dir %{perl_vendorarch}/auto/Apache/Leak
%dir %{perl_vendorarch}/auto/Apache/Symbol

%{perl_vendorarch}/auto/*/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/*/*/*.so

%{_mandir}/man3/[Acm]*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/auto/Apache/typemap
%{perl_vendorarch}/auto/Apache/mod_perl.exp
%{perl_vendorarch}/auto/Apache/include
