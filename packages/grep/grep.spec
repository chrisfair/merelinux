Summary: GNU Grep
Name: grep
Version: 2.5.4
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.gnu.org/software/grep
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}-debian_fixes-1.patch

Requires: base-layout, glibc

%description
%{name} searches one or more input files for lines
containing a match to a specified pattern.

%prep
%setup -q

%build
patch -Np1 -i %{SOURCE1}
./configure --prefix=/usr --bindir=/bin \
    --without-included-regex
make

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/usr/share/info/dir
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
/usr/bin/install-info %{_infodir}/grep.info %{_infodir}/dir

%preun
/usr/bin/install-info --delete %{_infodir}/grep.info %{_infodir}/dir

%files -f %{name}.lang
%defattr(-,root,root)
/bin/egrep
/bin/fgrep
/bin/grep
/usr/share/info/grep.info
/usr/share/man/man1/egrep.1
/usr/share/man/man1/fgrep.1
/usr/share/man/man1/grep.1

%changelog
* Tue Jul 28 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
