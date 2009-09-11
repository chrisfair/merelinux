Summary: Gzip compression utility
Name: gzip
Version: 1.3.12
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.gnu.org/software/gzip
Source: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.gz

Requires: base-layout, glibc

%description
The GNU zip compression utility.

%prep
%setup -q

%build
sed -i 's/futimens/gl_&/' gzip.c lib/utimens.{c,h}
sed -i 's/5 -)/5 - >\&3)/' zdiff.in
./configure --prefix=/usr --bindir=/bin
make
make check

%install
make DESTDIR=%{buildroot} install
mkdir -pv %{buildroot}/usr/bin
mv -v %{buildroot}/bin/{gzexe,uncompress,zcmp,zdiff,zegrep} %{buildroot}/usr/bin
mv -v %{buildroot}/bin/{zfgrep,zforce,zgrep,zless,zmore,znew} %{buildroot}/usr/bin
rm -f %{buildroot}/usr/share/info/dir

%post
/usr/bin/install-info %{_infodir}/gzip.info %{_infodir}/dir

%preun
/usr/bin/install-info --delete %{_infodir}/gzip.info %{_infodir}/dir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/bin/gunzip
/bin/gzip
/bin/zcat
/usr/bin/gzexe
/usr/bin/uncompress
/usr/bin/zcmp
/usr/bin/zdiff
/usr/bin/zegrep
/usr/bin/zfgrep
/usr/bin/zforce
/usr/bin/zgrep
/usr/bin/zless
/usr/bin/zmore
/usr/bin/znew
/usr/share/info/gzip.info
/usr/share/man/man1/gunzip.1
/usr/share/man/man1/gzexe.1
/usr/share/man/man1/gzip.1
/usr/share/man/man1/zcat.1
/usr/share/man/man1/zcmp.1
/usr/share/man/man1/zdiff.1
/usr/share/man/man1/zforce.1
/usr/share/man/man1/zgrep.1
/usr/share/man/man1/zless.1
/usr/share/man/man1/zmore.1
/usr/share/man/man1/znew.1

%changelog
* Fri Aug 14 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
