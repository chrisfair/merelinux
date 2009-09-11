Summary: Fine Free File Command
Name: file
Version: 5.03
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://darwinsys.com/file
Source: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.gz

Requires: base-layout, glibc

%package devel
Summary: Libraries and headers for developing with libmagic
Group: Development/Libraries

%description
The file command is "a file type guesser", that is, a command-line tool that tells you in words what kind of data a file contains.
file does not rely on filename extensions, but looks at the contents of a file to determine its type.

%description devel
Libraries and headers for developing with libmagic

%prep
%setup -q

%build
./configure --prefix=/usr --libdir=/usr/%{_lib}
make
make check

%install
make DESTDIR=%{buildroot} install
rm -v %{buildroot}/usr/%{_lib}/libmagic.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/file
/usr/%{_lib}/libmagic.so.1
/usr/%{_lib}/libmagic.so.1.0.0
/usr/share/man/man1/file.1
/usr/share/man/man4/magic.4
/usr/share/misc/magic.mgc

%files devel
%defattr(-,root,root)
/usr/include/magic.h
/usr/%{_lib}/libmagic.a
/usr/%{_lib}/libmagic.so
/usr/share/man/man3/libmagic.3

%changelog
* Fri Aug 14 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
