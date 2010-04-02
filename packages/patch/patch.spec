Summary: GNU Patch
Name: patch
Version: 2.6.1
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://savannah.gnu.org/projects/patch
Source0: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.bz2

Requires: base-layout, glibc
BuildRequires: digest(%{SOURCE0}) = 0818d1763ae0c4281bcdc63cdac0b2c0

%description
Patch allows merging of textual changes

%prep
%setup -q

%build
./configure --prefix=/usr --mandir=/usr/share/man
make

%install
make prefix=%{buildroot}/usr mandir=%{buildroot}/usr/share/man install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/patch
/usr/share/man/man1/patch.1

%changelog
* Thu Apr 01 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 2.6.1-1
- Upgrade to 2.6.1

* Fri Aug 14 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
