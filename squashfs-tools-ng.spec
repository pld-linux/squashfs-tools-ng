Summary:	A new set of tools and libraries for working with SquashFS images
Name:		squashfs-tools-ng
Version:	0.8
Release:	1
License:	LGPL v3+
Group:		Base/Utilities
Source0:	https://infraroot.at/pub/squashfs/%{name}-%{version}.tar.xz
# Source0-md5:	a4388e410178e9d5c7058c773d656c44
URL:		https://github.com/AgentD/squashfs-tools-ng
BuildRequires:	attr-devel
BuildRequires:	lz4-devel
BuildRequires:	lzo-devel >= 2.04
BuildRequires:	xz-devel >= 5.0.0
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
%ifarch %{x8664}
Requires:	libgcc_s.so.1()(64bit)
%else
Requires:	libgcc_s.so.1
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains utilities for squashfs filesystem.

%package -n squashfs-libs
Summary:	squashfs library
Summary(pl.UTF-8):	Biblioteka squashfs
Group:		Development/Libraries

%description -n squashfs-libs
squashfs library.

%description -n squashfs-libs -l pl.UTF-8
Biblioteka squashfs.

%package -n squashfs-devel
Summary:	Header files for squashfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki squashfs
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description -n squashfs-devel
Header files for squashfs library.

%description -n squashfs-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki squashfs.

%package -n squashfs-static
Summary:	Static squashfs library
Summary(pl.UTF-8):	Statyczna biblioteka squashfs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n squashfs-static
Static squashfs library.

%description -n squashfs-static -l pl.UTF-8
Statyczna biblioteka squashfs.

%prep
%setup -q
#-n %{name}%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n squashfs-libs -p /sbin/ldconfig
%postun	-n squashfs-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

%files -n squashfs-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsquashfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsquashfs.so.0

%files -n squashfs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsquashfs.so
%{_includedir}/sqfs
%{_pkgconfigdir}/libsquashfs0.pc

%files -n squashfs-static
%defattr(644,root,root,755)
%{_libdir}/libsquashfs.a
