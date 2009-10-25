Summary: The Linux Kernel
Name: linux
Version: 2.6.31.4
Release: 1
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://www.kernel.org/
Source: http://dev.lightcube.us/~jhuntwork/sources/%{name}/%{name}-%{version}.tar.bz2

Requires: base-layout

%description
The Linux Kernel

%package headers
Group: Development
Summary: Linux Userspace Headers

%description headers
In order to compile anything, the Linux kernel needs to expose an
Application Programming Interface (API) for the system's C library (Glibc)
to utilize. This is done by sanitizing various C header files that are
shipped in the Linux kernel source package.

%prep
%setup -q

%build
make mrproper
make headers_install
make headers_check
make INSTALL_HDR_PATH=dest headers_install
find dest -name .install -exec rm -v '{}' \;
find dest -name ..install.cmd -exec rm -v '{}' \;

%install
mkdir -pv %{buildroot}/usr/include
cp -rv dest/include/* %{buildroot}/usr/include

%clean
rm -fr %{buildroot}

%files headers
%defattr(-,root,root)
/usr/include/asm
/usr/include/asm-generic
/usr/include/drm
/usr/include/linux
/usr/include/mtd
/usr/include/rdma
/usr/include/scsi
/usr/include/sound
/usr/include/video
/usr/include/xen

%changelog
* Sat Oct 24 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Upgrade to 2.6.31.4

* Sat Jul 18 2009 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> -
- Initial version
