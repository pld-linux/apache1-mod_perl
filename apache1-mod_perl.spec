# TODO
# - hard to solve and is it worth?
#   Apache::Util::escape_html() can't be used outside Aapache it is xs and in shared library which is also the apache module
#   fix would be probably link only Apachye symbols to apache module and put rest of the symbols as perl library
#   perl-HTML-Menu-Select uses that method in test.
# 
# Conditional build:
%bcond_without	ipv6	# IPv6 support (must match same bcond from apache1-devel)
#
%include	/usr/lib/rpm/macros.perl
%define		mod_name	perl
%define 	apxs	/usr/sbin/apxs1
Summary:	A Perl interpreter for the Apache Web server
Summary(cs.UTF-8):	Vestavěný interpret Perlu pro WWW server Apache
Summary(da.UTF-8):	En indbygget Perl-fortolker for webtjeneren Apache
Summary(de.UTF-8):	Ein eingebetteter Perl-Interpreter für den Apache Web-Server
Summary(es.UTF-8):	Intérprete Perl para el servidor Web Apache
Summary(fr.UTF-8):	Interpréteur Perl intégré pour le serveur Web Apache
Summary(id.UTF-8):	Interpreter Perl untuk web server Apache
Summary(is.UTF-8):	Perl túlkur fyrir Apache vefþjóninn
Summary(it.UTF-8):	Interprete Perl integrato per il server Web Apache
Summary(ja.UTF-8):	Apache Web サーバー用の組込み Perl インタープリタ
Summary(nb.UTF-8):	En Perl-fortolker for webtjeneren Apache
Summary(pl.UTF-8):	Interpreter Perla dla serwera WWW Apache
Summary(pt.UTF-8):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru.UTF-8):	Встроенный интерпретатор Perl для WWW-сервера Apache
Summary(sk.UTF-8):	Interpreter jazyka Perl pre webový server Apache
Summary(sl.UTF-8):	Vključeni perlovski tolmač za spletni strežnik Apache
Summary(sv.UTF-8):	En inbyggd Perl-interpretator för webbservern Apache
Summary(uk.UTF-8):	Модуль вбудовування інтерпретатора Perl в сервер Apache
Summary(zh_CN.UTF-8):	用于 Apache web 服务程序的 Perl 解释程序。
Name:		apache1-mod_perl
Version:	1.30
Release:	1
License:	Apache v1.1
Group:		Networking/Daemons
Source0:	http://perl.apache.org/dist/mod_perl-%{version}.tar.gz
# Source0-md5:	bfd6f6cff1ab1cc3dbb58a236701d169
Patch0:		apache-perl-rh.patch
# from ftp://ftp.kddlabs.co.jp/Linux/packages/Kondara/pub/Jirai/
Patch1:		mod_perl-v6.patch
Patch2:		%{name}-optimize.patch
URL:		http://perl.apache.org/
%{?with_ipv6:BuildRequires:	apache1(ipv6)-devel}
BuildRequires:	apache1-devel >= 1.3.39-2
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

%description -l cs.UTF-8
Modul mod_perl začleňuje interpret Perlu do WWW serveru Apache, takže
WWW server může přímo provádět programy v Perlu. Mod_perl připojuje
běhovou knihovnu Perlu do Apache WWW serveru a poskytuje objektově
orientované perlovské rozhraní pro API serveru Apache. Výsledkem je
rychlejší start CGI skriptů, protože nemusí být startován externí
interpret Perlu.

%description -l de.UTF-8
Mod_perl integriert einen Perl-Interpreter in den Apache Web-Server,
so dass dieser Perl-Code direkt ausführen kann. Das Programm verknüpft
die Perl-Runtime-Bibliothek mit dem Apache Web-Sever und stellt eine
objektorientierte Perl-Benutzeroberfläche für die C-API des
Apache-Servers bereit. Das Resultat ist eine schnellere Ausführung von
CGI-Skripten, da kein externer Perl-Interpreter gestartet werden muss.

%description -l es.UTF-8
Mod_perl incluye un intérprete Perl en el servidor Apache, de manera
que se puede ejecutar el código Perl directamente desde el servidor
Web. Mod_perl enumera las bibliotecas runtime del Perl al Web servidor
Apache y proporciona una interfaz Perl object-oriented para las API
del lenguaje C. De tal modo que se obtiene una ejecución más rápida de
los script CGI sin necesidad de apoyarse en un intérprete Perl.

%description -l fr.UTF-8
Mod_perl incorpore un interpréteur Perl dans le serveur Web Apache, de
manière à ce que le serveur Web Apache puisse exécuter directement du
code Perl. Mod_perl lie la bibliothèque d'exécution Perl au serveur
Web Apache et fournit une interface Perl orientée objet pour l'API en
langage C d'Apache. Le résultat final est une exécution des scripts
CGI plus rapide, du fait qu'aucun interpréteur Perl externe ne doit
être démarré.

%description -l id.UTF-8
Mod_perl memasukkan interpreter Perl ke dalam web server Apache,
sehingga Apache dapat secara langsung menjalankan kode Perl. Mod_perl
me-link runtime library Perl ke dalam web server Apache dan
menyediakan antarmuka Perl yang object-oriented untuk API Apache yang
ditulis dalam C. Hasilnya, respon proses CGI lebih cepat, karena tidak
perlu lagi menjalankan interpreter Perl eksternal.

%description -l is.UTF-8
Mod_perl vinnur með perl á Apache vefþjóninum svo að Apache geti beint
keyrt Perl kóða. Mod_perl tengir Perl keyrslu söfnin við Apache
vefþjóninn og býður upp á hlutbundið Perl fyrir Apache C
forritunarmáls API. Það sem græðist er Hraðari CGI scriptur þar sem
það er engar úttengd Perl köll.

%description -l it.UTF-8
Mod_perl incorpora un interprete Perl nel server web Apache, in modo
che quest'ultimo possa eseguire direttamente il codice Perl. Mod_perl
collega la libreria runtime di Perl al server web Apache e fornisce
un'interfaccia Perl orientata all'oggetto per le API in linguaggio C
di Apache. In tal modo si velocizza il processo di turnaround degli
script CGI, poiché non è più necessario appoggiarsi ad un interprete
Perl esterno.

%description -l ja.UTF-8
mod_perl は、Apache Web サーバーが直接 Perl コードを実行できるように、
Perl インタープリタを Apache Web サーバーに組み込みます。mod_perl は、
Perl のランタイムライブラリを Apache Web サーバーにリンクさせ、Apache
の C 言語 API 用のオブジェクト指向の Perl インターフェイスを提供
します。その結果、外部の Perl インタープリタが起動する必要がないため、
CGI スクリプトのターンアラウンドプロセスが速くなります。

%description -l pl.UTF-8
Mod_perl jest modułem, który wyposaża serwer Apache w interpreter
Perla, umożliwiając w ten sposób bezpośrednie wykonywanie kodu Perla
przez serwer bez potrzeby angażowania zewnętrznego interpretera, co
przyspiesza procesy związane z uruchamianiem skryptów CGI.

%description -l pt.UTF-8
O mod_perl incorpora um interpretador de Perl no servidor Web Apache,
para que assim o servidor Web Apache possa executar directamente
código em Perl. O mod_perl associa a biblioteca de execução do Perl
com o servidor Web Apache e oferece uma interface orientada por
objectos do Perl para a API de C do Apache. O resultado final é um
processo de torneamento dos 'scripts' CGI mais rápido, dado que não
tem que se iniciar um interpretador de Perl externo.

%description -l ru.UTF-8
Mod_perl встраивает Perl-интрепретатор в WWW-сервер Apache, так что
этот сервер может напрямую работать с кодом Perl. Mod_perl связывает
библиотеку реального времени Perl с сервером Apache и содержит
объектно-ориентированный интерфейс Perl API языка Apache C. Конечный
результат - ускоренная работа со скриптами CGI.

%description -l sk.UTF-8
Mod_perl začleňuje interpreter Perlu do webového servera Apache;
server Apache potom môže priamo vykonávať príkazy Perlu. Mod_perl
zlinkuje knižnicu Perlu s webovým serverom Apache a poskytne tak
objektovo orietované rozhranie Perlu pre aplikačné rozhranie servera
Apache v jazyku C. Výsledkom je rýchlejšie vykonanie CGI skriptu, bez
akéhokoľvek spustenia externého interpretera jazyka Perl.

%description -l sv.UTF-8
Mod_perl införlivar en Perl-interpretator i webbservern Apache, så att
webbervern Apach kan köra Perl-kod direkt. Mod_perl länkar in Perls
körtidsbibliotek i webbservern Apache och ger ett objektorienterat
Perl-gränssnitt till Apaches API i språket C. Slutresultatet är en
snabbare processomsättning av CGI-skript, eftersom ingen extern
Perl-interpretator behöver startas.

%description -l uk.UTF-8
Проект інтеграції Apache та Perl дозволяє вам використовувати всю
потужність мови програмування Perl та web-серверу Apache. Це
досягається шляхом вбудовування бібліотек Perl всередину сервера
Apache через DSO та надання об'єктно-орієнтованих Perl-бібліотек для
доступу до Apache API.

Це досягається за допомогою mod_perl'а, котрий дозволяє створювати
модулі для Apache безпосередньо на мові Perl. Крім цього, це дозволяє
уникнути накладних витрат на завантаження інтерпретатора Perl при
обробці кожного запиту.

%description -l zh_CN.UTF-8
Mod_perl 将 Perl 解释程序与 Apache web 服务程序结合在一起，
以便后者可以直接执行 Perl 代码。 Mod_perl 将 Perl 运行时间程序库链接至
Apache web 服务程序， 并为 Apache 的 C 语言 API 提供面向对象的 Perl
接口。 由于不必启动任何外部 Perl 解释程序，因此会使 CGI
脚本回转过程更为快速。

%package -n perl-mod_perl1
Summary:	Perl APIs for mod_perl
Summary(pl.UTF-8):	Perlowe API dla mod_perla
Group:		Development/Languages/Perl

%description -n perl-mod_perl1
Perl APIs for mod_perl.

%description -n perl-mod_perl1 -l pl.UTF-8
Perlowe API dla mod_perl.

%package -n perl-mod_perl1-devel
Summary:	Files needed for building XS modules that use mod_perl
Summary(pl.UTF-8):	Pliki potrzebne do budowania modułów XS korzystających z mod_perla
Group:		Development/Libraries
Requires:	apache1-devel
Requires:	perl-mod_perl1 = %{version}-%{release}
Obsoletes:	apache1-mod_perl-devel

%description -n perl-mod_perl1-devel
The apache1-mod_perl-devel package contains the files needed for
building XS modules that use mod_perl.

%description -n perl-mod_perl1-devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do budowania modułów XS
korzystających z mod_perla.

%package doc
Summary:	mod_perl documentation
Summary(pl.UTF_8):	Dokumentacja do mod_perla
Group:		Documentation
Requires:	apache1-doc

%description doc
mod_perl online documentation.

%description doc -l pl.UTF-8
Dokumentacja do mod_perla dostępna przez Apache'a.

%prep
%setup -q -n mod_perl-%{version}
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
%doc CREDITS Changes INSTALL LICENSE README STATUS SUPPORT faq/*.html faq/*.txt apache-modlist.html eg
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/libperl.so

%files doc
%defattr(644,root,root,755)
%{_manualdocdir}/mod/mod_perl.html

%files -n perl-mod_perl1
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache.pm
%{perl_vendorarch}/mod_perl*.pm
%{perl_vendorarch}/mod_perl_hooks.pm.PL
%dir %{perl_vendorarch}/Apache
%{perl_vendorarch}/Apache/*.pm
%{perl_vendorarch}/Apache/Constants
%dir %{perl_vendorarch}/auto/Apache
%dir %{perl_vendorarch}/auto/Apache/Leak
%{perl_vendorarch}/auto/Apache/Leak/Leak.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Leak/Leak.so
%dir %{perl_vendorarch}/auto/Apache/Symbol
%{perl_vendorarch}/auto/Apache/Symbol/Symbol.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Symbol/Symbol.so
%{_mandir}/man3/Apache*.3pm*
%{_mandir}/man3/cgi_to_mod_perl.3pm*
%{_mandir}/man3/mod_perl*.3pm*

%files -n perl-mod_perl1-devel
%defattr(644,root,root,755)
%{perl_vendorarch}/auto/Apache/typemap
%{perl_vendorarch}/auto/Apache/mod_perl.exp
%{perl_vendorarch}/auto/Apache/include
