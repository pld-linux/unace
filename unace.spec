Summary:	unACE - extract, test and view ACE archives
Summary(pl):	unACE - rozpakowuje, testuje i przegl±da archiwa ACE
Name:		unace
Version:	2.2
Release:	2
License:	Freeware
Group:		Applications/Archiving
Source0:	http://hem.passagen.se/vanlid/winace/lin%{name}22.tgz
# Source0-md5:	218020e64975775e191077a195732735
URL:		http://www.winace.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unACE utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the ACE archiver.

%description -l pl
UnACE jest programem freeware, rozpowszechnianym wraz z kodem
¼ród³owym, przeznaczonym do rozpakowywania, testowania oraz
przegl±dania zawarto¶ci archiwów stworzonych przez program ACE.

%prep
%setup -q -c -T
tar zxf %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unace $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc file_id.diz
%attr(755,root,root) %{_bindir}/unace
