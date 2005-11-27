Summary:	C API for reading and writing PCRaster maps
Summary(pl):	API C do odczytu i zapisu map PCRaster
Name:		libcsf
Version:	2.0
%define	snap	041111
Release:	0.%{snap}.2
License:	BSD
Group:		Libraries
Source0:	http://pcraster.geo.uu.nl/download/dist/%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	20f60a66ef1df2500fc44c5e8371e26f
Source1:	http://pcraster.geo.uu.nl/download/doc/csfhtml.tar.gz
# Source1-md5:	059ac4a78e04df515e9f9cb411d1eb33
Patch0:		%{name}-shared.patch
Patch1:		%{name}-endian.patch
URL:		http://pcraster.geog.uu.nl/csfapi.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C API for reading and writing PCRaster maps.

%description -l pl
API C do odczytu i zapisu map PCRaster.

%package devel
Summary:	Header files for CSF library
Summary(pl):	Pliki nag³ówkowe biblioteki CSF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CSF library.

%description devel -l pl
Pliki nag³ówkowe biblioteki CSF.

%package static
Summary:	Static CSF library
Summary(pl):	Statyczna biblioteka CSF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CSF library.

%description static -l pl
Statyczna biblioteka CSF.

%prep
%setup -q -n %{name}-%{version}-%{snap} -a1
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libcsf.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc csfhtml/*
%attr(755,root,root) %{_libdir}/libcsf.so
%{_libdir}/libcsf.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcsf.a
