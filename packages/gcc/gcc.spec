Summary: The GNU Compiler Collection
Name: gcc
Version: 4.4.1
Release: 1
Group: Development/Tools
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://gcc.gnu.org
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.bz2

Requires: base-layout, glibc, glibc-devel, linux-headers, gmp, mpfr, binutils

%description
The GNU Compiler Collection is required to compile various languages.

%package libs
Summary: GCC support libraries
Group: System Environment/Libraries

%description libs
The %{name}-libs package contains support libraries for programs
compiled using GCC.

%package c++
Summary: GCC C++ compiler
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: %{name}-c++-libs = %{version}-%{release}

%description c++
The %{name}-c++ package contains a C++ compiler to be used with GCC. It
It includes support for most of the current C++ specification, including
templates and exception handling.

%package c++-libs
Summary: GCC C++ support libraries
Group: System Environment/Libraries
Requires: %{name}-libs = %{version}-%{release}

%description c++-libs
The %{name}-c++-libs package contains support libraries for programs
compiled using GCC C++.

%prep
rm -rf %{name}-build
%setup -q

%build
sed -i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in
sed -i 's,\./fixinc\.sh,-c true,' gcc/Makefile.in
%ifarch i686
sed -i 's/^T_CFLAGS =$$/& -fomit-frame-pointer/' gcc/Makefile.in
%endif
mkdir -v ../%{name}-build
cd ../%{name}-build
../%{name}-%{version}/configure --prefix=/usr --libexecdir=/usr/lib \
 --enable-shared --enable-threads=posix --enable-__cxa_atexit \
 --enable-clocale=gnu --enable-languages=c,c++
make LDFLAGS="-s"

%install
cd ../%{name}-build
make DESTDIR=%{buildroot} install
mkdir %{buildroot}/lib
ln -sv ../usr/bin/cpp %{buildroot}/lib
ln -sv gcc %{buildroot}/usr/bin/cc
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name *.la -exec rm -v '{}' \;

%post
for i in cpp cppinternals gcc gccinstall gccint libgomp
do
  /usr/bin/install-info %{_infodir}/$i.info %{_infodir}/dir
done

%preun
for i in cpp cppinternals gcc gccinstall gccint libgomp
do
  /usr/bin/install-info --delete %{_infodir}/$i.info %{_infodir}/dir
done

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post c++-libs -p /sbin/ldconfig
%postun c++-libs -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/lib/cpp
/usr/bin/cc
/usr/bin/cpp
/usr/bin/gcc
/usr/bin/gccbug
/usr/bin/gcov
/usr/bin/*-linux-gnu-gcc
/usr/bin/*-linux-gnu-gcc-%{version}
/usr/info/cpp.info
/usr/info/cppinternals.info
/usr/info/gcc.info
/usr/info/gccinstall.info
/usr/info/gccint.info
/usr/info/libgomp.info
/usr/lib/gcc
/usr/%{_lib}/libgcc_s.so
/usr/%{_lib}/libgomp.a
/usr/%{_lib}/libgomp.so
/usr/%{_lib}/libgomp.spec
/usr/%{_lib}/libmudflap.a
/usr/%{_lib}/libmudflap.so
/usr/%{_lib}/libmudflapth.a
/usr/%{_lib}/libmudflapth.so
/usr/%{_lib}/libssp.a
/usr/%{_lib}/libssp.so
/usr/%{_lib}/libssp_nonshared.a
/usr/man/man1/gcov*
/usr/man/man1/gcc*
/usr/man/man1/cpp*
/usr/man/man7/*
/usr/share/locale/*/LC_MESSAGES/cpplib.mo
/usr/share/locale/*/LC_MESSAGES/gcc.mo

%files libs
%defattr(-,root,root)
/usr/%{_lib}/libgcc_s.so.*
/usr/%{_lib}/libgomp.so.*
/usr/%{_lib}/libmudflap.so.*
/usr/%{_lib}/libmudflapth.so.*
/usr/%{_lib}/libssp.so.*

%files c++
%defattr(-,root,root)
/usr/bin/c++
/usr/bin/g++
/usr/bin/*-linux-gnu-c++
/usr/bin/*-linux-gnu-g++
/usr/include/c++
/usr/%{_lib}/libstdc++.a
/usr/%{_lib}/libstdc++.so
/usr/%{_lib}/libsupc++.a
/usr/man/man1/g++*
/usr/share/locale/*/LC_MESSAGES/libstdc++.mo

%files c++-libs
%defattr(-,root,root)
/usr/%{_lib}/libstdc++.so.*

%changelog
* Sat Jul 25 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
