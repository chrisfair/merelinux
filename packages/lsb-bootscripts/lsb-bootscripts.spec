Summary: LFS LSB Bootscripts
Name: lsb-bootscripts
Version: 3
Release: 2
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
Buildarch: noarch
URL: http://www.linuxfromscratch.org/lfs
Source0: http://dev.lightcube.us/sources/%{name}/lsb-v%{version}.tar.bz2
Source1: http://dev.lightcube.us/sources/%{name}/service

BuildRequires: digest(sha1:%{SOURCE0}) = 8ccc03c42c4e29d579fa124743ebeef966485ece
BuildRequires: digest(sha1:%{SOURCE1}) = d935be1993dbf647d9bba00f95b0d0982227d47a

%description
LSB compatible bootscripts from the LFS project.

%prep
%setup -q -n lsb-v%{version}

%install
# Fix syntax error
sed -i 's@\]@& ; then@' init.d/sendsignals
# LightCube specifics
sed -i -e 's@Linux From Scratch@LightCube OS@g' \
  -e 's/lfs-dev@linuxfromscratch.org/support@lightcube.us/' \
  -e 's/DISTRO_MINI=.*/DISTRO_MINI="lightcube"/' \
  -e 's@lfs-functions@lightcube-functions@' sysconfig/rc.site
make DESTDIR=%{buildroot} install
install -dv %{buildroot}/usr/sbin
install -m 754 %{SOURCE1} %{buildroot}/usr/sbin/service
mv -v %{buildroot}/etc/init.d/{lfs,lightcube}-functions

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/init.d
%config /etc/inittab
/etc/lsb
/etc/rc0.d
/etc/rc1.d
/etc/rc2.d
/etc/rc3.d
/etc/rc4.d
/etc/rc5.d
/etc/rc6.d
/etc/rcS.d
/etc/sysconfig/createfiles
/etc/sysconfig/modules
/etc/sysconfig/network-devices
/etc/sysconfig/rc
/etc/sysconfig/rc.site
/lib/lsb/init-functions
/lib/lsb/manage-functions
/usr/sbin/service

%changelog
* Sun Sep 12 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 3-2
- Fix quotes in service script

* Mon Aug 23 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 3-1
- Initial version
