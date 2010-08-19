Summary: udev
Name: udev
Version: 160
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: http://dev.lightcube.us/~jhuntwork/sources/%{name}-config/%{name}-config-20100128.tar.bz2

Requires: base-layout, glibc
BuildRequires: digest(%{SOURCE0}) = 65459a1f090082c0471bf4e5112208d7
BuildRequires: digest(%{SOURCE1}) = 8c8ad22d6fb9aa7c0733d33035204ea2

%description
Udev provides a dynamic /dev directory, and hooks userspace into kernel device events.

%package devel
Requires: %{name}

%description devel
Files for developing with %{name}

%prep
%setup -q

%build
tar -xf %{SOURCE1}
./configure \
  --prefix=/usr \
  --sysconfdir=/etc \
  --sbindir=/sbin \
  --with-rootlibdir=/%{_lib} \
  --libexecdir=/lib/udev \
  --disable-extras \
  --libdir=/usr/%{_lib} \
  --disable-introspection \
  --with-html-dir=/usr/share/doc/%{name}
make

%install
install -dv %{buildroot}/lib/udev/devices/{pts,shm}
make DESTDIR=%{buildroot} install
sed -i.bak 's@include$@&\nudevdir=/lib/udev@' %{buildroot}/usr/%{_lib}/pkgconfig/libudev.pc
mknod -m0666 %{buildroot}/lib/udev/devices/null c 1 3
cd udev-config-20100128
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/udev
/%{_lib}/libudev.so.0
/%{_lib}/libudev.so.0.8.3
/lib/udev
/sbin/udevadm
/sbin/udevd
/usr/share/doc/udev-config
/usr/share/man/man7/udev.7
/usr/share/man/man8/scsi_id.8
/usr/share/man/man8/udevadm.8
/usr/share/man/man8/udevd.8

%files devel
%defattr(-,root,root)
/usr/include/libudev.h
/usr/%{_lib}/libudev.so
/usr/%{_lib}/libudev.la
/usr/%{_lib}/pkgconfig/libudev.pc
/usr/share/pkgconfig/udev.pc
/usr/share/doc/udev

%changelog
* Sun Aug 08 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 160-1
- Upgrade to 160

* Sat Apr 10 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 151-1
- Initial version
