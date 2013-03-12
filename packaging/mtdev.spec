Name:       mtdev
Summary:    A library to transform all kernel MT events to protocol B (slotted)
Version:    1.1.3
Release:    1
Group:      System/X Hardware Support
License:    MIT
URL:        http://bitmath.org/code/mtdev/
Source0:    %{name}-%{version}.tar.gz
Source1001: mtdev.manifest
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  autoconf
BuildRequires:  libtool

%description
mtdev - The mtdev is a stand-alone library which transforms all variants of
kernel MT events to the slotted type B protocol. The events put into mtdev
may be from any MT device, specifically type A without contact tracking,
type A with contact tracking, or type B with contact tracking. See the
kernel documentation for further details. The bulk of the mtdev code has
been out there since 2008, as part of the Multitouch X Driver. With this
package, finger tracking and seamless MT protocol handling is available
under a free license.

%package devel
Summary:    Development header files for use with mtdev
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development header files for use with mtdev

%prep
%setup -q

%build
cp %{SOURCE1001} .
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest mtdev.manifest
%{_libdir}/libmtdev.so.*

%files devel
%manifest mtdev.manifest
%defattr(-,root,root,-)
%{_bindir}/mtdev-test
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc
%{_includedir}/mtdev*.h

