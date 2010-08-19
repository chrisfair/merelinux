Summary: Net:Iproute2
Name: iproute2
Version: 2.6.35
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.linuxfoundation.org/en/Net:Iproute2
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.bz2

Requires: base-layout, glibc
BuildRequires: digest(%{SOURCE0}) = b0f281b3124bf04669e18f5fe16d4934
BuildRequires: db-devel

%description
Iproute2 is a collection of utilities for controlling
TCP/IP networking and traffic control in Linux

%package arpd
Summary: arpd binary
Requires: %{name}, db

%description arpd
The aprd binary

%prep
%setup -q

%build
make DESTDIR= LIBDIR=/%{_lib}

%install
make DESTDIR=%{buildroot} SBINDIR=/sbin MANDIR=/usr/share/man \
     LIBDIR=/%{_lib} DOCDIR=/usr/share/doc/%{name}-%{version} install
rm -v %{buildroot}/usr/share/man/man3/libnetlink.3

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/iproute2
/%{_lib}/tc
/sbin/ctstat
/sbin/genl
/sbin/ifcfg
/sbin/ifstat
/sbin/ip
/sbin/lnstat
/sbin/nstat
/sbin/routef
/sbin/routel
/sbin/rtacct
/sbin/rtmon
/sbin/rtpr
/sbin/rtstat
/sbin/ss
/sbin/tc
/usr/share/doc/%{name}-%{version}
/usr/share/man/man8/ctstat.8
/usr/share/man/man8/ip.8
/usr/share/man/man8/lnstat.8
/usr/share/man/man8/nstat.8
/usr/share/man/man8/routef.8
/usr/share/man/man8/routel.8
/usr/share/man/man8/rtacct.8
/usr/share/man/man8/rtmon.8
/usr/share/man/man8/rtstat.8
/usr/share/man/man8/ss.8
/usr/share/man/man8/tc-bfifo.8
/usr/share/man/man8/tc-cbq-details.8
/usr/share/man/man8/tc-cbq.8
/usr/share/man/man8/tc-drr.8
/usr/share/man/man8/tc-htb.8
/usr/share/man/man8/tc-pfifo.8
/usr/share/man/man8/tc-pfifo_fast.8
/usr/share/man/man8/tc-prio.8
/usr/share/man/man8/tc-red.8
/usr/share/man/man8/tc-sfq.8
/usr/share/man/man8/tc-tbf.8
/usr/share/man/man8/tc.8

%files arpd
%defattr(-,root,root)
/sbin/arpd
/usr/share/man/man8/arpd.8

%changelog
* Sun Aug 08 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 2.6.35-1
- Upgrade to 2.6.35

* Wed Apr 14 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 2.6.33-2
- Separate the aprd binary due to its dependence on db

* Thu Apr 01 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 2.6.33-1
- Upgraded to 2.6.33-1

* Fri Aug 14 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
