Summary: Postfix MTA
Name: postfix
Version: 2.7.1
Release: 1
Group: Services
License: IBM Public License
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.postfix.org
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.gz
Source1: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}.init

BuildRequires: digest(%{SOURCE0}) = b7a5c3ccd309156a65d6f8d2683d4fa1
BuildRequires: digest(%{SOURCE1}) = 6b5839cdeaa91b671134e60f41c4e24d
BuildRequires: db-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: cyrus-sasl-devel

%description
Postfix is Wietse Venema's mailer that started life at IBM research as an
alternative to the widely-used Sendmail program.
Postfix attempts to be fast, easy to administer, and secure. The outside has
a definite Sendmail-ish flavor, but the inside is completely different.

%prep
%setup -q

%build
export CFLAGS="%{CFLAGS}"
export LDFLAGS="%{LDFLAGS}"
make makefiles \
     CCARGS='%{CFLAGS} -DDEF_DAEMON_DIR=\"/usr/lib/postfix\" -DUSE_SASL_AUTH -DUSE_CYRUS_SASL -DDEF_MANPAGE_DIR=\"/usr/share/man\" -DHAS_PCRE -DUSE_TLS -I/usr/include/sasl/ -I/usr/include/openssl/' \
     AUXLIBS='-L/usr/%{_lib} -lsasl2 -lpcre -ldb -lz -lm -lssl -lcrypto %{LDFLAGS}'
make

%install
sh postfix-install -non-interactive install_root=%{buildroot}
install -dv %{buildroot}/etc/init.d
install -m754 %{SOURCE1} %{buildroot}/etc/init.d/%{name}
#install -dv %{buildroot}/var/spool/postfix

%post
/usr/sbin/install_initd postfix

%preun
/usr/sbin/remove_initd postfix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/postfix
/etc/init.d/postfix
/usr/bin/mailq
/usr/bin/newaliases
/usr/lib/postfix
/usr/sbin/postalias
/usr/sbin/postcat
/usr/sbin/postconf
/usr/sbin/postfix
/usr/sbin/postkick
/usr/sbin/postlock
/usr/sbin/postlog
/usr/sbin/postmap
/usr/sbin/postmulti
/usr/sbin/postsuper
/usr/sbin/sendmail
/usr/share/man/man1/mailq.1
/usr/share/man/man1/newaliases.1
/usr/share/man/man1/postalias.1
/usr/share/man/man1/postcat.1
/usr/share/man/man1/postconf.1
/usr/share/man/man1/postdrop.1
/usr/share/man/man1/postfix.1
/usr/share/man/man1/postkick.1
/usr/share/man/man1/postlock.1
/usr/share/man/man1/postlog.1
/usr/share/man/man1/postmap.1
/usr/share/man/man1/postmulti.1
/usr/share/man/man1/postqueue.1
/usr/share/man/man1/postsuper.1
/usr/share/man/man1/sendmail.1
/usr/share/man/man5/access.5
/usr/share/man/man5/aliases.5
/usr/share/man/man5/body_checks.5
/usr/share/man/man5/bounce.5
/usr/share/man/man5/canonical.5
/usr/share/man/man5/cidr_table.5
/usr/share/man/man5/generic.5
/usr/share/man/man5/header_checks.5
/usr/share/man/man5/ldap_table.5
/usr/share/man/man5/master.5
/usr/share/man/man5/mysql_table.5
/usr/share/man/man5/nisplus_table.5
/usr/share/man/man5/pcre_table.5
/usr/share/man/man5/pgsql_table.5
/usr/share/man/man5/postconf.5
/usr/share/man/man5/postfix-wrapper.5
/usr/share/man/man5/regexp_table.5
/usr/share/man/man5/relocated.5
/usr/share/man/man5/tcp_table.5
/usr/share/man/man5/transport.5
/usr/share/man/man5/virtual.5
/usr/share/man/man8/anvil.8
/usr/share/man/man8/bounce.8
/usr/share/man/man8/cleanup.8
/usr/share/man/man8/defer.8
/usr/share/man/man8/discard.8
/usr/share/man/man8/error.8
/usr/share/man/man8/flush.8
/usr/share/man/man8/lmtp.8
/usr/share/man/man8/local.8
/usr/share/man/man8/master.8
/usr/share/man/man8/oqmgr.8
/usr/share/man/man8/pickup.8
/usr/share/man/man8/pipe.8
/usr/share/man/man8/proxymap.8
/usr/share/man/man8/qmgr.8
/usr/share/man/man8/qmqpd.8
/usr/share/man/man8/scache.8
/usr/share/man/man8/showq.8
/usr/share/man/man8/smtp.8
/usr/share/man/man8/smtpd.8
/usr/share/man/man8/spawn.8
/usr/share/man/man8/tlsmgr.8
/usr/share/man/man8/trace.8
/usr/share/man/man8/trivial-rewrite.8
/usr/share/man/man8/verify.8
/usr/share/man/man8/virtual.8
%dir /var/spool/postfix
%defattr(-,postfix,postfix)
/var/spool/postfix/active
/var/spool/postfix/bounce
/var/spool/postfix/corrupt
/var/spool/postfix/defer
/var/spool/postfix/deferred
/var/spool/postfix/flush
/var/spool/postfix/hold
/var/spool/postfix/incoming
/var/spool/postfix/private
/var/spool/postfix/saved
/var/spool/postfix/trace
%defattr(-,postfix,postdrop)
/var/spool/postfix/public
/var/spool/postfix/maildrop
%defattr(2755,root,postdrop)
/usr/sbin/postdrop
/usr/sbin/postqueue

%changelog
* Tue Aug 10 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 2.7.1-1
- Initial version
