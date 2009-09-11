Summary: GNU M4
Name: m4
Version: 1.4.13
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.gnu.org/software/m4
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.bz2

Requires: base-layout, glibc

%description
%{name} is a macro processor. It copies its input to the output,
expanding macros as it goes.

%prep
%setup -q

%build
./configure --prefix=/usr
make
make check

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/usr/share/info/dir

%clean
rm -rf %{buildroot}

%post
/usr/bin/install-info %{_infodir}/m4.info %{_infodir}/dir

%preun
/usr/bin/install-info --delete %{_infodir}/m4.info %{_infodir}/dir

%files
%defattr(-,root,root)
/usr/bin/m4
/usr/share/info/m4.info
/usr/share/info/m4.info-1
/usr/share/info/m4.info-2
/usr/share/man/man1/m4.1

%changelog
* Tue Jul 28 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
