Summary:	unACE - extract, test and view ACE archives.
Summary(pl):	unACE - rozpakowuje, testuje i przegl±da archiwa ACE.
Name:		unace
Version:	1.2b
Release:	2
Copyright:	Freeware
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source:		http://members.aol.com/mlemke6413/%{name}pub.zip
URL:		http://members.aol.com/mlemke6413/ace.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unACE utility is a freeware program, distributed with source code and
developed for extracting, testing and viewing the contents of archives created
with the ACE archiver.

%description -l pl
UnACE jest programem freeware, rozpowszechnianym wraz z kodem ¼ród³owym, 
przeznaczonym do rozpakowywania, testowania oraz przegl±dania zawarto¶ci
archiwów stworzonych przez program ACE.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}

%build
cp unix/makefile .
cp unix/gccmaked .
make CFLAGS="$RPM_OPT_FLAGS -DUNIX -DCASEINSENSE" dep
make CFLAGS="$RPM_OPT_FLAGS -DUNIX -DCASEINSENSE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -s unace $RPM_BUILD_ROOT%{_bindir}
gzip -9fn readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt.gz
%attr(755,root,root) %{_bindir}/unace
