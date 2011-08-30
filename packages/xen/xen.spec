Summary: The Xen hypervisor
Name: xen
Version: 4.1.1
Release: 1
Group: Virtualization
License: GPL
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.xen.org
Source0: http://dev.lightcube.us/sources/%{name}/%{name}-%{version}.tar.gz

Requires: python-lxml
Requires: linux-xen
Requires: bridge-utils
BuildRequires: digest(sha1:%{SOURCE0}) = f1b5ef4b663c339faf9c77fc895327cfbcc9776c
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: Python-devel
BuildRequires: util-linux-devel
BuildRequires: pciutils-devel
BuildRequires: bridge-utils-devel
BuildRequires: dev86
BuildRequires: iasl

%description
The Xen hypervisor offers a powerful, efficient, and secure feature set for
virtualization of x86, x86_64, IA64, ARM, and other CPU architectures.

%package devel
Summary: Headers and libraries for developing with xen
Group: Development/Libraries
Requires: xen

%description devel
Headers and libraries for developing with xen

%prep
%setup -q

%build
make xen
make tools
make stubdom

%install
make DESTDIR=%{buildroot} install-xen
make DESTDIR=%{buildroot} install-tools
make DESTDIR=%{buildroot} install-stubdom
# Fix some defaults to be more sane with our setup
sed -i 's@\$remote_fs@@' %{buildroot}/etc/init.d/xend
sed -i '/relocation-server yes/s@^@#@' %{buildroot}/etc/xen/xend-config.sxp
sed -i '/unix-server/s@.*$@&\n\(xend-unix-server yes\)@' %{buildroot}/etc/xen/xend-config.sxp
%{compress_man}
rm -rf %{buildroot}/usr/src
rm -rf %{buildroot}/etc/bash*

%preun
/usr/sbin/remove_initd xencommons &>/dev/null || /bin/true
/usr/sbin/remove_initd xend &>/dev/null || /bin/true

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/boot/xen-%{version}.gz
/boot/xen-4.1.gz
/boot/xen-4.gz
/boot/xen.gz
/boot/xen-syms-%{version}
/etc/init.d/xend
/etc/init.d/xendomains
/etc/init.d/xen-watchdog
/etc/init.d/xencommons
%config /etc/sysconfig/xencommons
%config /etc/sysconfig/xendomains
/etc/udev/rules.d/xen-backend.rules
/etc/udev/rules.d/xend.rules
%dir /etc/xen
/etc/xen/cpupool
/etc/xen/xl.conf
/etc/xen/README
/etc/xen/README.incompatibilities
/etc/xen/scripts
/etc/xen/xend-config.sxp
/etc/xen/xend-pci-permissive.sxp
/etc/xen/xend-pci-quirks.sxp
%config /etc/xen/xm-config.xml
/etc/xen/xmexample.hvm
/etc/xen/xmexample.hvm-stubdom
/etc/xen/xmexample.nbd
/etc/xen/xmexample.pv-grub
/etc/xen/xmexample.vti
/etc/xen/xmexample1
/etc/xen/xmexample2
/etc/xen/xmexample3
/usr/bin/pygrub
/usr/bin/qemu-img-xen
/usr/bin/qemu-nbd-xen
/usr/bin/remus
/usr/bin/xen-detect
/usr/bin/xencons
/usr/bin/xenstore
/usr/bin/xenstore-chmod
/usr/bin/xenstore-control
/usr/bin/xenstore-exists
/usr/bin/xenstore-list
/usr/bin/xenstore-ls
/usr/bin/xenstore-read
/usr/bin/xenstore-rm
/usr/bin/xenstore-watch
/usr/bin/xenstore-write
/usr/bin/xentrace
/usr/bin/xentrace_format
/usr/bin/xentrace_setsize
/usr/lib/python2.7/site-packages/fsimage.so
/usr/lib/python2.7/site-packages/grub
/usr/lib/python2.7/site-packages/pygrub-0.3-py2.7.egg-info
/usr/lib/python2.7/site-packages/xen-3.0-py2.7.egg-info
/usr/lib/python2.7/site-packages/xen
/usr/lib/xen
/usr/%{_lib}/fs
/usr/%{_lib}/libblktap.so.3.0
/usr/%{_lib}/libblktap.so.3.0.0
/usr/%{_lib}/libflask.so.1.0
/usr/%{_lib}/libflask.so.1.0.0
/usr/%{_lib}/libfsimage.so.1.0
/usr/%{_lib}/libfsimage.so.1.0.0
/usr/%{_lib}/libvhd.so.1.0
/usr/%{_lib}/libvhd.so.1.0.0
/usr/%{_lib}/libxenctrl.so.4.0
/usr/%{_lib}/libxenctrl.so.4.0.0
/usr/%{_lib}/libxenguest.so.4.0
/usr/%{_lib}/libxenguest.so.4.0.0
/usr/%{_lib}/libxenlight.so.1.0
/usr/%{_lib}/libxenlight.so.1.0.0
/usr/%{_lib}/libxenstore.so.3.0
/usr/%{_lib}/libxenstore.so.3.0.0
/usr/%{_lib}/libxlutil.so.1.0
/usr/%{_lib}/libxlutil.so.1.0.0
/usr/%{_lib}/libblktapctl.so.1.0
/usr/%{_lib}/libblktapctl.so.1.0.0
/usr/%{_lib}/xen
/usr/sbin/xenwatchdogd
/usr/sbin/xen-hptool
/usr/sbin/xen-hvmcrash
/usr/sbin/kdd
/usr/sbin/tap-ctl
/usr/sbin/blktapctrl
/usr/sbin/flask-getenforce
/usr/sbin/flask-loadpolicy
/usr/sbin/flask-setenforce
/usr/sbin/gdbsx
/usr/sbin/gtracestat
/usr/sbin/gtraceview
/usr/sbin/img2qcow
/usr/sbin/lock-util
/usr/sbin/qcow-create
/usr/sbin/qcow2raw
/usr/sbin/tapdisk
/usr/sbin/tapdisk-client
/usr/sbin/tapdisk-diff
/usr/sbin/tapdisk-stream
/usr/sbin/tapdisk2
/usr/sbin/td-util
/usr/sbin/vhd-update
/usr/sbin/vhd-util
/usr/sbin/xen-bugtool
/usr/sbin/xen-hvmctx
/usr/sbin/xen-python-path
/usr/sbin/xen-tmem-list-parse
/usr/sbin/xenbaked
/usr/sbin/xenconsoled
/usr/sbin/xend
/usr/sbin/xenlockprof
/usr/sbin/xenmon.py
/usr/sbin/xenpaging
/usr/sbin/xenperf
/usr/sbin/xenpm
/usr/sbin/xenpmd
/usr/sbin/xenstored
/usr/sbin/xentop
/usr/sbin/xentrace_setmask
/usr/sbin/xl
/usr/sbin/xm
/usr/sbin/xsview
/usr/share/doc/xen
/usr/share/man/man1/xentop.1.bz2
/usr/share/man/man1/xentrace_format.1.bz2
/usr/share/man/man8/xentrace.8.bz2
/usr/share/xen

%files devel
%defattr (-,root,root)
/usr/include/blktaplib.h
/usr/include/fsimage.h
/usr/include/fsimage_grub.h
/usr/include/fsimage_plugin.h
/usr/include/libxl.h
/usr/include/xen
/usr/include/xenctrl.h
/usr/include/xenguest.h
/usr/include/xs.h
/usr/include/xs_lib.h
/usr/include/_libxl_types.h
/usr/include/libxl_uuid.h
/usr/include/xenctrlosdep.h
/usr/include/xentoollog.h
/usr/%{_lib}/*.a
/usr/%{_lib}/*.so

%changelog
* Mon Jun 20 2011 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 4.1.1-1
- Upgrade to 4.1.1

* Fri Dec 17 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 4.0.1-2
- Fix blktap issues and dependencies on deprecated xmlproc code

* Thu Sep 09 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 4.0.1-1
- Initial version
