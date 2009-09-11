Summary: GNU Inetutils
Name: inetutils
Version: 1.6
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.gnu.org/software/inetutils
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.gz
Source1: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}-no_server_man_pages-1.patch

Requires: base-layout, glibc

%description
%{name} is a collection of common networking programs including ftp,
telnet, ping, hostname and traceroute

%prep
%setup -q

%build
patch -Np1 -i %{SOURCE1}
./configure --prefix=/usr --libexecdir=/usr/sbin \
    --localstatedir=/var --disable-ifconfig \
    --disable-logger --disable-syslogd --disable-whois \
    --disable-servers
make

%install
make DESTDIR=%{buildroot} install
mkdir -v %{buildroot}/bin
mv -v %{buildroot}/usr/bin/ping %{buildroot}/bin
rm -f %{buildroot}/usr/share/info/dir

%clean
rm -rf %{buildroot}

%post
/usr/bin/install-info %{_infodir}/inetutils.info %{_infodir}/dir

%preun
/usr/bin/install-info --delete %{_infodir}/inetutils.info %{_infodir}/dir

%files
%defattr(-,root,root)
/bin/ping
/usr/bin/ftp
/usr/bin/hostname
/usr/bin/ping6
/usr/bin/rcp
/usr/bin/rlogin
/usr/bin/rsh
/usr/bin/talk
/usr/bin/telnet
/usr/bin/tftp
/usr/bin/traceroute
/usr/share/info/inetutils.info
/usr/share/man/man1/ftp.1
/usr/share/man/man1/rcp.1
/usr/share/man/man1/rlogin.1
/usr/share/man/man1/rsh.1
/usr/share/man/man1/talk.1
/usr/share/man/man1/telnet.1
/usr/share/man/man1/tftp.1
/usr/share/man/man8/ping.8

%changelog
* Tue Jul 28 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
