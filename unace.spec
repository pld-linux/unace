Summary:     unACE - extract, test and view ACE archives.
Summary(pl): unACE - rozpakowuje, testuje i przegl±da archiwa ACE.
Name:        unace
Version:     1.2b
Release:     1
Copyright:   Freeware
Group:       Utilities/Archiving
Group(pl):   Narzêdzia/Archiwizacja
Source:	     http://members.aol.com/mlemke6413/%{name}pub.zip
URL:         http://members.aol.com/mlemke6413/ace.html
BuildRoot:   /tmp/%{name}-%{version}-root

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
make CFLAGS="$RPM_OPT_FLAGS -dLO_HI_BYTE_ORDER -DUNIX -DCASEINSENSE" dep
make CFLAGS="$RPM_OPT_FLAGS -dLO_HI_BYTE_ORDER -DUNIX -DCASEINSENSE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin
install -s unace $RPM_BUILD_ROOT/usr/bin
bzip2 -9 readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc readme.txt.bz2
%attr(755,root,root) /usr/bin/unace

%changelog
* Thu Feb 25 1999 Maciej Le¶niewski <nimir@kis.p.lodz.pl>
  [1.2b-1]
- Initial release as a PLD package.
