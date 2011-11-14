Summary: Perl Progamming Language
Name: perl
Version: 5.14.2
Release: 1
Group: Development/Languages
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.perl.org
Source0: http://www.cpan.org/src/5.0/perl-5.14.2.tar.gz

BuildRequires: digest(sha1:%{SOURCE0}) = df1549d65cdef2b20023af83ecaa2a024109a5ad
BuildRequires: util-linux
BuildRequires: zlib-devel
Provides: perl, perl(Carp::Heavy), perl(getopts.pl), perl(bigint.pl)


%description
Perl is a stable, cross platform programming language.

%package devel-docs
Group: Development/Languages
Summary: Documentation for development with perl
Requires: %{name} >= %{version}

%description devel-docs
Documentation for development with perl

%prep
%setup -q
# perl doesn't conform to POSIX sh and doesn't offer any easy workaround
mkdir bin
ln -s /bin/bash bin/sh

# we need to filter out a few auto requirements
cat > %{name}-req << "EOF"
#!/bin/sh
%{__perl_requires} "$@" | sed \
	-e '/perl(FCGI)/d' \
	-e '/perl(Mac::BuildTools)/d' \
	-e '/perl(Mac::InternetConfig)/d' \
	-e '/perl(Tk)/d' \
	-e '/perl(Tk::Pod)/d' \
	-e '/perl(VMS::Filespec)/d' \
	-e '/perl(VMS::Stdio)/d' \
	-e '/perl(NDBM_File)/d' \
	-e '/perl(Your::Module::Here)/d' \
	-e '/perl(DBD::SQLite)/d' \
	-e '/perl(DBIx::Simple)/d'
EOF
chmod +x %{name}-req
%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req

%build
sed -i -e "s|BUILD_ZLIB\s*= True|BUILD_ZLIB = False|" \
       -e "s|INCLUDE\s*= ./zlib-src|INCLUDE = /usr/include|" \
       -e "s|LIB\s*= ./zlib-src|LIB = /usr/%{_lib}|" \
       cpan/Compress-Raw-Zlib/config.in
sh Configure \
  -des \
  -Dprefix=/usr \
  -Dvendorprefix=/usr           \
  -Dman1dir=/usr/share/man/man1 \
  -Dman3dir=/usr/share/man/man3 \
  -Dpager="/usr/bin/less -isR" \
  -Duseshrplib
make %{PMFLAGS} OPTIMIZE="-Os -pipe"

%install
make DESTDIR=%{buildroot} install
install -dv %{buildroot}/usr/lib/perl5/site_perl/%{version}/$(arch)-linux/{auto,Bundle}
%{compress_man}
%{strip}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/a2p
/usr/bin/c2ph
/usr/bin/config_data
/usr/bin/corelist
/usr/bin/cpan
/usr/bin/cpan2dist
/usr/bin/cpanp
/usr/bin/cpanp-run-perl
/usr/bin/dprofpp
/usr/bin/enc2xs
/usr/bin/find2perl
/usr/bin/h2ph
/usr/bin/h2xs
/usr/bin/instmodsh
/usr/bin/json_pp
/usr/bin/libnetcfg
/usr/bin/perl
/usr/bin/perl%{version}
/usr/bin/perlbug
/usr/bin/perldoc
/usr/bin/perlivp
/usr/bin/perlthanks
/usr/bin/piconv
/usr/bin/pl2pm
/usr/bin/pod2html
/usr/bin/pod2latex
/usr/bin/pod2man
/usr/bin/pod2text
/usr/bin/pod2usage
/usr/bin/podchecker
/usr/bin/podselect
/usr/bin/prove
/usr/bin/psed
/usr/bin/pstruct
/usr/bin/ptar
/usr/bin/ptardiff
/usr/bin/ptargrep
/usr/bin/s2p
/usr/bin/shasum
/usr/bin/splain
/usr/bin/xsubpp
/usr/lib/perl5
/usr/share/man/man1/*.bz2

%files devel-docs
/usr/share/man/man3/*.bz2

%changelog
* Mon Nov 07 2011 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 5.14.2-1
- Upgrade to 5.14.2
- Optimize for size
- Separate man3 files into devel-docs package

* Sat Sep 11 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 5.12.1-2
- Create a shared perl library

* Sat Jul 17 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 5.12.1-1
- Upgrade to 5.12.1

* Thu Apr 01 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Add in UTF-8 fixes

* Sat Oct 24 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Upgrade to 5.10.1

* Tue Jul 28 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
