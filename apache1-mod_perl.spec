# TODO:
# - add devel subpackage
%include	/usr/lib/rpm/macros.perl
%define 	apxs	/usr/sbin/apxs1
Summary:	A Perl interpreter for the Apache Web server
Summary(cs):	Vestav�n� interpret Perlu pro WWW server Apache
Summary(da):	En indbygget Perl-fortolker for webtjeneren Apache
Summary(de):	Ein eingebetteter Perl-Interpreter f�r den Apache Web-Server
Summary(es):	Int�rprete Perl para el servidor Web Apache
Summary(fr):	Interpr�teur Perl int�gr� pour le serveur Web Apache
Summary(id):	Interpreter Perl untuk web server Apache
Summary(is):	Perl t�lkur fyrir Apache vef�j�ninn
Summary(it):	Interprete Perl integrato per il server Web Apache
Summary(ja):	Apache Web �����С��Ѥ��ȹ��� Perl ���󥿡��ץ꥿
Summary(nb):	En Perl-fortolker for webtjeneren Apache
Summary(pl):	Interpreter Perla dla serwera WWW Apache
Summary(pt):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru):	���������� ������������� Perl ��� WWW-������� Apache
Summary(sk):	Interpreter jazyka Perl pre webov� server Apache
Summary(sl):	Vklju�eni perlovski tolma� za spletni stre�nik Apache
Summary(sv):	En inbyggd Perl-interpretator f�r webbservern Apache
Summary(uk):	������ ������������ �������������� Perl � ������ Apache
Summary(zh_CN):	���� Apache web �������� Perl ���ͳ���
Name:		apache1-mod_perl
Version:	1.29
Release:	6
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
BuildRequires:	apache1(EAPI)-devel >= 1.3.29-4
BuildRequires:	perl-B-Graph
BuildRequires:	perl-BSD-Resource
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
PreReq:		apache1(EAPI)
Requires(post,preun):	%{apxs}
%requires_eq	apache1
%requires_eq	perl-base
Provides:	perl(mod_perl_hooks)
Provides:	mod_perl
Obsoletes:	mod_perl
Obsoletes:	mod_perl-common
Obsoletes:	perl-Apache-Test
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(Apache::.*)' 'perl(mod_perl)'

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code. Mod_perl
links the Perl runtime library into the Apache web server and provides
an object-oriented Perl interface for Apache's C language API. The end
result is a quicker CGI script turnaround process, since no external
Perl interpreter has to be started.

%description -l cs
Modul mod_perl za�le�uje interpret Perlu do WWW serveru Apache, tak�e
WWW server m��e p��mo prov�d�t programy v Perlu. Mod_perl p�ipojuje
b�hovou knihovnu Perlu do Apache WWW serveru a poskytuje objektov�
orientovan� perlovsk� rozhran� pro API serveru Apache. V�sledkem je
rychlej�� start CGI skript�, proto�e nemus� b�t startov�n extern�
interpret Perlu.

%description -l de
Mod_perl integriert einen Perl-Interpreter in den Apache Web-Server,
so dass dieser Perl-Code direkt ausf�hren kann. Das Programm verkn�pft
die Perl-Runtime-Bibliothek mit dem Apache Web-Sever und stellt eine
objektorientierte Perl-Benutzeroberfl�che f�r die C-API des
Apache-Servers bereit. Das Resultat ist eine schnellere Ausf�hrung von
CGI-Skripten, da kein externer Perl-Interpreter gestartet werden muss.

%description -l es
Mod_perl incluye un int�rprete Perl en el servidor Apache, de manera
que se puede ejecutar el c�digo Perl directamente desde el servidor
Web. Mod_perl enumera las bibliotecas runtime del Perl al Web servidor
Apache y proporciona una interfaz Perl object-oriented para las API
del lenguaje C. De tal modo que se obtiene una ejecuci�n m�s r�pida de
los script CGI sin necesidad de apoyarse en un int�rprete Perl.

%description -l fr
Mod_perl incorpore un interpr�teur Perl dans le serveur Web Apache, de
mani�re � ce que le serveur Web Apache puisse ex�cuter directement du
code Perl. Mod_perl lie la biblioth�que d'ex�cution Perl au serveur
Web Apache et fournit une interface Perl orient�e objet pour l'API en
langage C d'Apache. Le r�sultat final est une ex�cution des scripts
CGI plus rapide, du fait qu'aucun interpr�teur Perl externe ne doit
�tre d�marr�.

%description -l id
Mod_perl memasukkan interpreter Perl ke dalam web server Apache,
sehingga Apache dapat secara langsung menjalankan kode Perl. Mod_perl
me-link runtime library Perl ke dalam web server Apache dan
menyediakan antarmuka Perl yang object-oriented untuk API Apache yang
ditulis dalam C. Hasilnya, respon proses CGI lebih cepat, karena tidak
perlu lagi menjalankan interpreter Perl eksternal.

%description -l is
Mod_perl vinnur me� perl � Apache vef�j�ninum svo a� Apache geti beint
keyrt Perl k��a. Mod_perl tengir Perl keyrslu s�fnin vi� Apache
vef�j�ninn og b��ur upp � hlutbundi� Perl fyrir Apache C
forritunarm�ls API. �a� sem gr��ist er Hra�ari CGI scriptur �ar sem
�a� er engar �ttengd Perl k�ll.

%description -l it
Mod_perl incorpora un interprete Perl nel server web Apache, in modo
che quest'ultimo possa eseguire direttamente il codice Perl. Mod_perl
collega la libreria runtime di Perl al server web Apache e fornisce
un'interfaccia Perl orientata all'oggetto per le API in linguaggio C
di Apache. In tal modo si velocizza il processo di turnaround degli
script CGI, poich� non � pi� necessario appoggiarsi ad un interprete
Perl esterno.

%description -l ja
mod_perl �ϡ�Apache Web �����С���ľ�� Perl �����ɤ�¹ԤǤ���褦�ˡ�
Perl ���󥿡��ץ꥿�� Apache Web �����С����Ȥ߹��ߤޤ���mod_perl �ϡ�
Perl �Υ�󥿥���饤�֥��� Apache Web �����С��˥�󥯤�����Apache
�� C ���� API �ѤΥ��֥������Ȼظ��� Perl ���󥿡��ե���������
���ޤ������η�̡������� Perl ���󥿡��ץ꥿����ư����ɬ�פ��ʤ����ᡢ
CGI ������ץȤΥ����󥢥饦��ɥץ�������®���ʤ�ޤ���

%description -l pl
Mod_perl jest modu�em, kt�ry wyposa�a serwer Apache w interpreter
Perla, umo�liwiaj�c w ten spos�b bezpo�rednie wykonywanie kodu Perla
przez serwer bez potrzeby anga�owania zewn�trznego interpretera, co
przyspiesza procesy zwi�zane z uruchamianiem skrypt�w CGI.

%description -l pt
O mod_perl incorpora um interpretador de Perl no servidor Web Apache,
para que assim o servidor Web Apache possa executar directamente
c�digo em Perl. O mod_perl associa a biblioteca de execu��o do Perl
com o servidor Web Apache e oferece uma interface orientada por
objectos do Perl para a API de C do Apache. O resultado final � um
processo de torneamento dos 'scripts' CGI mais r�pido, dado que n�o
tem que se iniciar um interpretador de Perl externo.

%description -l ru
Mod_perl ���������� Perl-������������� � WWW-������ Apache, ��� ���
���� ������ ����� �������� �������� � ����� Perl. Mod_perl ���������
���������� ��������� ������� Perl � �������� Apache � ��������
��������-��������������� ��������� Perl API ����� Apache C. ��������
��������� - ���������� ������ �� ��������� CGI.

%description -l sk
Mod_perl za�le�uje interpreter Perlu do webov�ho servera Apache;
server Apache potom m��e priamo vykon�va� pr�kazy Perlu. Mod_perl
zlinkuje kni�nicu Perlu s webov�m serverom Apache a poskytne tak
objektovo orietovan� rozhranie Perlu pre aplika�n� rozhranie servera
Apache v jazyku C. V�sledkom je r�chlej�ie vykonanie CGI skriptu, bez
ak�hoko�vek spustenia extern�ho interpretera jazyka Perl.

%description -l sv
Mod_perl inf�rlivar en Perl-interpretator i webbservern Apache, s� att
webbervern Apach kan k�ra Perl-kod direkt. Mod_perl l�nkar in Perls
k�rtidsbibliotek i webbservern Apache och ger ett objektorienterat
Perl-gr�nssnitt till Apaches API i spr�ket C. Slutresultatet �r en
snabbare processoms�ttning av CGI-skript, eftersom ingen extern
Perl-interpretator beh�ver startas.

%description -l uk
������ �������æ� Apache �� Perl ������Ѥ ��� ��������������� ���
�����Φ��� ���� ������������� Perl �� web-������� Apache. ��
����������� ������ ������������ ¦�̦���� Perl ��������� �������
Apache ����� DSO �� ������� ��'�����-�Ҧ��������� Perl-¦�̦���� ���
������� �� Apache API.

�� ����������� �� ��������� mod_perl'�, ������ ������Ѥ ����������
����̦ ��� Apache ������������� �� ��צ Perl. �Ҧ� �����, �� ������Ѥ
�������� ��������� ������ �� ������������ �������������� Perl ���
�����æ ������� ������.

%description -l zh_CN
Mod_perl �� Perl ���ͳ����� Apache web �����������һ��
�Ա���߿���ֱ��ִ�� Perl ���롣 Mod_perl �� Perl ����ʱ������������
Apache web ������� ��Ϊ Apache �� C ���� API �ṩ�������� Perl
�ӿڡ� ���ڲ��������κ��ⲿ Perl ���ͳ�����˻�ʹ CGI
�ű���ת���̸�Ϊ���١�

%prep
%setup  -q -n mod_perl-%{version}
%patch0 -p1
%patch1 -p1
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
install -d $RPM_BUILD_ROOT{%{_libdir}/apache1,/home/apache/manual/mod}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install apaci/libperl.so $RPM_BUILD_ROOT%{_libdir}/apache1
install htdocs/manual/mod/mod_perl.html \
	$RPM_BUILD_ROOT/home/apache/manual/mod

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{apxs} -e -a -n perl %{_libexecdir}/libperl.so 1>&2
if [ -f /var/lock/subsys/apache ]; then
	/etc/rc.d/init.d/apache restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/apache start\" to start apache HTTP daemon."
fi

%preun
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n perl %{_libexecdir}/libperl.so 1>&2
	if [ -f /var/lock/subsys/apache ]; then
		/etc/rc.d/init.d/apache restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc README INSTALL CREDITS faq/*.html faq/*.txt apache-modlist.html eg
%doc /home/apache/manual/mod/*html

%attr(755,root,root) %{_libdir}/apache1/*.so

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

# to -devel ?
%{perl_vendorarch}/auto/Apache/typemap
%{perl_vendorarch}/auto/Apache/mod_perl.exp
%{perl_vendorarch}/auto/Apache/include
