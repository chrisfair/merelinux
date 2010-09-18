Summary: OpenSSH
Name: openssh
Version: 5.5p1
Release: 2
Group: Services
License: BSD
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.openssl.com
Source0: http://dev.lightcube.us/sources/%{name}/%{name}-%{version}.tar.gz
Source1: http://dev.lightcube.us/sources/%{name}/sshd.init

BuildRequires: digest(sha1:%{SOURCE0}) = 361c6335e74809b26ea096b34062ba8ff6c97cd6
BuildRequires: digest(sha1:%{SOURCE1}) = de7e20c23da063a29222ad9c753d57702e49e6cb
BuildRequires: openssl-devel
BuildRequires: zlib-devel

%description
OpenSSH is a free version of the SSH connectivity tools.

%prep
%setup -q

%build
./configure \
  --prefix=/usr \
  --sysconfdir=/etc/ssh \
  --datadir=/usr/share/sshd \
  --libexecdir=/usr/sbin \
  --with-md5-passwords \
  --with-privsep-path=/var/lib/sshd
make

%install
make DESTDIR=%{buildroot} install
install -dv %{buildroot}/var/lib/sshd
install -dv %{buildroot}/etc/{pam.d,init.d}
install -m754 %{SOURCE1} %{buildroot}/etc/init.d/sshd
cat > %{buildroot}/etc/pam.d/sshd << "EOF"
# Begin /etc/pam.d/sshd

auth        requisite      pam_nologin.so
auth        required       pam_securetty.so
auth        required       pam_unix.so
account     required       pam_access.so
account     required       pam_unix.so
session     required       pam_env.so
session     required       pam_motd.so
session     required       pam_limits.so
session     optional       pam_mail.so      dir=/var/mail standard
session     optional       pam_lastlog.so
session     required       pam_unix.so
password    required       pam_cracklib.so  retry=3
password    required       pam_unix.so      md5 shadow use_authtok

# End /etc/pam.d/sshd
EOF

%post
/usr/sbin/install_initd sshd
if [ ! -f /etc/ssh/ssh_host_key ]
   then /usr/bin/ssh-keygen -t rsa1 -f /etc/ssh/ssh_host_key -N "" >/dev/null 2>&1
fi
if [ ! -f /etc/ssh/ssh_host_rsa_key ]
   then /usr/bin/ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N "" >/dev/null 2>&1
fi
if [ ! -f /etc/ssh/ssh_host_dsa_key ]
   then /usr/bin/ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N "" >/dev/null 2>&1
fi

%preun
/usr/sbin/remove_initd sshd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/pam.d/sshd
/etc/init.d/sshd
/etc/ssh
/usr/bin/scp
/usr/bin/sftp
/usr/bin/slogin
/usr/bin/ssh*
/usr/sbin/sftp-server
/usr/sbin/ssh*
/usr/share/man/man1/*
/usr/share/man/man5/*
/usr/share/man/man8/*
/var/lib/sshd

%changelog
* Sat Sep 18 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 5.5p1-2
- Add host keys on install, if they don't exist

* Tue Aug 10 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 5.5p1-1
- Upgraded to 5.5p1 and added support for lsb bootscripts

* Wed Apr 14 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 5.4p1-1
- Initial version
