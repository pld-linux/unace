Summary:	unACE - extract, test and view ACE archives
Summary(pl.UTF-8):	unACE - rozpakowuje, testuje i przegląda archiwa ACE
Name:		unace
Version:	1.2b
Release:	4
Epoch:		1
License:	Freeware
Group:		Applications/Archiving
Source0:	%{name}pub.zip
# Source0-md5:	1a73dda37e4d8d8ef70f27a858e32a55
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unACE utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the ACE archiver.

%description -l pl.UTF-8
UnACE jest programem freeware, rozpowszechnianym wraz z kodem
źródłowym, przeznaczonym do rozpakowywania, testowania oraz
przeglądania zawartości archiwów stworzonych przez program ACE.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}

%build
cp -f unix/makefile .
cp -f unix/gccmaked .
%{__make} dep \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX -DCASEINSENSE" 
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX -DCASEINSENSE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unace $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt file_id.diz
%attr(755,root,root) %{_bindir}/unace
